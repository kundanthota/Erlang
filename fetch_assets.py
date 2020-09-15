import yfinance as yf
import fire

def get_tickers(names):
    return names

if __name__ == "__main__" :
    ticker = fire.Fire(get_tickers)
    data = yf.download(ticker, start="2015-01-01")
    data = data['Close']
    data.to_csv(f'data/ticker_price_{ticker}.csv')


#scaler.inverse_transform(scaled_data)