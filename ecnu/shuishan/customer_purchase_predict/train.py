# by:Snowkingliu
# 2023/3/23 17:13
import numpy as np
import pandas as pd

from tensorflow import keras

train_df = pd.read_csv("input/train.csv")
keys = train_df.keys()
x_train = train_df[[k for k in keys if "var" in k]].to_numpy()
y_train = train_df.target.to_numpy(dtype=np.float32)

test_df = pd.read_csv("input/test.csv")
x_test = test_df[[k for k in test_df.keys() if "var" in k]].to_numpy()


model = keras.models.Sequential()
model.add(keras.layers.Dense(units=1, input_dim=200, activation="sigmoid"))
model.compile(
    optimizer=keras.optimizers.Adam(0.01),
    loss="binary_crossentropy",
    metrics=["binary_accuracy"],
)

model.fit(x_train, y_train, epochs=100)

res = model.predict(x_test)
result = "\n".join(["1" if r[0] > 0.5 else "0" for r in res])
print(result)
