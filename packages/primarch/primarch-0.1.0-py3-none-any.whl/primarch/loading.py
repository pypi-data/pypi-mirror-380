from __future__ import annotations

import polars as pl
from . import transforms
from . import categories


def load_kalshi_data(
    *,
    timescale: str = '1d',
    trim_finalized: bool = True,
    add_subcategories: bool = True,
) -> pl.DataFrame:
    import absorb

    raw_metrics = absorb.query('kalshi.metrics')
    metadata = absorb.query('kalshi.metadata')
    metrics = _join_series_metadata(raw_metrics, metadata).select(
        timestamp='timestamp',
        series_ticker=pl.col.series_ticker.fill_null('Unknown'),
        contract_ticker='ticker_name',
        category=pl.col.category.fill_null('Unknown'),
        series_title=pl.col.series_title.fill_null('Unknown'),
        open_interest='open_interest',
        volume='daily_volume',
        status='status',
    )

    if trim_finalized:
        metrics = transforms.trim_finalized_markets(metrics)

    metrics = _refactor_raw_categories(metrics)
    if add_subcategories:
        metrics = categories.populate_subcategories(metrics)
        metrics = metrics.with_columns(
            pl.col.subcategory.fill_null(pl.col.series_title)
        )

    if timescale == '1d':
        return metrics
    else:
        return transforms.downsample_metrics(metrics, timescale=timescale)


def _join_series_metadata(
    kalshi_metrics: pl.DataFrame, kalshi_metadata: pl.DataFrame
) -> pl.DataFrame:
    """add series columns

    columns
    - series_ticker
    - category
    - series_title
    """
    joined_series = (
        kalshi_metrics.select(pl.col.report_ticker.unique())
        .join(
            kalshi_metadata.unique('series_ticker').select(
                'series_ticker', 'series_title', 'category'
            ),
            left_on='report_ticker',
            right_on='series_ticker',
            how='left',
            coalesce=False,
        )
        .join(
            kalshi_metadata.unique('series_ticker').select(
                'series_ticker', 'series_title', 'category'
            ),
            left_on='KX' + pl.col.report_ticker.str.to_uppercase(),
            right_on='series_ticker',
            how='left',
            coalesce=False,
        )
        .select(
            'report_ticker',
            series_ticker=pl.coalesce('series_ticker', 'series_ticker_right'),
            series_title=pl.coalesce('series_title', 'series_title_right'),
            category=pl.coalesce('category', 'category_right'),
        )
        .join(
            _get_manual_series_metadata(),
            left_on='report_ticker',
            right_on='series_ticker',
            how='left',
            coalesce=False,
        )
        .select(
            'report_ticker',
            series_ticker=pl.coalesce('series_ticker', 'series_ticker_right'),
            series_title=pl.coalesce('series_title_right', 'series_title'),
            category=pl.coalesce('category_right', 'category'),
        )
    )

    return kalshi_metrics.join(joined_series, on='report_ticker', how='left')


def _get_manual_series_metadata() -> pl.DataFrame:
    # (series_ticker, category, series_title)
    manual_series_metadata = [
        #
        # financials
        ('NASDAQ100D', 'NASDAQ100D', 'Financials'),
        ('NASDAQ100W', 'NASDAQ100W', 'Financials'),
        ('NASDAQ100DU', 'NASDAQ100DU', 'Financials'),
        ('NASDAQ100M', 'NASDAQ100M', 'Financials'),
        ('INXD', 'S&P 500 daily', 'Financials'),
        ('INXW', 'S&P 500 weekly', 'Financials'),
        ('INXDU', 'S&P 500 daily up/down', 'Financials'),
        ('INXM', 'S&P 500 monthly', 'Financials'),
        #
        # sports
        ('KXNFLSPREAD', 'NFL Football Game, Point Spread', 'Sports'),
        ('KXNFLTOTAL', 'NFL Football Game, Point Total', 'Sports'),
        ('KXNFLANYTD', 'NFL Football Game', 'Sports'),
        ('KXNCAAFSPREAD', 'NCAA Football Game', 'Sports'),
        ('KXNCAAFTOTAL', 'NCAA Football Game, Point Total', 'Sports'),
        ('KXNFLWINS', 'NFL Football Game, Who wins?', 'Sports'),
        ('KXNFLFIRSTTD', 'NFL Football Game, First Touchdown', 'Sports'),
        ('KXNFL2TD', 'NFL Football Game, 2 or more touchdowns', 'Sports'),
        #
        # politics
        ('KXPENNWIN', 'Pennsylvania win', 'Politics'),
        ('KXMAYORSF', 'San Francisco Mayor', 'Politics'),
        ('KXECADVANTAGE', 'Electoral College advantage', 'Politics'),
        ('KXLASTSTATECALL24', 'Last state called in 2024', 'Politics'),
        ('KXELECTION24RCP', 'Election 24 RCP', 'Politics'),
        ('KXELECTION24538', 'Election 24 538', 'Politics'),
        ('KXDJTPAWIN', 'Trump winning PA and the Presidency', 'Politics'),
        (
            'KXKHBLUEWALL',
            'Harris wins but loses any Blue Wall state',
            'Politics',
        ),
        (
            'KXDJTBLUEWALL',
            'Trump wins but loses any Blue Wall state',
            'Politics',
        ),
        ('KXKHMI', 'Harris wins but loses Michigan', 'Politics'),
        ('KXELECTIONPACALL', 'PA call', 'Politics'),
        ('KXELECTIONMICALL', 'MI call', 'Politics'),
        ('KXELECTIONGACALL', 'GA call', 'Politics'),
        ('KXEXITPOLLLMEN', 'Latino men 2024', 'Politics'),
        ('KXEXITPOLLMEN', 'Men in 2024', 'Politics'),
        ('KXEXITPOLLWOMEN', 'Women in 2024', 'Politics'),
        ('KXKHUNMWOMEN', 'Unmarried women 2024', 'Politics'),
        ('KXKHCGRADS', 'College graduates in 2024', 'Politics'),
        ('KXDJTMEN', 'Men in 2024', 'Politics'),
        ('KXDJTASIAN', 'Asians in 2024', 'Politics'),
        ('KXPAWINPOPVOTE', 'PA win popular vote nationally', 'Politics'),
        ('KXECPOPVOTE', 'EC/Pop Vote 2024', 'Politics'),
        ('KX3RDPARTY', '3rd Party 2% of vote', 'Politics'),
        ('KXRFKSHARE', 'RFK vote share', 'Politics'),
        ('KXDJTLGBT', 'LGBT voters 2024', 'Politics'),
        ('KXEXITPOLLLATE', 'Late deciders', 'Politics'),
        ('KXEXITPOLLWWOMEN', 'White women 2024', 'Politics'),
        ('KXDJTLATINO', 'Latinos 2024', 'Politics'),
        ('KXDJTNOGRAD', 'Non-college graduates 2024', 'Politics'),
        ('KXKHWOMEN', 'Women in 2024', 'Politics'),
        ('KX538CALL', '538 call 2024', 'Politics'),
        ('KXSILVERCALL', 'Silver call 2024', 'Politics'),
        ('KXOHDISTRICTS', 'Ohio redistricting referendum', 'Politics'),
    ]
    return pl.DataFrame(
        manual_series_metadata,
        schema=['series_ticker', 'series_title', 'category'],
        orient='row',
    )


def _refactor_raw_categories(metrics: pl.DataFrame) -> pl.DataFrame:
    rename_category = {
        'Entertainment': 'Culture',
        'Science and Technology': 'STEM',
    }

    merge_category = {
        'Companies': 'Financials',
        'Elections': 'Politics',
        'Mentions': 'Politics',
    }

    merge_as_subcategory = {
        'Social': 'Culture',
        'Health': 'STEM',
        'Climate and Weather': 'STEM',
        'Transportation': 'STEM',
        'Education': 'STEM',
    }

    return (
        metrics.with_columns(pl.col.category.replace(rename_category))
        .with_columns(pl.col.category.replace(merge_category))
        .with_columns(
            subcategory=pl.when(
                pl.col.category.is_in(merge_as_subcategory.keys())
            )
            .then('category')
            .otherwise(None)
        )
        .with_columns(pl.col.category.replace(merge_as_subcategory))
    )


def _get_uncategorized_kalshi_volume(df: pl.DataFrame) -> pl.DataFrame:
    return (
        df.filter(series_ticker='Unknown')
        .group_by('report_ticker')
        .agg(pl.sum('daily_volume'))
        .sort('daily_volume', descending=True)
    )
