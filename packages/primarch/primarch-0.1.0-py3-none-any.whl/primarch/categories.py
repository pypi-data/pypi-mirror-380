from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    import polars as pl


subcategory_triggers = {
    'Sports': {
        'Football': [
            '(?i)football',
            'NFL',
            'Super Bowl',
            'Heisman Trophy',
            'NCAAF',
            'AFC',
            'NFC',
            'Big 12',
            'SEC Champion',
            'ACC Champion',
            'Big Ten Champion',
            'SB mention',
            'UFL',
        ],
        'Soccer': [
            '(?i)soccer',
            'MLS',
            'English Premier League Game',
            'UEFA',
            'Club World Club Game',
            '(?i)La Liga',
            '(?i)Premier League',
            'Ligue 1',
            'Serie A',
            '(?i)Bundesliga',
            'Club World Cup',
            "Ballon d'Or",
            'EPL top 4 teams',
            "Men's World Cup",
            'FA cup',
            'Champions League',
            'Europa Leauge',
            'PFA Player of The Year',
            'Club World Club Group',
            'Europa League',
            'Ronaldo',
            'Real Madrid',
        ],
        'Baseball': [
            '(?i)baseball',
            'MLB',
            'World Series',
            'American League East',
            'American League West',
            'American League Central',
            'National League Central',
            'National League East',
            'National League West',
        ],
        'Basketball': [
            '(?i)basketball',
            'NBA',
            r'March Tournament \(M\)',
            r'March Tournament \(W\)',
            'LBJ retire',
            'NIT Champion',
        ],
        'Tennis': [
            'Tennis',
            '(?i)WIMBLEDON',
            'French Open',
            'ATP',
            'WTA',
            'Indian Wells Open',
            'Movistar Chile Open',
            'Rio Open',
            'Laver Cup',
            'Qatar ExxonMobil Open',
            'Djokovic',
        ],
        'Golf': [
            'PGA',
            'US Open',
            'Masters Tournament',
            'The Open Championship',
            'Ryder Cup',
            'Genesis Invitational',
            'LIV Tour',
            'Phoenix Open',
            'Masters Cut',
        ],
        'Martial Arts': ['UFC', 'Boxing'],
        'Hockey': ['Hockey', 'Stanley Cup', 'Conn Smythe'],
        'Automotive': [
            'F1 Race',
            'NASCAR',
            'Indy 500',
            'Formula 1',
            'Verstappen',
        ],
        'Eating': ["(?i)Nathan's Hot Dog"],
        'Chess': ['Chess', 'FIDE'],
        'Cricket': ['Asia Cup Winner', 'IPL Final'],
        'Pickleball': ['pickleball'],
        'Esports': [
            '2025 Mid-Season Invitational',
            'Dota 2',
            'Esports',
            'League of Legends',
        ],
        'Cycling': ['Tour de France'],
        'Running': ['4-Minute Mile'],
        'Frisbee': ['Frisbee'],
    },
    'Culture': {
        'Music': [
            'Spotify',
            'Grammy',
            'Billboard',
            'Eurovision',
            'Album record',
            'pop singer',
            'Top artist',
            'New albums',
            'Artist of the Year',
            'Top songs',
            'Will Taylor Swift release a',
            'Taylor Swift album',
            '(?i)Cardi B',
            'Kendrick Lamar',
            'Justin Bieber',
            'Billie Eilish',
            'CHARLI XCX',
            '(?i)Sabrina Carpenter',
            'Kanye',
            '(?i)Taylor Swift',
            '(?i)Album',
            '(?i)song',
            '(?i)many straight weeks',
            '(?i)doja cat',
            'Top New Artist',
            'Will any new height video receive 100 million views in 7 days',
            'Who will be featured on the life of a show girl',
            'Donda',
            'listen',
            'ACMA',
        ],
        'Trump': ['Trump'],
        'Movies': [
            '(?i)Rotten tomatoes',
            'Oscar',
            'RT',
            'SAG',
            'Netflix movie ranking',
            '(?i)film',
            'Critics Choice Award',
            "Palme d'Or",
            'Ghostbusters',
            'BAFTA',
            'Next Bond actor',
            'Golden Globe for Best Actor in a Drama',
            'Golden Globe for Best Director',
        ],
        'TV': [
            '(?i)Emmy',
            'Netflix TV rank',
            'White Lotus',
            'Jimmy Kimmel release',
            'TV',
            'Anime',
            '(?i)Season',
        ],
        'Video Games': ['Game Awards', 'GTA ', 'Clair Obscur', 'PS6'],
        'Person of the Year': ['Person of the Year'],
        'Podcast': [
            'Rogan',
            'JRE',
            'how many views will taylor swift get on video',
            'Lex Fridman',
            'podcast',
        ],
        'Sports': [
            '(?i)Super Bowl',
            ' BEST TEAM‬$',
            'March Madness',
            'NBA',
            'MLB',
            'head coach',
            'Bronny James',
        ],
        'Apps': ['Free app ranking'],
        'Internet': ['Mr. Beast'],
        'Biden': ['(?i)Biden'],
        'Strike': [
            'Writers strike ends',
            'Actors strike ends',
        ],
        'Relationship': ['Swift Kelce'],
        'Martial Arts': ['UFC', 'Hulk Hogan'],
        'Musical': ['Best Play', 'Best Musical', 'in a Musical'],
    },
    'STEM': {
        'AI': [
            'ChatGPT',
            '(?i)LLM',
            '^Top model$',
            'Unsupervised full self-driving',
            'AGI',
            'Top-ranked AI',
            'IMO AI',
            'OpenAI',
            'AI coding',
            '^Open-source model$',
            'Claude 4 release',
            'Deepseek',
            'AI ',
            'SWE bench',
            'Model hitting thresholds$',
            'GPT',
            '(?i)Grok',
        ],
        'Transportation': ['TSA check-ins this week', 'Waymo'],
        'Space': [
            'Aliens',
            'Starship',
            'NASA',
            'Webb Telescope launch',
            'Exoplanet',
            'Geomagnetic Storm',
            'SpaceX',
            'Major meteor strike',
            'Asteroid',
            'astronaut',
            'Moon',
        ],
        'Health': ['Ozempic', 'Omicron vaccine', 'cancer'],
    },
    'Financials': {
        'Nasdaq': ['(?i)Nasdaq'],
        'S&P': ['S&P', 'SPX', 'SPY', 'SP500'],
        'Tesla': ['(?i)tesla', 'Robotaxi'],
        'Forex': ['USD/JPY', 'EUR/USD', 'EURO/USD', 'Pound/US Dollar'],
        'Earnings mention': [
            '(?i)earnings mention',
            'earnings m$',
            'earnings menti$',
            r'earnings call\?$',
        ],
        'SpaceX': ['SpaceX'],
        'TikTok': ['(?i)TikTok'],
        'Treasury': ['Treasury'],
        'OpenAI': ['(?i)OpenAI'],
        'Coinbase': ['Coinbase'],
        'Nintendo': ['Nintendo'],
        'Commodities': ['WTI oil'],
        'IPO': ['IPOs'],
    },
    'Crypto': {
        'Bitcoin': ['(?i)Bitcoin', 'BTC'],
        'Ethereum': ['(?i)Ethereum', 'ETH'],
        'Solana': ['(?i)Solana', 'SOL'],
        'Doge': ['(?i)Doge'],
        'Shiba': ['(?i)Shiba'],
        'BCH': ['BCH'],
        'XRP': ['XRP'],
        'Avalanche': ['Avalanche'],
        'XLM': ['XLM'],
        'LTC': ['LTC'],
        'Chainlink': ['Chainlink'],
        'Polkadot': ['Polkadot'],
        'Stablecoins': ['USDC', 'USDT', 'UDST', '(?i)stablecoin'],
        'General': [
            'Crypto being positive',
            'New coin launch',
            'Crypto reserve assets',
            'Crypto performance',
            'Next coin in RH',
            'New coin chain',
        ],
    },
    'Economics': {
        'Inflation': ['(?i)inflation', 'CPI'],
        'IPO': ['IPO'],
        'Interest Rates': [
            'Fed ',
            'rate cuts',
            'Large cuts',
            'Rate cut',
            'Zero rates',
        ],
        'Commodities': [
            '(?i)Gas',
            'Oil',
            '(?i)Semiconductor',
            'prices',
            'Price of',
            'Costco hot dog price increase',
            'ISM PMI',
            'Diesel price',
            'SPR use',
            'Used Vehicle Value Index',
        ],
        'Real Estate': [
            '(?i)real estate',
            'home sales',
            'house average sale',
            'Mortgage',
            'Rent',
            'US housing price up monthly',
            'yearly rent growth',
            'NYC rent yearly increase',
        ],
        'Strike': ['strike'],
        'Wealth': [
            'First trillionaire',
            'Musk wealth',
            'Musk trillionaire',
            'Top 3 wealthiest people',
            'Wealthiest person in world',
            'Half-trillionaire',
            'Person wealthiest',
        ],
        'Forex': ['exchange rate'],
        'Trade': [
            '(?i)tariff',
            'Export tariffs',
            'trade deficit',
            'Suez traffic',
            'U.S. BOP',
        ],
        'Employment': [
            'Jobs numbers',
            '(?i)Unemployment',
            'Weekly initial jobless claims',
            'Initial jobless claims',
            'ADP employment change',
            'layoffs',
            'Employment-population ratio',
            'Job revisions',
        ],
        'GDP': ['GDP', '(?i)recession'],
        'Debt': ['debt', 'Trillion dollar coin minted'],
        'Insolvency': ['bankrupt', 'card defaults'],
    },
}


def _get_subcategory_series() -> dict[str, list[str]]:
    return {
        'Basketball': [
            'KXNBAFINALSMVP',
            'KXNEXTTEAMGIANNIS',
            'KXMANTISFREETHROWS',
            'KXNYKCOACH',
            'KXNEXTTEAMLEBRON',
        ],
        'Hockey': ['KXNHLEAST', 'KXNHLWEST', 'KXNHL4NATIONS'],
        'Baseball': [
            'KXMLBNLCPOTY',
        ],
        'Soccer': ['KXUCLROUND'],
        'Football': [
            'KXNEWCOACHNO',
            'KXNEWCOACHDAL',
            'KXNEWCOACHCHIBEARS',
            'KXNEXTTEAMMICAH',
            'KXNEWCOACHNYJ',
            'KXNEWCOACHLV',
            'KXNEWCOACHJAX',
            'KXTUSHPUSH',
            'KXFFQBALLENMAHOMES',
            'KXSTARTCLEBROWNS',
            'KXSTARTIND',
            'KXSTARTNOSAINTS',
            'KXNEWCOACHNE',
            'KXNEXTTEAMMCLAURIN',
        ],
        'Golf': ['KXFIRSTUSOPEN'],
        'Esports': [
            'KXFANATICSGAMESFIRSTPLACE',
            'KXINTERNETINVITATIONAL',
            'KXVCCHAMPIONSPARIS',
        ],
    }


def _get_recategorize_series() -> dict[str, tuple[str, typing.Optional[str]]]:
    return {
        'KXREVSOL': ('Crypto', 'SOL'),
        'KXWTAX': ('Politics', None),
        'KXRAINNOSB': ('STEM', 'Climate and Weather'),
        'KXRAINNY': ('STEM', 'Climate and Weather'),
        'KXHIGHNY0': ('STEM', 'Climate and Weather'),
        'KXNEXTPOPE': ('Culture', 'Religion'),
        'KXNEWPOPEDATE': ('Culture', 'Religion'),
        'KXNEWPOPEROUNDS': ('Culture', 'Religion'),
        'KXNEWPOPECONTINENT': ('Culture', 'Religion'),
        'KXNEWPOPENAME': ('Culture', 'Religion'),
        'KXPOPEVISITNEXT': ('Culture', 'Religion'),
        'KXNEWPOPE': ('Culture', 'Religion'),
        'KXNEWPOPECOUNTRY': ('Culture', 'Religion'),
        'KXRECSS': ('Economics', 'Recession'),
        'KXUSADEALCOUNT': ('Economics', 'Trade'),
        'KXFOOTBALL1001': ('Sports', 'Football'),
        'KXNYCBOROUGHWINBRON': ('Politics', 'NYC Mayor'),
        'KXNYCBOROUGHWINMAN': ('Politics', 'NYC Mayor'),
        'KXHAPPIER': ('Culture', 'Music'),
        'KXFERTILITYSK': ('Economics', 'Demographics'),
        'KXPRCBIRTHS': ('Economics', 'Demographics'),
        'KXCASE7DCN': ('STEM', 'Health'),
        'KXTRUMPVISITSTATES': ('Culture', 'Trump'),
        'KXMONKEYPOX': ('STEM', 'Health'),
        'KXMAERSK': ('Economics', 'Trade'),
        'KXGDPCN': ('Economics', 'GDP'),
        'KXDINENYC': ('STEM', 'Health'),
        'KXARGCENTRALBANK': ('Economics', 'Insolvency'),
        'KXARGDOLLAR': ('Economics', None),
        'KXNYCBOROUGHWINQUEE': ('Politics', 'NYC Mayor'),
        'KXNYCBOROUGHWINBROOK': ('Politics', 'NYC Mayor'),
        'KXMAMDANIBOROUGHS': ('Politics', 'NYC Mayor'),
        'KXSLOAN': ('Economics', 'Debt'),
        'KXSHAKEDURATIONDJTPUTIN': ('Culture', 'Trump'),
        'KXPAHLAVIVISITA': ('Politics', 'Iran'),
        'KXINTERSTELLAR': ('STEM', 'Space'),
        'KXDEBATEMAMDANICUOMO': ('Politics', 'NYC Mayor'),
        'KXSEAICE': ('STEM', 'Climate and Weather'),
        'KXPMLA': ('STEM', 'Climate and Weather'),
        'KXOLYMCANCEL': ('STEM', 'Health'),
        'KXSUEZ': ('Economics', 'Trade'),
        'KXNYCBOROUGHWINSTAT': ('Politics', 'NYC Mayor'),
        'KXINDEXADD': ('Financials', 'S&P 500'),
    }


def populate_subcategories(data: pl.DataFrame) -> pl.DataFrame:
    import polars as pl

    original_data = data
    columns = [
        'series_ticker',
        'contract_ticker',
        'series_title',
        'category',
        'subcategory',
    ]
    data = data.unique(columns).select(columns)

    # trigger keywords
    for category in subcategory_triggers.keys():
        partitions = data.with_columns(
            subcategory_is_null=pl.col.category == category
        ).partition_by('subcategory_is_null', as_dict=True)

        subcategory: str | None
        category_data = partitions[(True,)]
        when_replace: typing.Any = pl.when(False).then(None)
        for subcategory, keywords in subcategory_triggers[category].items():
            filter = (
                pl.col.category == category
            ) & pl.col.series_title.str.contains(keywords[0])
            for keyword in keywords[1:]:
                filter = filter | (
                    (pl.col.category == category)
                    & pl.col.series_title.str.contains(keyword)
                )
            when_replace = when_replace.when(filter).then(pl.lit(subcategory))
        category_data = category_data.with_columns(
            subcategory=when_replace.otherwise('subcategory')
        )
        data = (
            partitions[(False,)]
            .vstack(category_data)
            .drop('subcategory_is_null')
        )

    # direct replacements by subcategory
    when_replace = pl.when(False).then(None)
    subcategory_series = _get_subcategory_series()
    recategorize_series = _get_recategorize_series()
    for series_ticker, (category, subcategory) in recategorize_series.items():
        if subcategory is not None:
            if subcategory not in subcategory_series:
                subcategory_series[subcategory] = []
            subcategory_series[subcategory].append(series_ticker)
    for subcategory, keywords in subcategory_series.items():
        filter = pl.col.series_ticker == keywords[0]
        for keyword in keywords[1:]:
            filter = filter | (pl.col.series_ticker == keyword)
        when_replace = when_replace.when(filter).then(pl.lit(subcategory))
    data = data.with_columns(subcategory=when_replace.otherwise('subcategory'))

    # direct replacements by category
    category_series: dict[str, list[str]] = {}
    for series_ticker, (category, subcategory) in recategorize_series.items():
        category_series.setdefault(category, []).append(series_ticker)
    when_replace = pl
    for subcategory, keywords in category_series.items():
        filter = pl.col.series_ticker == keywords[0]
        for keyword in keywords[1:]:
            filter = filter | (pl.col.series_ticker == keyword)
        when_replace = when_replace.when(filter).then(pl.lit(subcategory))
    data = data.with_columns(category=when_replace.otherwise('category'))

    return original_data.drop('category', 'subcategory').join(
        data.sort('contract_ticker').select(
            'contract_ticker', 'category', 'subcategory'
        ),
        on='contract_ticker',
        how='left',
    )
