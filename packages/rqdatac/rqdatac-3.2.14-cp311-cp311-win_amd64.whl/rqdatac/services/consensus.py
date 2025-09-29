# -*- coding: utf-8 -*-
import datetime
import warnings
from collections import defaultdict

import pandas as pd
import numpy as np
from rqdatac.utils import today_int

from rqdatac.validators import (
    ensure_list_of_string,
    ensure_order_book_ids,
    check_items_in_container,
    ensure_date_range,
    ensure_date_int,
    ensure_string_in,
)

from rqdatac.client import get_client
from rqdatac.decorators import export_as_api, ttl_cache, deprecated


CONSENSUS_INDICATOR_FIELDS = [
    'net_profit_t',
    'net_profit_t1',
    'net_profit_t2',
    'revenue_t',
    'revenue_t1',
    'revenue_t2',
    'net_asset_t',
    'net_asset_t1',
    'net_asset_t2',
    'cash_from_operating_activities_t',
    'cash_from_operating_activities_t1',
    'cash_from_operating_activities_t2',
    'profit_from_operation_t',
    'profit_from_operation_t1',
    'profit_from_operation_t2',
    'cost_of_goods_sold_t',
    'cost_of_goods_sold_t1',
    'cost_of_goods_sold_t2',
    'profit_before_tax_t',
    'profit_before_tax_t1',
    'profit_before_tax_t2',
    'ebit_t',
    'ebit_t1',
    'ebit_t2',
    'operating_revenue_per_share_t',
    'operating_revenue_per_share_t1',
    'operating_revenue_per_share_t2',
    'eps_t',
    'eps_t1',
    'eps_t2',
    'bps_t',
    'bps_t1',
    'bps_t2',
    'share_cap_chg_date',
    'report_main_id',
    'grade_coef',
    'targ_price',
    'ebitda_t',
    'ebitda_t1',
    'ebitda_t2',
    'profit_res_t',
    'profit_res_t1',
    'profit_res_t2',
    'operate_cash_flow_per_share_t',
    'operate_cash_flow_per_share_t1',
    'operate_cash_flow_per_share_t2',
    'profit_chg_t',
    'profit_chg_t1',
    'profit_chg_t2',
    'grade_chg_t',
    'grade_chg_t1',
    'grade_chg_t2',
    'targ_price_chg_t',
    'targ_price_chg_t1',
    'targ_price_chg_t2',
    'chg_reason_t',
    'chg_reason_t1',
    'chg_reason_t2',
    'create_time',
    'summary',
]

NON_NUMERIC_FIELDS = [
    'share_cap_chg_date',
    'report_main_id',
    'chg_reason_t',
    'chg_reason_t1',
    'chg_reason_t2',
    'create_time',
    'summary',
]


DTYPES = {k: '<f8' for k in CONSENSUS_INDICATOR_FIELDS if k not in NON_NUMERIC_FIELDS}
DTYPES['fiscal_year'] = '<u4'
DTYPES['data_source'] = '<f2'


CONSENSUS_PRICE_FIELDS = [
    'half_year_target_price',
    'one_year_target_price',
    'quarter_recommendation',
    'half_year_recommendation',
    'one_year_recommendation',
]

CONSENSUS_PRICE_FIELDS_MAP = {
    'half_year_target_price': ('price_raw', 'price_prd', 'M06'),
    'one_year_target_price': ('price_raw', 'price_prd', 'Y01'),
    'quarter_recommendation': ('grd_coef', 'grd_prd', '1'),
    'half_year_recommendation': ('grd_coef', 'grd_prd', '2'),
    'one_year_recommendation': ('grd_coef', 'grd_prd', '3'),
}

PRICE_DTYPES = {
    'half_year_target_price': '<f8',
    'one_year_target_price': '<f8',
    'quarter_recommendation': '<f8',
    'half_year_recommendation': '<f8',
    'one_year_recommendation': '<f8',
    'price_raw': '<f8',
}


@export_as_api(namespace='consensus')
def get_indicator(order_book_ids, fiscal_year, fields=None, start_date=None, end_date=None, date_rule=None, market='cn'):
    """
    获取一致预期数据

    :param order_book_ids: 股票名称
    :param fiscal_year: int/str, 查询年份
    :param fields: list,  一致预期字段
    :param start_date: date-like object, 开始日期, 默认为None
    :param end_date: date-like object, 结束日期, 默认为None
    :param date_rule: str 日期截取规则，和start_date/end_date一起使用，默认为None不生效
        'rpt_dt'，根据研报发布日期RPT_DT截取返回的数据
        'create_tm',根据今日投资入库时间截取返回的数据
        'rice_create_tm',根据米筐入库时间截取返回的数据
    :param market: (Default value = 'cn')
    :returns: pandas  MultiIndex DataFrame
    """
    order_book_ids = ensure_order_book_ids(order_book_ids, market=market)
    if fields is None:
        fields = CONSENSUS_INDICATOR_FIELDS
    else:
        fields = ensure_list_of_string(fields, 'consensus_indicator')
        check_items_in_container(fields, CONSENSUS_INDICATOR_FIELDS, 'consensus_indicator')

    if start_date is not None:
        start_date = ensure_date_int(start_date)
    if end_date is not None:
        end_date = ensure_date_int(end_date)
    if date_rule is not None:
        ensure_string_in(date_rule, ('rpt_dt', 'create_tm', 'rice_create_tm'), 'date_rule')
    elif start_date is not None or end_date is not None:
        raise ValueError('Ambiguous: date_rule should be specific!')
    if fiscal_year is not None:
        fiscal_year = int(fiscal_year)
    elif start_date is None and end_date is None:
        raise ValueError('at least one of (start_date/end_date, fiscal_year) should be non-none value.')

    data = get_client().execute('consensus.get_indicator_v2', order_book_ids, fiscal_year, fields, start_date, end_date, date_rule, market=market)
    if not data:
        return None
    df = pd.DataFrame(data)
    df.set_index(['order_book_id', 'date'], inplace=True)
    df.sort_index(inplace=True)
    dtypes = {f: DTYPES[f] for f in df.columns if f in DTYPES}
    df = df.astype(dtypes)
    return df


@export_as_api(namespace='consensus')
def get_price(order_book_ids, start_date=None, end_date=None, fields=None, adjust_type='none', market='cn'):
    """
    获取一致预期股价预测数据

    :param order_book_ids: 股票名称
    :param start_date: 开始日期， date-like object, 默认三月前那天
    :param end_date: 结束日期， date-like object， 默认当天
    :param fields: list,  一致预期字段
    :param adjust_type: 可选参数,默认为‘none', 返回原始数据
            'pre' 返回前复权数据
            'post' 返回后复权数据
    :param market: (Default value = 'cn')
    :returns: pandas MultiIndex DataFrame
    """
    order_book_ids = ensure_order_book_ids(order_book_ids, market=market)

    if fields is None:
        fields = CONSENSUS_PRICE_FIELDS
    else:
        fields = ensure_list_of_string(fields, 'consensus_price')
        check_items_in_container(fields, CONSENSUS_PRICE_FIELDS, 'consensus_price')

    start_date, end_date = ensure_date_range(start_date, end_date)

    data = get_client().execute('consensus.get_price', order_book_ids, start_date, end_date, market=market)
    if not data:
        return None

    records = defaultdict(dict)
    for r in data:
        key = (r['order_book_id'], r['institute'], r['date'])
        if key not in records:
            records[key].update(r)
        for field in fields:
            name, f, value = CONSENSUS_PRICE_FIELDS_MAP[field]
            if r[f] == value:
                records[key][field] = r[name]
    df = pd.DataFrame(list(records.values()))
    df.set_index(['order_book_id', 'date'], inplace=True)
    df.sort_index(inplace=True)
    for f in fields:
        if f not in df.columns:
            df[f] = None
    df = df.astype({f: PRICE_DTYPES[f] for f in fields if f in PRICE_DTYPES})

    if adjust_type != 'none':
        adjust_fields = list(set(CONSENSUS_PRICE_FIELDS[:2]) & set(fields))
        if not adjust_fields:
            return df

        from rqdatac.services.detail.adjust_price import get_ex_factor_for
        ex_factors = get_ex_factor_for(order_book_ids, market)
        pre = adjust_type == 'pre'

        def adjust(sub):
            factors = ex_factors.get(sub.name)
            if factors is None:
                return sub
            factor = np.take(factors.values, factors.index.searchsorted(sub.index.get_level_values(1), side='right') - 1)
            if pre:
                factor /= factors.iloc[-1]

            sub[adjust_fields] = (sub[adjust_fields].values.T * factor).T
            return sub

        df = df.groupby(level=0).apply(adjust)
        df[adjust_fields] = np.round(df[adjust_fields], 4)

    return df


CONSENSUS_COMP_INDICATOR_FIELDS = [
    'comp_operating_revenue_t',
    'comp_con_operating_revenue_t1',
    'comp_con_operating_revenue_t2',
    'comp_con_operating_revenue_t3',
    'comp_con_operating_revenue_ftm',
    'comp_net_profit_t',
    'comp_con_net_profit_t1',
    'comp_con_net_profit_t2',
    'comp_con_net_profit_t3',
    'comp_con_net_profit_ftm',
    'comp_eps_t',
    'comp_con_eps_t1',
    'comp_con_eps_t2',
    'comp_con_eps_t3',
    'comp_net_asset_t',
    'comp_con_net_asset_t1',
    'comp_con_net_asset_t2',
    'comp_con_net_asset_t3',
    'comp_con_net_asset_ftm',
    'comp_cash_flow_t',
    'comp_con_cash_flow_t1',
    'comp_con_cash_flow_t2',
    'comp_con_cash_flow_t3',
    'comp_con_cash_flow_ftm',
    'comp_roe_t',
    'comp_con_roe_t1',
    'comp_con_roe_t2',
    'comp_con_roe_t3',
    'comp_con_roe_ftm',
    'comp_pe_t',
    'comp_con_pe_t1',
    'comp_con_pe_t2',
    'comp_con_pe_t3',
    'comp_con_pe_ftm',
    'comp_ps_t',
    'comp_con_ps_t1',
    'comp_con_ps_t2',
    'comp_con_ps_t3',
    'comp_con_ps_ftm',
    'comp_pb_t',
    'comp_con_pb_t1',
    'comp_con_pb_t2',
    'comp_con_pb_t3',
    'comp_con_pb_ftm',
    'comp_peg',
    'comp_operating_revenue_growth_ratio_t',
    'comp_con_operating_revenue_growth_ratio_t1',
    'comp_con_operating_revenue_growth_ratio_t2',
    'comp_con_operating_revenue_growth_ratio_t3',
    'comp_con_operating_revenue_growth_ratio_ftm',
    'comp_net_profit_growth_ratio_t',
    'comp_con_net_profit_growth_ratio_t1',
    'comp_con_net_profit_growth_ratio_t2',
    'comp_con_net_profit_growth_ratio_t3',
    'comp_con_net_profit_growth_ratio_ftm',
    'con_grd_coef',
    'con_targ_price',
    'comp_con_eps_ftm',
    'ty_profit_t1',
    'ty_profit_t2',
    'ty_profit_t3',
    'ty_profit_ftm',
    'ty_eps_t1',
    'ty_eps_t2',
    'ty_eps_t3',
    'ty_eps_ftm',
]

CONSENSUS_COMP_INDICATOR_FIELDS_V = [
    'comp_con_net_profit_t1',
    'comp_con_net_profit_t2',
    'comp_con_net_profit_t3',
    'comp_con_operating_revenue_t1',
    'comp_con_operating_revenue_t2',
    'comp_con_operating_revenue_t3',
    'comp_con_cash_flow_t1',
    'comp_con_cash_flow_t2',
    'comp_con_cash_flow_t3',
    'comp_con_eps_t1',
    'comp_con_eps_t2',
    'comp_con_eps_t3',
    'comp_con_eps_ftm',
]

CONSENSUS_COMP_INDICATORS_FIELDS_GRD_HIST = ['con_targ_price']

COMP_INDICATORS_DTYPES = {
    field: '<f8' for field in
    CONSENSUS_COMP_INDICATOR_FIELDS + CONSENSUS_COMP_INDICATOR_FIELDS_V + CONSENSUS_COMP_INDICATORS_FIELDS_GRD_HIST
}


@export_as_api(namespace='consensus')
def get_comp_indicators(order_book_ids, start_date=None, end_date=None, fields=None, report_range=0, market='cn'):
    """
    获取个股一致预期表

    :param order_book_ids: 股票名称
    :param start_date: date-like object, 默认当日
    :param end_date: date-like object, 默认为当日
    :param fields: list,  一致预期字段
    :param report_range: int, 研报范围
        0-不考虑补录入&包括所有报告数据（历史值修复会存在数值变动，需要不变的话传入3）
        1-考虑补录入&包括所有报告数据
        2-考虑补录入&仅包括公司报告数据
        3-不考虑补录入&包括所有报告数据
        4-不考虑补录入&仅包括公司报告数据
    :param market: (Default value = 'cn')

    :returns: pandas MultiIndex DataFrame
    """
    order_book_ids = ensure_order_book_ids(order_book_ids, market=market)
    today = today_int()
    start_date = ensure_date_int(start_date) if start_date else today
    end_date = ensure_date_int(end_date) if end_date else today

    assert report_range in (0, 1, 2, 3, 4), 'invalid report_range {}. should in (0,1,2,3,4)!'.format(report_range)
    fields_pool = CONSENSUS_COMP_INDICATOR_FIELDS if report_range == 0 else CONSENSUS_COMP_INDICATOR_FIELDS_V
    if report_range in (1, 3):
        fields_pool += CONSENSUS_COMP_INDICATORS_FIELDS_GRD_HIST
    if fields is None:
        fields = fields_pool
    else:
        fields = ensure_list_of_string(fields, 'consensus_comp_indicator')
        check_items_in_container(fields, fields_pool, 'consensus_comp_indicator')

    data = get_client().execute(
        'consensus.get_comp_indicators',
        order_book_ids, start_date, end_date, fields, report_range=report_range,
        market=market
    )
    if not data:
        return None
    if report_range in (1, 3) and len(fields) > 1 and (
            set(fields) & set(CONSENSUS_COMP_INDICATORS_FIELDS_GRD_HIST)
    ):
        new_data = defaultdict(dict)
        for d in data:
            pkey = (d['order_book_id'], d['date'])
            if pkey not in new_data:
                new_data[pkey] = d
                continue
            for k, v in d.items():
                if k not in new_data[pkey]:
                    new_data[pkey][k] = v
        df = pd.DataFrame(list(new_data.values()))
    else:
        df = pd.DataFrame(data)
    df.set_index(['order_book_id', 'date'], inplace=True)
    df.sort_index(inplace=True)
    dtypes = {f: COMP_INDICATORS_DTYPES[f] for f in df.columns if f in COMP_INDICATORS_DTYPES}
    df = df.astype(dtypes)
    return df


@ttl_cache(3600)
def _all_industries(market='cn'):
    return get_client().execute('consensus.all_industries', market=market)


@ttl_cache(3600)
def _all_industry_dict(market='cn'):
    result = defaultdict(list)
    for v in _all_industries(market):
        result[v['industry_code']].append(v['industry_code'])
        result[v['industry_name']].append(v['industry_code'])
    return result


def ensure_industries(industries):
    industries = ensure_list_of_string(industries)
    code_mapping = _all_industry_dict()
    industry_codes = set()
    for i in industries:
        if i in code_mapping:
            industry_codes.update(code_mapping[i])
    return list(industry_codes)


@export_as_api(namespace='consensus')
def all_industries(market='cn'):
    data = _all_industries(market)
    return pd.DataFrame(data).set_index('industry_code')


@export_as_api(namespace='consensus')
def get_industry_rating(industries, start_date, end_date, market='cn'):
    """
    获取行业评级数据

    :param industries: str or list, 行业code是今日投资行业分类代码, 可通过all_consensus_industries()获取全部
    :param start_date: date-like object， 结束日期
    :param end_date: date-like object, 结束日期
    :param market: str, 默认'cn'
    :return: pandas.DataFrame
    """
    industries = ensure_industries(industries)
    if not industries:
        warnings.warn('No valid industry found')
        return None

    start_date, end_date = ensure_date_range(start_date, end_date)
    data = get_client().execute('consensus.get_industry_rating', industries, start_date, end_date, market=market)
    if not data:
        return None

    df = pd.DataFrame(data)
    df.set_index(['industry_name', 'info_date'], inplace=True)
    return df


@export_as_api(namespace='consensus')
def get_market_estimate(indexes, fiscal_year, market='cn'):
    """
    获取今日投资的机构预测大势表

    :param indexes: str or list, 指数列表
    :param fiscal_year: int, 年份
    :param market: str, default 'cn'
    :return: pandas MultiIndex DataFrame

    :example:
    >>> rqdatac.consensus.get_market_estimate('000001.XSHG', 2021)
                                fiscal_year    institute start_date  ...  period  value
    order_book_id info_date                        ...
    000001.XSHG   2020-10-13        2021    财信证券 2021-01-01  ...  策略年度报告     中性
                  2020-10-16        2021    华融证券 2021-01-01  ...  策略年度报告     中性
                  2020-10-23        2021    东北证券 2021-01-01  ...  策略年度报告     中性
                  2020-11-01        2021    方正证券 2021-01-01  ...  策略年度报告     中性
                  2020-11-02        2021    西南证券 2021-01-01  ...  策略年度报告     中性
                                    ...      ...      ...       ...     ...        ...
                  2021-12-31        2021    山西证券 2022-01-01  ...  策略月度报告     中性
                  2021-12-31        2021    方正证券 2021-12-31  ...   策略日报等     中性
                  2021-12-31      2021    东亚前海证券 2022-01-01  ...  策略月度报告     中性
                  2021-12-31        2021    粤开证券 2022-01-01  ...  策略月度报告     乐观
                  2021-12-31        2021    渤海证券 2022-01-01  ...  策略月度报告     中性

    返回字段:
    fiscal_year: 预测年份
    institue: 机构名称
    start_date: 预测开始日期
    end_date: 预测结束日期
    high: 预测高点
    low: 预测低点
    period: 预测时段
    value: 预测值
    """

    indexes = ensure_list_of_string(indexes)
    indexes = ensure_order_book_ids(indexes, type='INDX')
    fiscal_year = int(fiscal_year)
    data = get_client().execute('consensus.get_market_estimate', indexes, fiscal_year, market=market)
    if not data:
        return None
    df = pd.DataFrame(data)
    df.set_index(['order_book_id', 'info_date'], inplace=True)
    df.sort_index(inplace=True)
    return df


export_as_api(deprecated(
    func=get_indicator,
    msg='get_consensus_indicator will be deprecated in future. use consensus.get_indicator instead.'
), name='get_consensus_indicator')
export_as_api(deprecated(
    func=get_price,
    msg='get_consensus_price will be deprecated in future. use consensus.get_price instead.'
), name='get_consensus_price')
export_as_api(deprecated(
    func=get_comp_indicators,
    msg='get_consensus_comp_indicators will be deprecated in future. use consensus.get_comp_indicators instead.'
), name='get_consensus_comp_indicators')
export_as_api(deprecated(
    func=all_industries,
    msg='all_consensus_industries will be deprecated in future. use consensus.all_industries instead.'
), name='all_consensus_industries')
export_as_api(deprecated(
    func=get_industry_rating,
    msg='get_consensus_industry_rating will be deprecated in future. use consensus.get_industry_rating instead.'
), name='get_consensus_industry_rating')
export_as_api(deprecated(
    func=get_market_estimate,
    msg='get_consensus_market_estimate will be deprecated in future. use consensus.get_market_estimate instead.'
), name='get_consensus_market_estimate')


VALID_STAT_PERIODS = ['WEEK1', 'MON1', 'MON3', 'MON6', 'YEAR1']


@export_as_api(namespace='consensus')
def get_security_change(order_book_ids, start_date=None, end_date=None, stat_periods=None):
    """
    获取机构报告统计周期内个股调整明细表

    :param order_book_ids: 股票名称
    :param start_date: 开始日期， date-like object, 默认三月前那天
    :param end_date: 结束日期， date-like object， 默认当天
    :param stat_periods: 统计周期，str/list, 默认全部, 可选值 {'WEEK1', 'MON1', 'MON3', 'MON6', 'YEAR1'}

    :return: pandas MultiIndex DataFrame

    返回字段：
    order_book_id
    date
    stat_period
    institute
    adjust_classification: 调整类别
        1 盈利预测调高;
        2 盈利预测调低;
        3 投资评级调高;
        4 投资评级调低;
        5 盈利预测维持;
        6 投资评级维持;
    """
    order_book_ids = ensure_order_book_ids(order_book_ids)
    start_date, end_date = ensure_date_range(start_date, end_date)

    if stat_periods is None:
        stat_periods = VALID_STAT_PERIODS
    else:
        stat_periods = ensure_list_of_string(stat_periods)
        check_items_in_container(stat_periods, VALID_STAT_PERIODS, 'stat_periods')

    data = get_client().execute('consensus.get_security_change', order_book_ids, start_date, end_date, stat_periods)
    if not data:
        return None
    df = pd.DataFrame(data)
    df.set_index(['order_book_id', 'date'], inplace=True)
    df.sort_index(inplace=True)
    return df


REPORT_PERIODS = {'q1': 103, 'q2': 106, 'q3': 109, 'q4': 112}
REPORT_TYPES = {'financial_reports': 0, 'performance_forecast': 1, 'current_performance': 2}
APPRAISAL_RESULTS = {'exceed': 1, 'below': 2}
VALID_REPORT_PERIODS = list(REPORT_PERIODS)
VALID_REPORT_TYPES = list(REPORT_TYPES)
VALID_APPRAISAL_RESULTS = list(APPRAISAL_RESULTS)
REVERSED_REPORT_PERIODS = {103: 'q1', 106: 'q2', 109: 'q3', 112: 'q4'}
REVERSED_REPORT_TYPES = {0: 'financial_reports', 1: 'performance_forecast', 2: 'current_performance'}
REVERSED_APPRAISAL_RESULTS = {1: 'exceed', 2: 'below'}


@export_as_api(namespace='consensus')
def get_expect_appr_exceed(
        order_book_ids,
        start_date=None,
        end_date=None,
        report_year=None,
        report_periods=None,
        report_types=None,
        appraisal_results=None
):
    """
    获取超预期鉴定数据

    :param order_book_ids: 股票名称
    :param start_date: 开始日期， date-like object, 默认三月前那天
    :param end_date: 结束日期， date-like object， 默认当天
    :param report_year: int, 报告年度，默认全部
    :param report_periods: str/list, 报告时段， 默认全部
        q1  一季度
        q2  半年度
        q3  三季度
        q4  年度
    :param report_types: str/list, 业绩报告类型, 默认全部
        financial_reports 财务定期报告
        performance_forecast 业绩预告
        current_performance 业绩快报
    :param appraisal_results: str/list, 鉴定结果,默认全部
        exceed 超预期
        below 低于预期

    :return: pandas MultiIndex DataFrame
    
    返回字段:
    report_year: int，报告年度
    report_period: str，报告时段
    report_type: str, 业绩报告类型
    appraisal_result: str，鉴定结果
        exceed 超预期
        below 低于预期
    info_date: datetime.datetime
    forecast_profit_max: float 业绩预告净利润上限，报告为年报时，对应的披露数据
    forecast_profit_min: float 业绩预告净利润下限，报告为年报时，对应的披露数据
    forecast_profit: float 业绩预告净利润，报告为年报时，对应的披露数据，包括定期报告和业绩快报数据
    adjust_con_profit: float，调整后一致预期净利润，报告为季报时，对应季报发布日之后第5个交易日的一致预期（T+1年）仅计算5日内的预测明细数据（简单平均）
    appraisal_date: datetime.datetime, 鉴定日
    appraisal_standard: int, 鉴定标准
        1 报表发布日鉴定
        2 报表发布周期鉴定
    con_cal_date: datetime.datetime, 一致预期计算日
    con_profit: float, 一致预期净利润
        鉴定标准为1时，为财报或者预告、快报发布日前一交易日的一致预期净利润；
        鉴定标准为2时，为对应财报期最后一个交易日的一致预期净利润
    profit_ex_rate: float, 业绩超预期幅度
        超预期幅度=(报告净利润或调整后一致预期净利润 - 一致预期净利润) / ABS(一致预期净利润)
    """
    order_book_ids = ensure_order_book_ids(order_book_ids)
    start_date, end_date = ensure_date_range(start_date, end_date)

    if report_periods is None:
        report_periods = VALID_REPORT_PERIODS
    else:
        report_periods = ensure_list_of_string(report_periods)
        check_items_in_container(report_periods, VALID_REPORT_PERIODS, 'report_periods')

    if report_types is None:
        report_types = VALID_REPORT_TYPES
    else:
        report_types = ensure_list_of_string(report_types)
        check_items_in_container(report_types, VALID_REPORT_TYPES, 'report_types')

    if appraisal_results is None:
        appraisal_results = VALID_APPRAISAL_RESULTS
    else:
        appraisal_results = ensure_list_of_string(appraisal_results)
        check_items_in_container(appraisal_results, VALID_APPRAISAL_RESULTS, 'appraisal_results')

    data = get_client().execute(
        'consensus.get_expect_appr_exceed', order_book_ids, start_date, end_date, report_year,
        [REPORT_PERIODS[_] for _ in report_periods],
        [REPORT_TYPES[_] for _ in report_types],
        [APPRAISAL_RESULTS[_] for _ in appraisal_results]
    )
    if not data:
        return None
    df = pd.DataFrame(data)
    df['report_period'] = df['report_period'].map(REVERSED_REPORT_PERIODS)
    df['report_type'] = df['report_type'].map(REVERSED_REPORT_TYPES)
    df['appraisal_result'] = df['appraisal_result'].map(REVERSED_APPRAISAL_RESULTS)
    df.set_index(['order_book_id', 'date'], inplace=True)
    df.sort_index(inplace=True)
    return df


@export_as_api(namespace='consensus')
def get_expect_prob(order_book_ids, expect_prob, start_date=None, end_date=None):
    """
    获取超/低于预期数据

    :param order_book_ids: str or list, 股票列表
    :param expect_prob: str, 'below': 低于预期， 'exceed': 超预期
    :param start_date: 开始日期， date-like object, 默认三月前那天
    :param end_date: 结束日期， date-like object， 默认当天

    :return: pandas.DataFrame
    
    返回字段:
    order_book_id
    date
    report_year: 报告年度
    report_period: 报告时段
        103  一季度 q1
        106  半年度 q2
        109  三季度 q3
        112  年度 q4
    info_classification: 预期类别代码
        exceed:
            1101 分析师上调（剔除明星分析师）
            1102 明星分析师上调
            1103 业绩公告后分析师全部上调
            1201 业绩公告后一致预期净利润大幅上调
            1301 研报标题超预期
            1302 研报摘要超预期
            1401 业绩预告/快报超上次预期
            1403 业绩预告/快报超一致预期
            1405 本期财报净利润超一致预期净利润（单季度）
            1501 本期财报净利润同比增速超年度一致预期净利润同比增速
            1502 本次预告/快报净利润同比增速超年度一致预期净利润同比增速
            1503 本期财报净利润同比增速超一致预期净利润同比增速（单季度）
            1504 本次预告/快报净利润同比增速超一致预期净利润同比增速（单季度）
        below:
            2101 分析师下调;
            2102 明星分析师下调（名字待定）
            2103 业绩公告后分析师全部下调
            2201 一致预期净利润大幅下调
            2301 研报标题低于预期
            2302 研报摘要低于预期
            2401 业绩预告/快报低于上次预期
            2403 业绩预告/快报低于一致预期
            2405 本期财报净利润低于一致预期净利润（单季度）
            2501 本期财报净利润同比增速低于年度一致预期净利润同比增速
            2502 本次预告/快报净利润同比增速低于年度一致预期净利润同比增速
            2503 本期财报净利润同比增速低于一致预期净利润同比增速（单季度）
            2504 本次预告/快报净利润同比增速低于一致预期净利润同比增速（单季度）
    institute: 研究机构简称
    info_summary: 超预期信息简述
    report_date: 本次研究报告撰写日
    title: 本次研报标题
    author: 本次研报作者
    est_profit: 本次研报预测净利润
    report_date_last: 上次研究报告撰写日
    title_last: 上次研报标题
    est_profit_last: 上次研报预测净利润
    info_date: 本次业绩报告日
    report_type: 本次业绩报告类型
        0 财务定期报告 financial_reports
        1 业绩预告 performance_forecast
        2 业绩快报 current_performance
    forecast_profit_max: 本次业绩预告上限净利润 适用类型：1 业绩预告
    forecast_profit_min: 本次业绩预告下限净利润 适用类型：1 业绩预告
    profit: 本次业绩报告净利润	适用类型：0 财务定期报告； 2 业绩快报
    profit_q: 本次业绩报告净利润（单季度） 适用类型：0 财务定期报告； 2 业绩快报
    forecast_profit_growth_limit: 本次业绩预告净利润同比增速上下限
        exceed: 下限
        below:  上限
        适用类型：0 财务定期报告； 2 业绩快报
    profit_growth: 本次业绩报告净利润同比增速 适用类型：1 业绩预告
    forecast_profit_growth_limit_q: 本次业绩预告净利润同比增速上下限（单季度）
        exceed: 下限
        below:  上限
        适用类型：0 财务定期报告； 2 业绩快报
    profit_growth_q: 本次业绩报告净利润同比增速（单季度） 适用类型：1 业绩预告 2 业绩快报
    fin_report_date_last: 上次业绩报告公告日 适用类型：1 业绩预告； 2 业绩快报
    fin_report_type_last: 上次业绩报告类型 1 业绩预告； 2 业绩快报
    forecast_profit_max_last: 上次业绩预告上限净利润 适用类型：1 业绩预告；
    forecast_profit_min_last: 上次业绩预告下限净利润 适用类型：1 业绩预告；
    profit_last: 上次业绩快报净利润 	适用类型：2 业绩快报
    con_calc_date: 本次一致预期计算日
    con_profit: 本次一致预期净利润
    con_calc_date_last: 上次一致预期计算日
    con_profit_last: 上次一致预期净利润
    con_profit_q_last: 上次一致预期净利润（单季度）
    con_profit_growth_last: 上次一致预期净利润同比增速（年度）
    con_profit_growth_q_last: 上次一致预期净利润同比增速（单季度）
    expect_rate: 业绩上下调幅度或低于预期幅度
    """

    order_book_ids = ensure_order_book_ids(order_book_ids)
    start_date, end_date = ensure_date_range(start_date, end_date)

    ensure_string_in(expect_prob, ('exceed', 'below'))
    if expect_prob not in ('exceed', 'below'):
        raise ValueError('invalid expect_prob: {}'.format(expect_prob))

    data = get_client().execute('consensus.get_expect_prob', order_book_ids, expect_prob, start_date, end_date)
    if not data:
        return None
    df = pd.DataFrame(data)
    df['report_period'] = df['report_period'].map(REVERSED_REPORT_PERIODS)
    df['report_type'] = df['report_type'].map(REVERSED_REPORT_TYPES)
    df.set_index(['order_book_id', 'date'], inplace=True)
    df.sort_index(inplace=True)
    return df


FACTOR_EMOTIONS = [
    'MTK_CONF',
    'OPTIM_CONF',
    'PESSIM_CONF',
    'TY_PROFIT_T1_DEV',
    'TY_PROFIT_T2_DEV',
    'TY_PROFIT_T3_DEV',
    'TY_EPS_T1_DEV',
    'TY_EPS_T2_DEV',
    'TY_EPS_T3_DEV',
    'EPS_T1_DEV',
    'EPS_T2_DEV',
    'EPS_T3_DEV',
    'PROFIT_T1_DEV',
    'PROFIT_T2_DEV',
    'PROFIT_T3_DEV',
    'OP_REVEN_T1_DEV',
    'OP_REVEN_T2_DEV',
    'OP_REVEN_T3_DEV',
    'OP_COST_T1_DEV',
    'OP_COST_T2_DEV',
    'OP_COST_T3_DEV',
    'OP_PROFIT_T1_DEV',
    'OP_PROFIT_T2_DEV',
    'OP_PROFIT_T3_DEV',
    'OP_CASH_FLOW_T1_DEV',
    'OP_CASH_FLOW_T2_DEV',
    'OP_CASH_FLOW_T3_DEV',
    'ROE_T1_DEV',
    'ROE_T2_DEV',
    'ROE_T3_DEV',
    'PEG_1Y_DEV',
    'PEG_3Y_DEV',
    'PB_T1_DEV',
    'PB_T2_DEV',
    'PB_T3_DEV',
    'PE_T1_DEV',
    'PE_T2_DEV',
    'PE_T3_DEV',
    'PS_T1_DEV',
    'PS_T2_DEV',
    'PS_T3_DEV',
    'PCF_T1_DEV',
    'PCF_T2_DEV',
    'PCF_T3_DEV',
]
FACTOR_EMOTIONS = ['{}_{}D'.format(f, d) for d in [7, 14, 30, 60, 90] for f in FACTOR_EMOTIONS]

FACTOR_VALUATIONS = [
    'PEG_1Y',
    'PEG_1Y_SCO',
    'PEG_3Y',
    'PEG_3Y_SCO',
    'RV_VALUT_EM',
    'RV_VALUT_EM_SCO',
    'PB_T',
    'PE_T',
    'PS_T',
    'PCF_T',
    'PB_T_SCO',
    'PE_T_SCO',
    'PS_T_SCO',
    'PCF_T_SCO',
    'PB_T1',
    'PE_T1',
    'PS_T1',
    'PCF_T1',
    'PB_T1_SCO',
    'PE_T1_SCO',
    'PS_T1_SCO',
    'PCF_T1_SCO',
    'PB_T2',
    'PE_T2',
    'PS_T2',
    'PCF_T2',
    'PB_T2_SCO',
    'PE_T2_SCO',
    'PS_T2_SCO',
    'PCF_T2_SCO',
    'PB_T3',
    'PE_T3',
    'PS_T3',
    'PCF_T3',
    'PB_T3_SCO',
    'PE_T3_SCO',
    'PS_T3_SCO',
    'PCF_T3_SCO',
    'PB_FTM',
    'PE_FTM',
    'PS_FTM',
    'PCF_FTM',
    'PB_FTM_SCO',
    'PE_FTM_SCO',
    'PS_FTM_SCO',
    'PCF_FTM_SCO',
]

FACTOR_GROWTHS = [
    'TY_PROFIT_T1_CHG',
    'TY_PROFIT_T2_CHG',
    'TY_PROFIT_T3_CHG',
    'TY_EPS_T1_CHG',
    'TY_EPS_T2_CHG',
    'TY_EPS_T3_CHG',
    'PROFIT_T1_CHG',
    'PROFIT_T2_CHG',
    'PROFIT_T3_CHG',
    'EPS_T1_CHG',
    'EPS_T2_CHG',
    'EPS_T3_CHG',
    'OP_REVEN_T1_CHG',
    'OP_REVEN_T2_CHG',
    'OP_REVEN_T3_CHG',
    'OP_COST_T1_CHG',
    'OP_COST_T2_CHG',
    'OP_COST_T3_CHG',
    'OP_PROFIT_T1_CHG',
    'OP_PROFIT_T2_CHG',
    'OP_PROFIT_T3_CHG',
    'OP_CASH_FLOW_T1_CHG',
    'OP_CASH_FLOW_T2_CHG',
    'OP_CASH_FLOW_T3_CHG',
    'ASSET_T1_CHG',
    'ASSET_T2_CHG',
    'ASSET_T3_CHG',
    'ROE_T1_CHG',
    'ROE_T2_CHG',
    'ROE_T3_CHG',
]
FACTOR_GROWTHS = ['{}_{}D'.format(f, d) for d in [7, 14, 30, 60, 90] for f in FACTOR_GROWTHS]

FACTOR_FINS = [
    'RPT_YR_T',
    'ANN_RPT_DT_LAST',
    'PROFIT_T',
    'PROFIT_T1',
    'PROFIT_T2',
    'PROFIT_T3',
    'PROFIT_FTM',
    'PROFIT_YOY_T',
    'PROFIT_YOY_T1',
    'PROFIT_YOY_T2',
    'PROFIT_YOY_T3',
    'PROFIT_YOY_FTM',
    'PROFIT_CAGR_2Y',
    'PROFIT_CAGR_3Y',
    'TY_PROFIT_T1',
    'TY_PROFIT_T2',
    'TY_PROFIT_T3',
    'TY_PROFIT_FTM',
    'TY_PROFIT_YOY_T1',
    'TY_PROFIT_YOY_T2',
    'TY_PROFIT_YOY_T3',
    'TY_PROFIT_YOY_FTM',
    'EPS_T',
    'EPS_T1',
    'EPS_T2',
    'EPS_T3',
    'EPS_FTM',
    'EPS_YOY_T',
    'EPS_YOY_T1',
    'EPS_YOY_T2',
    'EPS_YOY_T3',
    'EPS_YOY_FTM',
    'TY_EPS_T1',
    'TY_EPS_T2',
    'TY_EPS_T3',
    'TY_EPS_FTM',
    'TY_EPS_YOY_T1',
    'TY_EPS_YOY_T2',
    'TY_EPS_YOY_T3',
    'TY_EPS_YOY_FTM',
    'OP_REVEN_T',
    'OP_REVEN_T1',
    'OP_REVEN_T2',
    'OP_REVEN_T3',
    'OP_REVEN_FTM',
    'OP_REVEN_YOY_T',
    'OP_REVEN_YOY_T1',
    'OP_REVEN_YOY_T2',
    'OP_REVEN_YOY_T3',
    'OP_REVEN_YOY_FTM',
    'OP_REVEN_CAGR_2Y',
    'OP_REVEN_CAGR_3Y',
    'OP_COST_T',
    'OP_COST_T1',
    'OP_COST_T2',
    'OP_COST_T3',
    'OP_COST_FTM',
    'OP_COST_YOY_T',
    'OP_COST_YOY_T1',
    'OP_COST_YOY_T2',
    'OP_COST_YOY_T3',
    'OP_COST_YOY_FTM',
    'OP_PROFIT_T',
    'OP_PROFIT_T1',
    'OP_PROFIT_T2',
    'OP_PROFIT_T3',
    'OP_PROFIT_FTM',
    'OP_PROFIT_YOY_T',
    'OP_PROFIT_YOY_T1',
    'OP_PROFIT_YOY_T2',
    'OP_PROFIT_YOY_T3',
    'OP_PROFIT_YOY_FTM',
    'ROE_T',
    'ROE_T1',
    'ROE_T2',
    'ROE_T3',
    'ROE_FTM',
    'ROE_YOY_T',
    'ROE_YOY_T1',
    'ROE_YOY_T2',
    'ROE_YOY_T3',
    'ROE_YOY_FTM',
    'OP_CASH_FLOW_T',
    'OP_CASH_FLOW_T1',
    'OP_CASH_FLOW_T2',
    'OP_CASH_FLOW_T3',
    'OP_CASH_FLOW_FTM',
    'OP_CASH_FLOW_YOY_T',
    'OP_CASH_FLOW_YOY_T1',
    'OP_CASH_FLOW_YOY_T2',
    'OP_CASH_FLOW_YOY_T3',
    'OP_CASH_FLOW_YOY_FTM',
    'ASSET_T',
    'ASSET_T1',
    'ASSET_T2',
    'ASSET_T3',
    'ASSET_FTM',
    'ASSET_YOY_T',
    'ASSET_YOY_T1',
    'ASSET_YOY_T2',
    'ASSET_YOY_T3',
    'ASSET_YOY_FTM',
    'EARN_QUAL',
]

VALID_FACTOR_FIELDS = FACTOR_EMOTIONS + FACTOR_GROWTHS + FACTOR_VALUATIONS + FACTOR_FINS


@export_as_api(namespace='consensus')
def get_factor(order_book_ids, factors, start_date=None, end_date=None):
    """
    获取一致预期因子库数据

    :param order_book_ids: str or list, 股票列表
    :param factors: str or list, 因子列表
    :param start_date: 开始日期， date-like object, 默认三月前那天
    :param end_date: 结束日期， date-like object， 默认当天

    :return: pandas.DataFrame
    """
    order_book_ids = ensure_order_book_ids(order_book_ids)
    start_date, end_date = ensure_date_range(start_date, end_date)

    factors = ensure_list_of_string(factors)
    check_items_in_container(factors, VALID_FACTOR_FIELDS, 'factors')

    data = get_client().execute('consensus.get_factor', order_book_ids, factors, start_date, end_date)
    if not data:
        return

    result = defaultdict(dict)
    for r in data:
        key = (r['order_book_id'], r['date'])
        result[key].update(r)

    df = pd.DataFrame(result.values())
    df.set_index(['order_book_id', 'date'], inplace=True)
    fields = [f for f in df.columns if f != 'ANN_RPT_DT_LAST']
    df[fields] = df[fields].astype(float)
    df.sort_index(inplace=True)
    return df


ANALYST_MOMEMTUM_FIELDS = [
    'profit_chg_1w',
    'profit_chg_1w_rank',
    'profit_chg_1w_sco',
    'profit_chg_2w',
    'profit_chg_2w_rank',
    'profit_chg_2w_sco',
    'profit_chg_1m',
    'profit_chg_1m_rank',
    'profit_chg_1m_sco',
    'profit_chg_2m',
    'profit_chg_2m_rank',
    'profit_chg_2m_sco',
    'profit_chg_3m',
    'profit_chg_3m_rank',
    'profit_chg_3m_sco',
    'op_reven_chg_1w',
    'op_reven_chg_1w_rank',
    'op_reven_chg_1w_sco',
    'op_reven_chg_2w',
    'op_reven_chg_2w_rank',
    'op_reven_chg_2w_sco',
    'op_reven_chg_1m',
    'op_reven_chg_1m_rank',
    'op_reven_chg_1m_sco',
    'op_reven_chg_2m',
    'op_reven_chg_2m_rank',
    'op_reven_chg_2m_sco',
    'op_reven_chg_3m',
    'op_reven_chg_3m_rank',
    'op_reven_chg_3m_sco',
    'ty_est_dev',
    'ty_est_dev_rank',
    'ty_est_dev_sco',
    'est_em_bic_sco',
    'est_em_non_bic_sco',
    'grd_em_1m',
    'grd_em_1m_rank',
    'grd_em_1m_sco',
    'grd_em_2m',
    'grd_em_2m_rank',
    'grd_em_2m_sco',
    'grd_em_3m',
    'grd_em_3m_rank',
    'grd_em_3m_sco',
    'targ_price_space',
    'targ_price_space_rank',
    'targ_price_space_sco',
    'grd_em_sco',
    'ana_em_bic_sco',
    'ana_em_non_bic_sco',
]

OBJECT_DTYPE = np.dtype('O')


@export_as_api(namespace='consensus')
def get_analyst_momentum(
        order_book_ids,
        fiscal_year=None,
        start_date=None,
        end_date=None,
        fields=None,
        report_periods=None,
        report_range=None,
        market='cn'
):
    """
    获取一致预期分析师动能数据

    :param order_book_ids: 股票名称
    :param fiscal_year: int/str, 查询年份, 默认返回全部
    :param start_date: date-like object, 开始日期, 默认三月前那天
    :param end_date: date-like object, 结束日期, 默认当天
    :param fields: stor/list, 数据字段, 默认返回全部
    :param report_periods: str/list, 报告时段， 默认全部
        q1  一季度
        q2  半年度
        q3  三季度
        q4  年度
    :param report_range: int, 默认全部
        1-考虑补录入&包括所有报告数据
        3-不考虑补录入&包括所有报告数据
    :param market: Default('cn')
    :returns: pandas  MultiIndex DataFrame
    
    返回字段说明:
    profit_chg_1w	        净利润1周变化率        [一致预期净利润（当前）-一致预期净利润（1周前）]/ [︱一致预期净利润（1周前）︱+0.5*总股本]
    profit_chg_1w_rank	    净利润1周变化率排名      全市场排名
    profit_chg_1w_sco	    净利润1周变化率得分      百分制打分，排名最靠前的1%为100分。
    profit_chg_2w   	    净利润2周变化率        [一致预期净利润（当前）-一致预期净利润（2周前）]/ [︱一致预期净利润（2周前）︱+0.5*总股本]
    profit_chg_2w_rank	    净利润2周变化率排名      全市场排名
    profit_chg_2w_sco	    净利润2周变化率得分      百分制打分，排名最靠前的1%为100分。
    profit_chg_1m	        净利润1月变化率        [一致预期净利润（当前）-一致预期净利润（1月前）]/ [︱一致预期净利润（1月前）︱+0.5*总股本]
    profit_chg_1m_rank	    净利润1月变化率排名      全市场排名
    profit_chg_1m_sco	    净利润1月变化率得分      百分制打分，排名最靠前的1%为100分。
    profit_chg_2m   	    净利润2月变化率        [一致预期净利润（当前）-一致预期净利润（2月前）]/ [︱一致预期净利润（2月前）︱+0.5*总股本]
    profit_chg_2m_rank	    净利润2月变化率排名      全市场排名
    profit_chg_2m_sco	    净利润2月变化率得分      百分制打分，排名最靠前的1%为100分。
    profit_chg_3m	        净利润3月变化率        [一致预期净利润（当前）-一致预期净利润（3月前）]/ [︱一致预期净利润（3月前）︱+0.5*总股本]
    profit_chg_3m_rank	    净利润3月变化率排名      全市场排名
    profit_chg_3m_sco	    净利润3月变化率得分      百分制打分，排名最靠前的1%为100分。
    op_reven_chg_1w	        业务收入1周变化率       [一致预期业务收入（当前）-一致预期业务收入（1周前）]/ 一致预期业务收入（1周前）
    op_reven_chg_1w_rank	业务收入1周变化率排名     全市场排名
    op_reven_chg_1w_sco	    业务收入1周变化率得分     百分制打分，排名最靠前的1%为100分。
    op_reven_chg_2w	        业务收入2周变化率       [一致预期业务收入（当前）-一致预期业务收入（2周前）]/ 一致预期业务收入（2周前）
    op_reven_chg_2w_rank	业务收入2周变化率排名     全市场排名
    op_reven_chg_2w_sco	    业务收入2周变化率得分     百分制打分，排名最靠前的1%为100分。
    op_reven_chg_1m	        业务收入1月变化率       [一致预期业务收入（当前）-一致预期业务收入（1月前）]/ 一致预期业务收入（1月前）
    op_reven_chg_1m_rank	业务收入1月变化率排名     全市场排名
    op_reven_chg_1m_sco	    业务收入1月变化率得分     百分制打分，排名最靠前的1%为100分。
    op_reven_chg_2m	        业务收入2月变化率       [一致预期业务收入（当前）-一致预期业务收入（2月前）]/ 一致预期业务收入（2月前）
    op_reven_chg_2m_rank	业务收入2月变化率排名     全市场排名
    op_reven_chg_2m_sco	    业务收入2月变化率得分     百分制打分，排名最靠前的1%为100分。
    op_reven_chg_3m	        业务收入3月变化率       [一致预期业务收入（当前）-一致预期业务收入（3月前）]/ 一致预期业务收入（3月前）
    op_reven_chg_3m_rank	业务收入3月变化率排名     全市场排名
    op_reven_chg_3m_sco	    业务收入3月变化率得分     百分制打分，排名最靠前的1%为100分。
    ty_est_dev	            天眼预期偏离度	        （天眼预期-一致预期）/(｜一致预期｜+0.5*总股本）
    ty_est_dev_rank	        天眼预期偏离度排名       全市场排名
    ty_est_dev_sco	        天眼预期偏离度得分       百分制打分，排名最靠前的1%为100分。
    est_em_bic_sco	        预期动能得分(考虑业务收入变化率)   考虑了收入的变化率
    est_em_non_bic_sco	    预期动能得分(不考虑业务收入变化率)  未考虑了收入的变化率
    grd_em_1m           	评级动能1月            1个月前评级系数-现在评级系数；对于单个评级，强力买入1.00；买入2.00；观望3.00；适度减持4.00；卖出5.00。评级系数为60天内所有给出评级机构最新评级的简单平均。
    grd_em_1m_rank	        评级动能1月排名         全市场排名
    grd_em_1m_sco	        评级动能1月得分         百分制打分，排名最靠前的1%为100分。
    grd_em_2m	            评级动能2月            2个月前评级系数-现在评级系数；对于单个评级，强力买入1.00；买入2.00；观望3.00；适度减持4.00；卖出5.00。评级系数为60天内所有给出评级机构最新评级的简单平均。
    grd_em_2m_rank	        评级动能2月排名         全市场排名
    grd_em_2m_sco	        评级动能2月得分         百分制打分，排名最靠前的1%为100分。
    grd_em_3m	            评级动能3月            3个月前评级系数-现在评级系数；对于单个评级，强力买入1.00；买入2.00；观望3.00；适度减持4.00；卖出5.00。评级系数为60天内所有给出评级机构最新评级的简单平均。
    grd_em_3m_rank	        评级动能3月排名         全市场排名
    grd_em_3m_sco	        评级动能3月得分         百分制打分，排名最靠前的1%为100分。
    targ_price_space	    目标价涨升空间
    targ_price_space_rank	目标价涨升空间排名       全市场排名
    targ_price_space_sco	目标价涨升空间得分       百分制打分，排名最靠前的1%为100分。
    grd_em_sco	            评级动能得分            百分制打分，排名最靠前的1%为100分。
    ana_em_bic_sco	        分析师动能得分(考虑业务收入变化率)      0.3*天眼预期得分+0.2*预期业绩动能得分+0.3*目标价涨升空间得分+0.2*评级动能得分（考虑业务收入变动情况）
    ana_em_non_bic_sco	    分析师动能得分(不考虑业务收入变化率)     0.3*天眼预期得分+0.2*预期业绩动能得分2+0.3*目标价涨升空间得分+0.2*评级动能得分（不考虑业务收入变动）
    """
    order_book_ids = ensure_order_book_ids(order_book_ids)
    start_date, end_date = ensure_date_range(start_date, end_date)

    if fiscal_year is not None:
        fiscal_year = int(fiscal_year)

    if fields is None:
        fields = ANALYST_MOMEMTUM_FIELDS
    else:
        fields = ensure_list_of_string(fields, 'analyst_momentum')
        check_items_in_container(fields, ANALYST_MOMEMTUM_FIELDS, 'analyst_momentum')

    if report_periods is not None:
        report_periods = ensure_list_of_string(report_periods)
        check_items_in_container(report_periods, VALID_REPORT_PERIODS, 'report_periods')
        report_periods = [REPORT_PERIODS[_] for _ in report_periods]

    if report_range is not None:
        assert report_range in (1, 3), 'invalid report_range {}. should in (1,3)!'.format(report_range)

    data = get_client().execute(
        'consensus.get_analyst_momentum',
        order_book_ids, fiscal_year, start_date, end_date, fields,
        report_periods,
        report_range,
        market=market
    )

    if not data:
        return None

    df = pd.DataFrame(data)
    dtypes = {f: (dtype if dtype != OBJECT_DTYPE else '<f8') for f, dtype in df[fields].dtypes.items()}
    df = df.astype(dtypes)
    df['report_period'] = df['report_period'].map(REVERSED_REPORT_PERIODS)
    df.set_index(['order_book_id', 'date'], inplace=True)
    return df
