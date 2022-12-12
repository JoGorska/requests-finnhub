'''
as a second attempt to get stock symbols I used https://finnhub.io/docs/api/stock-symbols.
forloop returned none, but brands could be found when manually going into that url

'''

import requests
from run import API_KEY


brands = ['apple', 'amazon', 'netflix', 'facebook', 'google']
companies = ['APPLE INC', 'AMAZON.COM', 'NETFLIX INC', 'META PLATFORMS INC-CLASS', 'ALPHABET INC-CL']
codes = ['AAPL', 'AMZN', 'NFLX', '', '']


def call_api():
    token = API_KEY
    params = dict(exchange='US', currency='USD', token=token)
    r = requests.get('https://finnhub.io/api/v1/stock/symbol', params=params)

    # print(r.url)
    res = r.json()
    # comented out so it doesn't rewrite same file again
    # with open('results/02_stock-symbols.py', 'w') as f:
    #     f.write(str(res))
    return res



# def get_code(brand):
#     '''
    
#     '''

#     # list_of_results = res['result']
#     # list_of_codes = [item['symbol'] for item in list_of_results]
#     list_result = call_api()
#     for company in list_result:
#         if company['description'].lower() == brand:
#             return company['symbol']

# codes = [get_code(brand) for brand in brands]
# # print(codes) # gives none



# def all_symbols(brands):
#     # returns empty list
#     list_result = call_api()
#     symbols = []
#     for company in list_result:
#         if company['description'].lower() in brands:
#             symbols.append(company['symbol'])
#     return symbols

# def all_descriptions():
#     # returns empty list
#     list_result = call_api()
#     descriptions = []
#     for company in list_result:
#         descriptions.append(company['description'])
#     print(descriptions)
#     return descriptions
# all_descriptions()

