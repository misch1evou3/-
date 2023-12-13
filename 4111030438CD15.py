# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.datasets import mnist
import matplotlib.pyplot as plt

#建立資料集
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#標準化資料
x_train = x_train.reshape(60000, 28, 28).astype('float32') / 255 #將60000張28*28大小的圖像標準化成三維數據且希望輸入數據為浮點數
x_test = x_test.reshape(10000, 28, 28).astype('float32') / 255
y_train = keras.utils.to_categorical(y_train , 10) #轉換成相應圖像的編碼
y_test = keras.utils.to_categorical(y_test, 10)

#建構神經網路mnist
model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=(28 , 28)), #模型輸入二維圖像數據層
    keras.layers.Dense(128, activation='relu'), #128個神經元學習提取輸入中的特徵 激活函數'relu'
    keras.layers.Dropout(0.2), #每次訓練迭代有20%神經元被隨機丟棄 減少過擬合風險
    keras.layers.Dense(10, activation='softmax')
])

#設定損失函數 優化器 評估指標
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

#訓練神經網路模型
history = model.fit(x_train, y_train, batch_size=32, epochs=10, verbose=1, validation_data=(x_test, y_test)) #batch_size每批樣本數 epochs訓練輪數 verbose顯示訓練過程中的詳細信息(此處用1顯示)

#評估訓練成果
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0], 'Test accuracy:',score[1])

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train','test'], loc='upper left')
plt.show()

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train','test'], loc='upper left')
plt.show()