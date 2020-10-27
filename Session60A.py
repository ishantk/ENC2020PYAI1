import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

A = tf.constant([[1.0, 2.0], [3.0, 4.0]])
B = tf.constant([[5.0, 6.0], [7.0, 8.0]])

print(A)
print(B)

C = tf.matmul(A, B)
print(C)

X = tf.constant([1, 2, 3, 4, 5])
Y = tf.constant([6, 7, 8, 9, 10])

Z = tf.multiply(A, B)
print(Z)

# Assignment: Explore more of matrix APIs in Tensorflow

