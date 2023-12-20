# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Dropout, Flatten, Activation
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.utils import plot_model
import numpy as np
import matplotlib.pyplot as plt

# 下載數據
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# (batch_size, 垂直尺寸, 水平尺寸, 顏色通道數)
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# 建立模型物件
model = Sequential()

# 計算準確率
model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(28,28,1)))
model.add(Conv2D(filters=64, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.fit(X_train, y_train, batch_size=128, epochs=5, verbose=1)

scores = model.evaluate(X_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])

# 將前10張圖片畫出來
for i in range(10):
  plt.subplot(2, 5, i+1)
  plt.imshow(X_test[i].reshape((28,28)), 'gray')
plt.suptitle("The first ten of the test data", fontsize=20)
plt.show()

# 顯示前10張圖片預測結果
pred = np.argmax(model.predict(X_test[0:10]), axis=1)
print(pred)