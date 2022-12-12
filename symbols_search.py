'''
as a second attempt to get stock symbols I used https://finnhub.io/docs/api/stock-symbols.
forloop returned none, I realised that brands are not applicable, and reaserched for 
proper comany names (list companies)

'''

import requests
import os
if os.path.isfile("env.py"):
    import env  # noqa


API_KEY = os.environ.get('API_KEY')


brands = ['apple', 'amazon', 'netflix', 'facebook', 'google']
companies = ['APPLE INC', 'AMAZON.', 'NETFLIX INC', 'META PLATFORMS', 'ALPHABET']


def call_api():
    token = API_KEY
    params = dict(exchange='US', currency='USD', token=token)
    r = requests.get('https://finnhub.io/api/v1/stock/symbol', params=params)
    res = r.json()
    return res


def get_symbol(brand):
    list_result = call_api()
    for company in list_result:
        if brand in company['description']:
            return company['symbol']


SYMBOLS = [get_symbol(company) for company in companies]


with open('results/02_stock_symbols.py', 'w') as f:
    f.write(str(SYMBOLS))
