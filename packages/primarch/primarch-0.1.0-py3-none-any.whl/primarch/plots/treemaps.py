from __future__ import annotations

import typing
from .. import transforms

if typing.TYPE_CHECKING:
    import polars as pl
    import tooltree
    import tooltime


def plot_treemap(
    metrics: pl.DataFrame,
    metric: typing.Literal['volume', 'open_interest'],
    *,
    timescale: str | None = None,
    start_timestamp: tooltime.Timestamp | None = None,
    end_timestamp: tooltime.Timestamp | None = None,
    levels: list[str] = ['category', 'series_title', 'contract_ticker'],
    max_children: int = 100,
    min_child_fraction: float = 0.0001,
    max_depth: int = 3,
    plot_kwargs: dict[str, typing.Any] | None = None,
) -> tooltree.TreemapPlot:
    import tooltree
    import polars as pl

    if metric == 'volume':
        if (
            timescale is None
            and start_timestamp is None
            and end_timestamp is None
        ):
            timescale = '1d'
        if start_timestamp is None and end_timestamp is None:
            end_timestamp = metrics['timestamp'].max()  # type: ignore
        data = transforms.get_metrics_subrange(
            metrics,
            start_time=start_timestamp,
            end_time=end_timestamp,
            duration=timescale,
        )
    elif metric == 'open_interest':
        if start_timestamp is None:
            start_timestamp = metrics['timestamp'].max()  # type: ignore
        data = metrics.filter(timestamp=start_timestamp)
    else:
        raise Exception('invalid metric: ' + metric)

    if plot_kwargs is None:
        plot_kwargs = {}

    return tooltree.plot_treemap(
        data,
        levels=levels,
        metric=metric,
        root=_get_title(data=data, metric=metric, timescale=timescale),
        metric_format=_get_dollar_format(),
        height=700,
        max_depth=max_depth,
        max_children=max_children,
        min_child_fraction=min_child_fraction,
        **plot_kwargs,
    )


def _get_dollar_format() -> dict[str, typing.Any]:
    return {'order_of_magnitude': True, 'decimals': 1, 'prefix': '$'}


def _get_title(data: pl.DataFrame, metric: str, timescale: str | None) -> str:
    if metric == 'open_interest':
        timerange_str = '[' + str(data['timestamp'].max())[:10] + ']'
        return 'Kalshi ' + metric.title() + ' ' + timerange_str

    if timescale is None:
        raise Exception('timescale must be specified for volume metric')
    timerange_str = (
        '['
        + str(data['min_timestamp'][0])[:10]
        + ', '
        + str(data['max_timestamp'][0])[:10]
        + ']'
    )
    if timescale == '1d':
        timerange_str = '[' + str(data['timestamp'].max())[:10] + ']'
        title = 'Kalshi ' + metric.title() + ' Over Past 24H'
    elif timescale == 'all':
        title = 'Kalshi Lifetime ' + metric.title()
    else:
        title = 'Kalshi ' + metric.title() + ' Over Past ' + timescale
    return title + ' ' + timerange_str
