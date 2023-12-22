import time
import datetime
import requests
import csv
import random
import pandas as pd 
import Keps


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


stocks_csv = 'stocks_name.csv'

def read_symbols(stocks_csv):
    symbols = []

    with open(stocks_csv, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Using DictReader for easy access to columns by name

        for row in reader:
            symbols.append(row['Symbol'])  # Append the symbol from each row

    # Select one random symbol from the list
    random_symbol = random.choice(symbols) if symbols else None
    return random_symbol


def stock_data(ticker):
    """
    Returns the latest open and close price of a stock.
    """
    # Get today's date
    today = datetime.datetime.now()

    # Set period1 to the start of today and period2 to the end of today
    period1 = int(time.mktime(today.replace(hour=0, minute=0, second=0, microsecond=0).timetuple()))
    period2 = int(time.mktime(today.replace(hour=23, minute=59, second=59, microsecond=0).timetuple()))

    interval = "1d"

    # Construct the query string
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

    try:
        df = pd.read_csv(query_string)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

print(stock_data(read_symbols(stocks_csv)))

def main():
    ticker = random_symbols
    news_items = get_stock_news(ticker, api_key)

    tickers_data = [[article['tickers']]for article in news_items]
    sentimental_data = [[article['sentiment']] for article in news_items]
    
    return