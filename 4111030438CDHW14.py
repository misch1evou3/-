# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 21:50:45 2023

@author: User
"""

# 匯入必要的套件
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


# 載入MNIST資料集
digits = datasets.load_digits()
X = digits.data
y = digits.target

# 資料預處理：標準化特徵
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 切分資料集為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 使用決策樹分類器建立模型
model = DecisionTreeClassifier(random_state=42)

# 在訓練集上訓練模型
model.fit(X_train, y_train)

# 在測試集上評估模型的準確性
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on the test set: {accuracy:.2f}")

# 使用K-Fold交叉驗證評估模型性能
k_fold_scores = cross_val_score(model, X_scaled, y, cv=5)
print(f"Cross-validated accuracy: {k_fold_scores.mean():.2f} (+/- {k_fold_scores.std() * 2:.2f})")

# 產生預測結果報告
cross_val_predictions = cross_val_predict(model, X_scaled, y, cv=5)
report = classification_report(y, cross_val_predictions)
print("Classification Report:")
print(report)
