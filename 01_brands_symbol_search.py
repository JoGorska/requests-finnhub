'''
I initially used https://finnhub.io/docs/api/symbol-search to find the symbols for each brand
but the results I was getting contained *.de and other letters after a dot,
none of the results gave me AAPL - which was given as an example of apple symbol
'''

import requests
from run import API_KEY


def get_code(brand):
    '''
    gets symbol-search url to get symbols for brandhs
    '''
    params = dict(token=API_KEY, q=brand)
    r = requests.get('https://finnhub.io/api/v1/search', params=params)

    res = r.json()
    list_of_results = res['result']
    list_of_codes = [item['symbol'] for item in list_of_results]
    return list_of_codes


brands = ['apple', 'amazon', 'netflix', 'facebook', 'google']

brands_with_codes = [{brand: get_code(brand)} for brand in brands]

with open('results/01_brands.py', 'w') as f:
    f.write(str(brands_with_codes))
