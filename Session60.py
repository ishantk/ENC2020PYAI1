"""
    TensorFlow
"""

import tensorflow as tf
import os
# A workaround -> you may or may not need it
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # in order to fix some warning messages from tensorflow library

print(tf.__version__)

hello = tf.constant("Hello World of Tensorflow")
print(hello)