import requests
from run import API_KEY


def get_code(brand):
    '''
    https://finnhub.io/docs/api/symbol-search
    describes how to find symbol for a company and gives apple as an example
    but when I run this url in requests I am not getting AAPL code.
    '''
    params = dict(token=API_KEY, q=brand)
    r = requests.get('https://finnhub.io/api/v1/search', params=params)

    res = r.json()
    list_of_results = res['result']
    list_of_codes = [item['symbol'] for item in list_of_results]
    return list_of_codes


# find latest price
brands = ['apple', 'amazon', 'netflix', 'facebook', 'google']

# codes = [get_code(brand) for brand in brands]

brands_with_codes = [{brand: get_code(brand)} for brand in brands]