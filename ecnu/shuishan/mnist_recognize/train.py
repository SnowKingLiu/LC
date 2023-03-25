# by:Snowkingliu
# 2023/3/24 16:09
from keras import Sequential
from keras.optimizers import Adam
from tensorflow import keras
from keras.layers import Reshape, Conv2D, MaxPooling2D, Flatten, Dense
import numpy as np


(x_train_data, y_train_num), (
    x_test_data,
    y_test_num,
) = keras.datasets.mnist.load_data()

x_train = np.where(x_train_data > 127, 1, 0)
x_test = np.where(x_test_data > 127, 1, 0)
y_train = keras.utils.to_categorical(y_train_num)
y_test = keras.utils.to_categorical(y_test_num)

model = Sequential()
# model.add(Reshape((28, 28, 1), input_shape=(28, 28)))
model.add(Conv2D(64, (3, 3), input_shape=(28, 28, 1), activation="relu"))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation="relu"))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dense(10, activation="softmax"))

model.compile(optimizer="adam", loss=keras.losses.categorical_hinge)

model.fit(x_train, y_train, batch_size=1000, epochs=10)
# model.fit(x_train, y_train, epochs=1, validation_data=(x_test, y_test))
res = model.predict(x_test)
res_num = np.argmax(res, axis=1)
print(sum(np.where(res_num - y_test_num == 0, 1, 0)) / res_num.shape[0])
