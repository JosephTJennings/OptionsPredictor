import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from keras.callbacks import EarlyStopping


def predictRNN(filename):
    df = pd.read_csv(filename)

    # [0, 3, 4, 5, 6, 7, 8, 9, 10]
    X = df.iloc[:, [0, 5, 6, 7, 8, 9, 10]].values
    y = df.iloc[:, [1]].values

    # Scale the data
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)

    # Reshape the data to 3D for LSTM
    X = np.reshape(X, (X.shape[0], 1, X.shape[1]))

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, shuffle=False)

    # Build the model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Define early stopping
    # early_stop = EarlyStopping(monitor='val_loss', patience=10)

    # Fit the model
    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

    # Make predictions
    y_pred = model.predict(X_test)
    y_pred = (y_pred > 0.5)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)

    # Print scores
    print(f'!! Scores for {filename}:')
    print(f'Accuracy: {accuracy:.2f}\n')



if __name__ == "__main__":
    predictRNN('./AAPL_main.csv')
    predictRNN('./AAPL_calls.csv')
    predictRNN('./AAPL_puts.csv')
