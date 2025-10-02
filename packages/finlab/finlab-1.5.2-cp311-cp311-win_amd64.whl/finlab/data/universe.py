import re
import pandas as pd

# Shared universe state used to filter datasets
universe_stocks = set()


class universe():
    def __init__(self, market='ALL', category='ALL'):
        self._market = market
        self._category = category
        self._previous_stocks = set()

    def __enter__(self):
        global universe_stocks
        self._previous_stocks = universe_stocks
        set_universe(self._market, self._category)
        return self

    def __exit__(self, type, value, traceback):
        global universe_stocks
        universe_stocks = self._previous_stocks


def set_universe(market: str = 'ALL', category='ALL'):
    from . import data as data_module

    categories = data_module.get('security_categories').reset_index().set_index('stock_id')

    market_match = pd.Series(True, categories.index)

    if 'TSE' in market and 'OTC' in market:
        market = 'TSE_OTC'

    if market == 'ALL':
        pass
    elif market == 'TSE':
        market_match = categories.market == 'sii'
    elif market == 'OTC':
        market_match = categories.market == 'otc'
    elif market == 'TSE_OTC':
        market_match = (categories.market == 'sii') | (categories.market == 'otc')
    elif market == 'ETF':
        market_match = categories.market == 'etf'
    elif market == 'STOCK_FUTURE':
        market_match = data_module.get('single_stock_futures_and_equity_options_underlying')\
            .pipe(lambda df: df[df['是否為股票期貨標的'] == 'Y'])\
            .pipe(lambda df: pd.Series(True, set(df.stock_id)).reindex(categories.index).fillna(False))

    category_match = pd.Series(True, categories.index)

    if category == 'ALL':
        pass
    else:
        if isinstance(category, str):
            category = [category]

        matched_categories = set()
        all_categories = set(categories.category)
        for ca in category:
            matched_categories |= set([c for c in all_categories if isinstance(c, str) and re.search(ca, c)])
        category_match = categories.category.isin(matched_categories)

    global universe_stocks
    universe_stocks = set(categories.index[market_match & category_match])


class us_universe:
    def __init__(self, market='ALL', sector='ALL', industry='ALL', exchange='ALL'):
        self._market = market
        self._sector = sector
        self._industry = industry
        self._exchange = exchange
        self._previous_stocks = set()

    def __enter__(self):
        global universe_stocks
        self._previous_stocks = universe_stocks
        set_us_universe(self._market, self._sector, self._industry, self._exchange)
        return self

    def __exit__(self, type, value, traceback):
        global universe_stocks
        universe_stocks = self._previous_stocks


def set_us_universe(market: str = 'ALL', sector='ALL', industry='All', exchange='ALL'):
    from . import data as data_module

    categories = data_module.get('us_tickers').reset_index().set_index('stock_id')
    market_range = [
        'ADR Common Stock',
        'ADR Common Stock Primary Class',
        'ADR Common Stock Secondary Class',
        'ADR Preferred Stock',
        'Domestic Common Stock',
        'Domestic Common Stock Primary Class',
        'Domestic Common Stock Secondary Class',
        'Domestic Preferred Stock',
    ]

    if market == 'ALL':
        market_match = categories.category.isin(market_range)
    else:
        market_match = categories.category.isin([m for m in market_range if market in m])

    def match_ids(column, item):
        category_match = pd.Series(True, categories.index)
        if item == 'ALL':
            pass
        else:
            if isinstance(item, str):
                item = [item]
            matched_categories = set()
            all_categories = set(categories[column])
            for ca in item:
                matched_categories |= set([c for c in all_categories if isinstance(c, str) and re.search(ca, c)])
            category_match = categories[column].isin(matched_categories)
        return category_match

    sector_match = match_ids('sector', sector)
    industry_match = match_ids('industry', industry)

    exchange_match = pd.Series(True, categories.index)
    if exchange == 'ALL':
        pass
    else:
        if isinstance(exchange, str):
            exchange = [exchange]
        exchange_match = categories.exchange.isin(exchange)

    global universe_stocks
    universe_stocks = set(categories.index[market_match & sector_match & industry_match & exchange_match])


not_available_universe_stocks = [
    'benchmark_return', 'institutional_investors_trading_all_market_summary',
    'margin_balance', 'intraday_trading_stat',
    'stock_index_price', 'stock_index_vol',
    'taiex_total_index', 'broker_info',
    'rotc_monthly_revenue', 'rotc_price',
    'world_index', 'rotc_broker_trade_record',
    'security_categories', 'finlab_tw_stock_market_ind',
    'tw_industry_pmi', 'tw_industry_nmi',
    'tw_total_pmi', 'tw_total_nmi',
    'tw_business_indicators', 'tw_business_indicators_details',
    'tw_monetary_aggregates', 'us_unemployment_rate_seasonally_adjusted',
    'us_tickers',
]


def refine_stock_id(dataset, ret):
    from .data import process_data  # lazy import to avoid circular dependency

    ret = process_data(dataset, ret)

    if dataset in not_available_universe_stocks:
        return ret

    if not universe_stocks:
        return ret

    if ':' in dataset:
        subset_stocks = ret.columns.intersection(universe_stocks)
        if subset_stocks.any():
            return ret.loc[:, subset_stocks]

    if 'stock_id' in ret.columns:
        subset_stocks = ret['stock_id'].isin(universe_stocks)
        if subset_stocks.any():
            return ret.loc[subset_stocks]

    return ret



