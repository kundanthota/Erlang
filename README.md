# stock_prediction

This project is only for educational purpose, not for real use and the results are accurate but not exact. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install necessary packages

## Install Vitaulenv 
```bash
pip install virtualenv
```
## Create a project environment 
```bash
virtualenv -python = path/to/python3.6 virtualenv_name
```
## Install packages 
windows: 
```bash
virtualenv_name/Scripts/pip install -r requirements.txt
```

Linux: 
```bash
virtualenv_name/bin/pip install -r requirements.txt
```
## Example jobs

```bash
path/to/venv/python fetch_assets.py ticker_name
```
```bash
path/to/venv/python normalize_prices.py ticker_name
```
```bash
path/to/venv/python test_train_split.py ticker_name
```
```bash
path/to/venv/python train.py ticker_name
```
```bash
path/to/venv/python test.py ticker_name
```
## Here are some results on three tickers  Google(GOOG), Facebook(FB), Amazon(AMZN)
 
 ![alt text](https://raw.githubusercontent.com/kundanthota/stock_prediction/master/GOOGLE.png)
 
 ![alt text](https://raw.githubusercontent.com/kundanthota/stock_prediction/master/FACEBOOK.png)
 
 ![alt text](https://raw.githubusercontent.com/kundanthota/stock_prediction/master/AMAZON.png)
