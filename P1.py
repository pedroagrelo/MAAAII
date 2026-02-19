import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist

(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

print("Train:", X_train.shape)
print("Test:", X_test.shape)

#Vamos a trabajar con el conjunto de test
print(X_test.shape)
print(y_test.shape)
print(X_test.dtype)