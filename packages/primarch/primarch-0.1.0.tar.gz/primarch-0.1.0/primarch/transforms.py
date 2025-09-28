from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    import polars as pl
    import tooltime


def trim_finalized_markets(metrics: pl.DataFrame) -> pl.DataFrame:
    """Remove all but the first finalized data point for each market"""
    import polars as pl

    return (
        metrics.with_columns(
            first_appearance=pl.struct(
                pl.col.contract_ticker, pl.col.status
            ).is_first_distinct()
        )
        .filter((pl.col.status != 'finalized') | (pl.col.first_appearance))
        .drop('first_appearance')
    )


def get_metrics_subrange(
    metrics: pl.DataFrame,
    *,
    start_time: tooltime.Timestamp | None = None,
    end_time: tooltime.Timestamp | None = None,
    duration: str | None = None,
) -> pl.DataFrame:
    import polars as pl
    import tooltime
    import datetime

    if start_time is None and end_time is None and duration is None:
        raise ValueError('must specify two of start_time, end_time, duration')
    if duration == 'all':
        start_time = metrics['timestamp'].min()  # type: ignore
        end_time = metrics['timestamp'].max()  # type: ignore
    if start_time is None:
        if duration is not None and end_time is not None:
            start_time = tooltime.timestamp_to_seconds(
                end_time
            ) - tooltime.timelength_to_seconds(duration)
        else:
            raise ValueError(
                'must specify two of start_time, end_time, duration'
            )
    if end_time is None:
        if duration is not None and start_time is not None:
            end_time = tooltime.timestamp_to_seconds(
                start_time
            ) + tooltime.timelength_to_seconds(duration)
        else:
            raise ValueError(
                'must specify two of start_time, end_time, duration'
            )

    start_time = tooltime.timestamp_to_datetime(start_time).replace(
        tzinfo=datetime.timezone.utc
    )
    end_time = tooltime.timestamp_to_datetime(end_time).replace(
        tzinfo=datetime.timezone.utc
    )

    filtered = metrics.filter(
        pl.col.timestamp >= start_time, pl.col.timestamp < end_time
    )
    return (
        filtered.group_by('contract_ticker', maintain_order=True)
        .agg(**_get_resample_columns())
        .with_columns(timestamp=pl.lit(start_time))
        .select(
            *metrics.columns,
            end_timestamp=pl.lit(end_time),
            min_timestamp=pl.lit(filtered['timestamp'].min()),
            max_timestamp=pl.lit(filtered['timestamp'].max()),
        )
    )


def get_metrics_by_category(metrics: pl.DataFrame) -> pl.DataFrame:
    import polars as pl

    return metrics.group_by('timestamp', 'category', maintain_order=True).agg(
        pl.col.volume.sum(),
        pl.col.open_interest.sum(),
        pl.col.series_ticker.n_unique().alias('event_types'),
        pl.col.contract_ticker.n_unique().alias('contracts'),
        pl.col.subcategory.n_unique().alias('subcategories'),
    )


def downsample_metrics(
    metrics: pl.DataFrame, timescale: str, *, include_status: bool = False
) -> pl.DataFrame:
    import polars as pl

    if not include_status and 'status' in metrics.columns:
        metrics = metrics.drop('status')

    if timescale == 'all':
        timescale = '100y'

    if timescale.endswith('w'):
        timestamp = (
            pl.col.timestamp.dt.offset_by('1d')
            .dt.truncate(timescale)
            .dt.offset_by('-1d')
        )
    else:
        timestamp = pl.col.timestamp.dt.truncate(timescale)

    resample_columns = {
        k: v
        for k, v in _get_resample_columns().items()
        if k in metrics.columns or k in {'min_time', 'max_time'}
    }
    return (
        metrics.group_by(
            timestamp=timestamp,
            contract_ticker='contract_ticker',
            maintain_order=True,
        )
        .agg(**resample_columns)
        .select(*metrics.columns, 'min_time', 'max_time')
    )


def _get_resample_columns() -> dict[str, pl.Expr]:
    import polars as pl

    return dict(
        series_ticker=pl.col.series_ticker.first(),
        category=pl.col.category.first(),
        subcategory=pl.col.subcategory.first(),
        series_title=pl.col.series_title.first(),
        volume=pl.col.volume.sum(),
        open_interest=pl.col.open_interest.first(),
        status=pl.col.status.unique(),
        min_time=pl.col.timestamp.min(),
        max_time=pl.col.timestamp.max(),
    )


def add_event_slugs(metrics: pl.DataFrame) -> pl.DataFrame:
    all_contracts = (
        metrics.unique(('series_ticker', 'contract_ticker', 'series_title'))
        .select('series_ticker', 'contract_ticker', 'series_title')
        .with_columns(
            n_series_dashes=pl.col.series_ticker.str.count_matches('-'),
            n_contract_dashes=pl.col.contract_ticker.str.count_matches('-'),
        )
    )

    event_slugs = all_contracts.filter(
        pl.col.n_series_dashes + 2 == pl.col.n_contract_dashes,
        pl.col.contract_ticker.str.starts_with(pl.col.series_ticker)
        | pl.col.contract_ticker.str.starts_with('KX' + pl.col.series_ticker),
    ).with_columns(
        event_slug=pl.col.contract_ticker.str.split('-').list.get(1),
    )

    return metrics.join(
        event_slugs.select('contract_ticker', 'event_slug'),
        on='contract_ticker',
        how='left',
    )
