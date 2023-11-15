import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


# Get data about the Stock from https://www.alphavantage.co/query
trading_api_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol':  STOCK,
    'interval': '60min',
    'datatype': 'json',
    'apikey': os.environ.get("STOCK_API_KEY")
}

url = 'https://www.alphavantage.co/query'
res = requests.get(url, params=trading_api_params)
res.raise_for_status()
data_trading = res.json()["Time Series (Daily)"]
# A list with all the dates starting now going back every hour until 4am
date_keys = list(data_trading)
stock_price_yesterday = data_trading[date_keys[1]]['4. close']
stock_price_before_yesterday = data_trading[date_keys[2]]['4. close']

stock_dif = float(stock_price_yesterday) - float(stock_price_before_yesterday)
stock_percentage_dif = round(
    stock_dif / float(stock_price_before_yesterday) * 100)

emoji_up_down = None
if stock_dif < 0:
    emoji_up_down = '🔻'
else:
    emoji_up_down = '🔺'

# Get news about the company if price difference from yesterday is bigger than 5% from
# https://newsapi.org
if abs(stock_percentage_dif) > 5:
    news_api_params = {
        'apiKey': os.environ.get('NEWS_API_KEY'),
        'q': COMPANY_NAME
    }

    url_news = 'https://newsapi.org/v2/everything'
    res_news = requests.get(url_news, params=news_api_params)
    res_news.raise_for_status()
    data_news = res_news.json()["articles"]
    first_articles = [data_news[:3]]
