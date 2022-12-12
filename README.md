# Python script
* Use https://finnhub.io/ free stock price API to query stock prices for specific tech stocks.

* Get the latest price for Apple, Amazon, Netflix, Facebook, Google.

* Get the latest price for Apple, Amazon, Netflix, Facebook, Google.

* Save the following information for the most_volatile_stock to a CSV file with the following rows.

* include headers in the CSV file 

# Initial settings
You can use any virtual enviroment tool to run this project locally. I used venv.

create venv
```
python3 -m venv /path/to/new/virtual/environment
```
activate venv
```
source /path/to/venv/bin/activate

```
Once venv is active:

```
pip3 install  -r requirements.txt
```
You need to create env.py file and add API_KEY obtained from https://finnhub.io/
to run program 
```
python3 run.py
```

```
to deactivate venv run:
```
deactivate
```


# Technologies used
venv was used for local enviroment
pycodestyle for linting

# steps to complete task:

I started with finding the stock symbols. I made two attempts to call api and filter the answer. These attempts are in files '01_brands_symbol_search.py' and '02_all_stock_symbols_search.py'.

To complete the task of getting the stock data - I created run.py file. 