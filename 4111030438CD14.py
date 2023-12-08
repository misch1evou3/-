# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 21:46:04 2023

@author: User
"""

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_predict

data = load_breast_cancer()
dx, dy = data.data, data.target
dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size = 0.2, random_state = 0)

svm = SVC()
svm.fit(dx_train, dy_train)
predictions = svm.predict(dx_test)

print(classification_report(dy_test, predictions))
y_kfold_pred = cross_val_predict(svm, dx_std, dy, cv = 5)
print(classification_report(dy, y_kfold_pred))