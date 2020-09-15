import numpy as np
import pandas as pd
import fire

def get_tickers(names):
    return names

if __name__ == "__main__" :
    ticker = fire.Fire(get_tickers)
    data = pd.read_csv(f'data/normalized_prices_{ticker}.csv')
    data = np.array(data)
    train_data = data[:-57]
    test_data = data[-57:]

    train_features = []
    train_labels = []
    sequence_length = 50
    for index in range(sequence_length,len(train_data)-7):
        train_features.append(train_data[index-sequence_length:index])
        train_labels.append(list(train_data[index : index+7]))

    test_features =  np.array(test_data[:50])
    test_features = test_features.reshape(1,len(test_features),1)
    test_labels = np.array(test_data[50:])
    test_labels = test_labels.reshape(1,len(test_labels),1)
    
    np.array(train_features,dtype=object).dump(f'data/train_features_{ticker}.npy')
    np.array(train_labels, dtype=object).dump(f'data/train_labels_{ticker}.npy')
    np.array(test_features, dtype=object).dump(f'data/test_features_{ticker}.npy')
    np.array(test_labels, dtype=object).dump(f'data/test_labels_{ticker}.npy')