import requests
import csv
import os

if os.path.isfile("env.py"):
    import env  # noqa


API_KEY = os.environ.get('API_KEY')
BRANDS = ['apple', 'amazon', 'netflix', 'facebook', 'google']
COMPANIES = [
    'APPLE INC', 'AMAZON.COM', 'NETFLIX INC', 'META PLATFORMS INC-CLASS', 'ALPHABET INC-CL']
SYMBOLS = ['AAPL', 'AMZN', 'NFLX', 'META', 'GOOGL']


def call_api(symbol):
    token = 'ceatviiad3i52v0dd6b0ceatviiad3i52v0dd6bg'
    params = dict(symbol=symbol, token=token)
    r = requests.get('https://finnhub.io/api/v1/quote', params=params)

    # print(r.url)
    res = r.json()
    this_brand = {
        'symbol': symbol,
        'percentage_change': res['dp'],
        'current_price': res['c'],
        'last_close_price': res['pc']
    }
    return this_brand


final_results = [call_api(symbol) for symbol in SYMBOLS]
headers = ['stock_symbol', 'percentage_change', 'current_price', 'last_close_price']


with open('final_results.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for item in final_results:

        writer.writerow([
            item['symbol'],
            item['percentage_change'],
            item['current_price'],
            item['last_close_price']
        ])
