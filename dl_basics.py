# Dense layer from scratch
import tensorflow as tf

class MyDenseLayer(tf.keras.layers.Layer):
    def __init__(self, input_dim, output_dim):
        super(MyDenseLayer, self).__init__()

        self.W = self.add_weight(shape=(input_dim, output_dim), initializer="random_normal", trainable=True)
        self.b = self.add_weight(shape=(output_dim,), initializer="zeros", trainable=True)
    
    def call(self, inputs):
        z = tf.matmul(inputs, self.W) + self.b
        output = tf.math.sigmoid(z)
        return output

layer = MyDenseLayer(input_dim=10, output_dim=5)
# print(layer.W.shape)
# print(layer.b.shape)

layer = tf.keras.layers.Dense(5, activation='sigmoid')
layer.build(input_shape=(10,))
# print(layer.kernel.shape)
# print(layer.bias.shape)

# RNN from scratch

class MyRNNCell(tf.keras.layers.Layer):
    def __init__(self, rnn_units, input_dim, output_dim):
        super(MyRNNCell, self).__init__()
        self.W_xh = self.add_weight(shape=(rnn_units, input_dim))
        self.W_hh = self.add_weight(shape=(rnn_units, rnn_units))
        self.W_hy = self.add_weight(shape=(output_dim, rnn_units))
        self.h = tf.zeros([rnn_units, 1])

    def call(self, x):
        self.h = tf.math.tanh(tf.matmul(self.W_hh, self.h) + tf.matmul(self.W_xh, x))
        output = tf.matmul(self.W_hy, self.h)
        return output, self.h

cell = MyRNNCell(rnn_units=10, input_dim=4, output_dim=2)
cell(tf.ones(shape=(4, 1)))
print(cell.h)
