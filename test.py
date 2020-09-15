import keras

import fire

def get_tickers(names):
    return names

if __name__ == "__main__" :
    
    ticker = fire.Fire(get_tickers)
    data = pd.read_csv(f'data/ticker_price_{ticker}.csv')
    data = data[data.columns[1:]]
    scaler = preprocessing.MinMaxScaler(feature_range = (0,1))
    data = scaler.fit_transform(data[data.columns])
     
    model = keras.models.load_model(f"trained_model_{ticker}")

    test_features =  np.array(np.load(f'test_features_{ticker}.npy', allow_pickle = True).tolist())
    test_labels =  np.array(np.load(f'test_labels_{ticker}.npy', allow_pickle = True).tolist())

    predicted_labels = model.predict(test_features)

    predicted_labels = scaler.inverse_transform(predicted_labels)

    np.array(predicted_labels, dtype=object).dump(f'data/predicted_labels_{ticker}.npy') 