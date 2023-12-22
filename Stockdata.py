import time
import datetime
import pandas as pd 

import requests
import Keps


def stock_data(ticker):
    """
    returns the open and close price of a stock
    """
    period1 = int(time.mktime(datetime.datetime(2023,11,1,23,59).timetuple()))
    period2 = int(time.mktime(datetime.datetime(2023,11,30,23,59).timetuple()))
    interval = "1wk" #1d,1m

    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

    df = pd.read_csv(query_string)
    result = print(df)
    return result


def get_stock_news(ticker, api_key):
    
    base_url = "https://stocknewsapi.com/api/v1"
    params = {
        'tickers': ticker,
        'items': 3,  # Adjusted to 3 items for the trial plan
        'page': 1,
        'token': api_key
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # This will raise an error for HTTP error codes

        # Parse the JSON response
        news_data = response.json()

        # Extract the news articles from the response
        articles = news_data.get('data', [])
        return articles

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


api_key = Keps.api_key
ticker = 'AMZN'
news_items = get_stock_news(ticker, api_key)

res = [[article['tickers'], article['date'], article['sentiment']] for article in news_items]
print(res)





