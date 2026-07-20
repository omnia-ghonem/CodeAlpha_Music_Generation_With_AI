from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def build_model(input_shape, output_size):

    model = Sequential()

    model.add(LSTM(256,
                   input_shape=input_shape,
                   return_sequences=True))

    model.add(Dropout(0.3))

    model.add(LSTM(256))

    model.add(Dense(128, activation="relu"))

    model.add(Dropout(0.3))

    model.add(Dense(output_size, activation="softmax"))

    model.compile(
        loss="sparse_categorical_crossentropy",
        optimizer="adam",
        metrics=["accuracy"]
    )

    return model