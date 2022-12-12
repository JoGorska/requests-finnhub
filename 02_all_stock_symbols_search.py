import requests
from run import API_KEY

# # find latest price
brands = ['apple', 'amazon', 'netflix', 'facebook', 'google']
companies = ['APPLE INC', 'AMAZON.COM', 'NETFLIX INC', 'META PLATFORMS INC-CLASS', 'ALPHABET INC-CL']
codes = ['AAPL', 'AMZN', 'NFLX', '', '']

# todo - file too long - save it into a file?

def call_api():
    token = API_KEY
    params = dict(exchange='US', currency='USD', token=token)
    r = requests.get('https://finnhub.io/api/v1/stock/symbol', params=params)
    r = requests.get(f'https://finnhub.io/api/v1/stock/symbol?exchange=US&token={API_KEY}')
    # print(r.url)
    res = r.json()
    return res
# call_api()

def get_code(brand):
    '''
    https://finnhub.io/docs/api/stock-symbols
    '''

    # list_of_results = res['result']
    # list_of_codes = [item['symbol'] for item in list_of_results]
    list_result = call_api()
    for company in list_result:
        if company['description'].lower() == brand:
            return company['symbol']

codes = [get_code(brand) for brand in brands]
# print(codes) # gives none



def all_symbols(brands):
    # returns empty list
    list_result = call_api()
    symbols = []
    for company in list_result:
        if company['description'].lower() in brands:
            symbols.append(company['symbol'])
    return symbols

def all_descriptions():
    # returns empty list
    list_result = call_api()
    descriptions = []
    for company in list_result:
        descriptions.append(company['description'])
    print(descriptions)
    return descriptions
all_descriptions()

