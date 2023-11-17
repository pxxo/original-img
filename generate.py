import tensorflow as tf
import gradio as gr
import matplotlib.pyplot as plt
import numpy as np

# print(tf.__version__)

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0

fig, ax = plt.subplots(nrows=2, ncols=5, figsize=(10, 10), tight_layout=True)

n = 0

# for i in range(2):
# for j in range(5):
# ax[i][j].imshow(x_train[n], cmap=plt.cm.binary)
# n += 1

# plt.show()

model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax"),
    ]
)

model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

model.summary()

model.fit(x_train, y_train, epochs=10)

predictions = model.predict(x_test)

plt.imshow(x_test[0], cmap=plt.cm.binary)

print(np.argmax(predictions[0]))

plt.show()
