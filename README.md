# Python script
* Use [Finnhub](https://finnhub.io/) free stock price API to query stock prices for specific tech stocks.

* Get the latest price for Apple, Amazon, Netflix, Facebook, Google.

* Get the latest price for Apple, Amazon, Netflix, Facebook, Google.

* Save the following information for the most_volatile_stock to a CSV file with the following rows.

* include headers in the CSV file 


# Initial settings to run the script locally
You can use any virtual enviroment tool to run this project locally. I used venv.

## Create venv
```
python3 -m venv /path/to/new/virtual/environment
```
activate venv
```
source /path/to/venv/bin/activate

```
## install requirements
Once venv is active:

```
pip3 install  -r requirements.txt
```

## env.py file
Example of env file can be found as env_example.py. This needs to be renamed to env.py and will be exempt from git version control. env.py file needs to contain api key. This can be obtained for free from [Finnhub](https://finnhub.io/)
## run script

to run script 
```
python3 run.py
```
## deactivate venv
to deactivate venv run:
```
deactivate
```


# Technologies used
venv was used for local enviroment
pycodestyle for linting


# Steps to complete task:
1. finding symbols
I started with finding the stock symbols. I made two attempts to call api and filter the answer. These attempts are in files '01_brands_symbol_search.py' and '02_all_stock_symbols_search.py'.
2. finding stock data
To complete the task of getting the stock data - I created run.py file, that calls finnhub api and saves data into csv file inside results folder. Every day the script is run it saves a new file with new data in the file name.