import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
def company_industries():

    headers =\
        {
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://trading.vietcap.com.vn",
            "Referer": "https://trading.vietcap.com.vn/price-board?filter-group=INDUSTRY_MENU&filter-value=2300&view-type=FLAT",
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/138.0.0.0 Safari/537.36")
        }

    query =\
        """
            {
                CompaniesListingInfo
                {
                    ticker
                    organName
                    # enOrganName
                    icbName3
                    # enIcbName3
                    icbName2
                    # enIcbName2
                    icbName4
                    # enIcbName4
                    # comTypeCode
                    # icbCode1
                    # icbCode2
                    # icbCode3
                    # icbCode4
                    # __typename
                }
            }
        """

    payload = \
        {
            "query": query,
            "variables":
            {

            }
        }

    url_comp = 'https://trading.vietcap.com.vn/data-mt/graphql'
    res_comp = requests.post(url=url_comp, json=payload, headers=headers)
    data_comp = res_comp.json()['data']['CompaniesListingInfo']
    df_comp = pd.DataFrame(data_comp)

    url_floor = 'https://trading.vietcap.com.vn/api/price/symbols/getAll'
    res_floor = requests.get(url = url_floor,headers=headers)
    data_floor = res_floor.json()
    df_floor = pd.DataFrame(data_floor)
    df_floor.rename(columns={'symbol': 'ticker'}, inplace=True)
    df_floor = df_floor[['ticker','board']]

    df_all = pd.merge(df_comp,df_floor,on='ticker', how='left')
    df_all = df_all[['ticker','board','organName','icbName2','icbName3','icbName4']]

    return df_all

def FinancialStatement(symbol,report_type, periods):
    '''
    report_type: BALANCE_SHEET, INCOME_STATEMENT, CASH_FLOW, NOTE \n
    period: years, quarters
    '''

    headers =\
        {
            'sec-ch-ua-platform': '"macOS"',
            'Referer': 'https://trading.vietcap.com.vn/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
            'Accept': 'application/json',
            'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
            'sec-ch-ua-mobile': '?0',
        }

    params =\
            {
                'section': report_type,
            }

    url = f'https://iq.vietcap.com.vn/api/iq-insight-service/v1/company/{symbol}/financial-statement'
    url_meta = f'https://iq.vietcap.com.vn/api/iq-insight-service/v1/company/{symbol}/financial-statement/metrics'

    res = requests.get\
            (
                url=url,
                params=params,
                headers=headers,
            )

    df_raw = pd.DataFrame(res.json()['data'][periods])
    df_raw.drop\
        (
            [
                'organCode',
                'createDate',
                'publicDate',
                'updateDate',
                'ticker'
            ],
            axis=1,
            inplace=True
        )

    df_raw["yearReport"] = np.where(
        df_raw["lengthReport"].isin([1,2,3,4]),
        "Q" + df_raw["lengthReport"].astype(str) + "-" + df_raw["yearReport"].astype(str),
        "Năm " + df_raw["yearReport"].astype(str)
    )

    df_long = df_raw.melt(id_vars='yearReport', var_name='field', value_name='value')
    df_wide = df_long.pivot(index='field', columns='yearReport', values='value')
    df_wide = df_wide.sort_index\
        (
            axis=1,
            key=lambda x: x.map(lambda v: (int(v[-4:]), int(v[1]) if v.startswith("Q") else 5))
        ).reset_index()
    df_wide.columns.name = None

    res_meta = requests.get\
        (
            url=url_meta,
            params=params,
            headers=headers,
        )

    df_meta = pd.DataFrame(res_meta.json()['data'][report_type])
    df_meta.drop(['parent', 'titleEn', 'titleVi', 'name', 'fullTitleEn'], axis=1, inplace=True)

    df_final = pd.merge(df_meta, df_wide, on='field', how='left')
    df_final.drop(['field','level'], axis=1, inplace=True)
    df_final.rename(columns={'fullTitleVi': 'Name'}, inplace=True)
    
    return df_final

def price_stock(symbol, interval, count_back=9999):

    headers =\
        {
            'sec-ch-ua-platform': '"macOS"',
            'Referer': 'https://trading.vietcap.com.vn/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
            'Accept': 'application/json',
            'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
            'sec-ch-ua-mobile': '?0',
        }
    
    url = 'https://trading.vietcap.com.vn/api/chart/OHLCChart/gap-chart'

    end_time = datetime.now() + timedelta(days=1)
    end_stamp = int(end_time.timestamp())

    OHLC_MAP =\
        {
        't': 'time',
        'o': 'open',
        'h': 'high',
        'l': 'low',
        'c': 'close',
        'v': 'volume'
        }
    
    payload =\
        {
            "timeFrame": interval,
            "symbols": [symbol],
            "to": end_stamp,
            "countBack": count_back
        }
    
    res = requests.post(url, headers=headers, json=payload)
    df = pd.DataFrame(res.json()[0])
    df = df.rename(columns=OHLC_MAP)
    df['time'] = pd.to_datetime(df['time'].astype(int), unit='s').dt.date
    df = df.sort_values('time', ascending=False).reset_index(drop=True)
    df.drop(['accumulatedVolume','minBatchTruncTime','accumulatedValue'], axis=1, inplace=True)

    return df

