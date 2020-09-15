import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

def get_tickers(names):
    return names

def LSTM_model( num_units ):
  model = Sequential()
  model.add(LSTM(units= num_units,return_sequences=True,input_shape=(train_features.shape[1],1)))
  model.add(Dropout(0.2))

  #layer -2
  model.add(LSTM(units=num_units,return_sequences=True))
  model.add(Dropout(0.2))

  #layer -3
  model.add(LSTM(units=num_units,return_sequences=True))
  model.add(Dropout(0.2))

  #layer -4
  model.add(LSTM(units= num_units,return_sequences=True))
  model.add(Dropout(0.2))

  #layer -6
  model.add(LSTM(units= num_units,return_sequences=True))
  model.add(Dropout(0.2))

  #layer -6
  model.add(LSTM(units= num_units,return_sequences=True))
  model.add(Dropout(0.2))

  #layer -7
  model.add(LSTM(units=num_units))
  model.add(Dropout(0.2))

  model.add(Dense(units = 7))
  return model

if __name__ == "__main__" :

    ticker = fire.Fire(get_tickers)
    
    train_features = np.array(np.load(f'train_features_{ticker}.npy', allow_pickle = True).tolist())
    train_labels = np.array(np.load(f'train_labels_{ticker}.npy', allow_pickle = True).tolist())

    num_units = 100 #number of neurons in each layer
    
    model = LSTM_model(num_units)
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(train_features, train_labels, epochs=50, batch_size=64, verbose =2)
    model.save(f"models/trained_model_{ticker}")
    
