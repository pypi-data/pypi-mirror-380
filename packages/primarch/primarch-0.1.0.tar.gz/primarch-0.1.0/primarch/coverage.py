from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    import polars as pl


def print_data_summary(data: pl.DataFrame) -> None:
    import toolstr

    toolstr.print_text_box('Data Summary')
    print(
        '- data range: ['
        + str(data['timestamp'].min())[:10]
        + ', '
        + str(data['timestamp'].max())[:10]
        + ']'
    )
    print('- categories:', data['category'].n_unique())
    print('- subcategories:', toolstr.format(data['subcategory'].n_unique()))
    print('- event types:', toolstr.format(data['series_ticker'].n_unique()))
    print('- contracts:', toolstr.format(data['contract_ticker'].n_unique()))


def get_category_coverage(
    uncategorized: pl.DataFrame, data: pl.DataFrame
) -> pl.DataFrame:
    import datetime
    import polars as pl

    max_timestamp = data['timestamp'].max()
    last_24H = pl.col.timestamp == max_timestamp
    last_7D = pl.col.timestamp >= max_timestamp - datetime.timedelta(days=7)  # type: ignore
    last_30D = pl.col.timestamp >= max_timestamp - datetime.timedelta(days=30)  # type: ignore

    return uncategorized.select(
        (
            1
            - pl.col.volume.filter(last_24H).sum()
            / data.filter(last_24H)['volume'].sum()
        ).alias('last\n24H'),
        (
            1
            - pl.col.volume.filter(last_7D).sum()
            / data.filter(last_7D)['volume'].sum()
        ).alias('last\n7D'),
        (
            1
            - pl.col.volume.filter(last_30D).sum()
            / data.filter(last_30D)['volume'].sum()
        ).alias('last\n30D'),
        (1 - pl.col.volume.sum() / data['volume'].sum()).alias('all\ntime'),
    )


def get_coverage(data: pl.DataFrame) -> pl.DataFrame:
    import polars as pl

    categorized_filter = ~pl.col.category.is_in(['World', 'Unknown'])
    subcategorized_filter = categorized_filter & (
        pl.col.series_title != pl.col.subcategory
    )

    # category coverage
    uncategorized_coverage = get_category_coverage(
        data.filter(~categorized_filter),
        data,
    )

    # subcategory coverage
    unsubcategorized_coverage = get_category_coverage(
        data.filter(~subcategorized_filter),
        data,
    )

    # combine all
    return pl.concat(
        [
            uncategorized_coverage,
            unsubcategorized_coverage,
        ]
    ).insert_column(
        0,
        pl.Series(['categorized', 'subcategorized']),
    )


def print_coverage(metrics: pl.DataFrame) -> None:
    import toolstr

    coverage = get_coverage(metrics)
    toolstr.print_text_box('Volume Label Coverage')
    column_formats = {
        'last\n24H': {'percentage': True, 'decimals': 2},
        'last\n7D': {'percentage': True, 'decimals': 2},
        'last\n30D': {'percentage': True, 'decimals': 2},
        'all\ntime': {'percentage': True, 'decimals': 2},
    }
    toolstr.print_dataframe_as_table(
        coverage, compact=3, column_formats=column_formats
    )
