import tensorflow as tf
import gradio as gr
import matplotlib.pyplot as plt

# print(tf.__version__)

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0

fig, ax = plt.subplots(nrows=2, ncols=5, figsize=(10, 10), tight_layout=True)

n = 0
for i in range(2):
    for j in range(5):
        ax[i][j].imshow(x_train[n], cmap=plt.cm.binary)
        n += 1
