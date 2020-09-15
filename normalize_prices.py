import pandas as pd
from sklearn import preprocessing
import fire

def get_tickers(names):
    return names

if __name__ == "__main__" : 
    ticker = fire.Fire(get_tickers)
    data = pd.read_csv(f'data/ticker_price_{ticker}.csv')
    data = data[data.columns[1:]]
    scaler = preprocessing.MinMaxScaler(feature_range = (0,1))
    scaled_data = pd.DataFrame(scaler.fit_transform(data[data.columns]), columns = data.columns)
    scaled_data.to_csv(f'data/normalized_prices_{ticker}.csv', index = False)