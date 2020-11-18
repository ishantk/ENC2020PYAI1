import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model('covid_cnn_model')
# model = tf.keras.models.load_model('covid_cnn_model.h5')
print(model.summary())


# image1 = cv2.imread("covid19dataset/test/covid/radiol.2020200490.fig3.jpeg")
# image2 = cv2.imread("covid19dataset/test/normal/NORMAL2-IM-1412-0001.jpeg")
#
# image1 = cv2.resize(image1, (64, 64))
# image1 = np.reshape(image1, [1, 64, 64, 3])
#
# image2 = cv2.resize(image2, (64, 64))
# image2 = np.reshape(image2, [1, 64, 64, 3])
#
# predicted_class1 = model.predict_classes(image1)
# predicted_class2 = model.predict_classes(image2)
# print(predicted_class1)
# print(predicted_class2)
#
# labels = ["NORMAL", "COVID"]
# print(labels[predicted_class1[0][0]])
# print(labels[predicted_class2[0][0]])


# Assignment:
# In Session 73A -> Directly Use the Trained Model to make predictions
