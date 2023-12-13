# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 22:54:55 2023

@author: User
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 讀取數據集
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# 數據預處理
def preprocess_data(data):
    # 填充缺失值
    train_data['Age'].fillna(data['Age'].median(), inplace=True)
    train_data['Fare'].fillna(data['Fare'].median(), inplace=True)
    train_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)
    train_data['Cabin'].fillna(method='ffill', inplace=True)


    
    # 將性别映射為數字 映射函式.map()
    data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
    
    # 提取船艙等級的前缀，並映射為數字
    data['Cabin'] = data['Cabin'].apply(lambda x: str(x)[0] if pd.notnull(x) else 'N')
    cabin_mapping = {'N': 0, 'C': 1, 'E': 2, 'G': 3, 'D': 4, 'A': 5, 'B': 6, 'F': 7, 'T': 8}
    data['Cabin'] = data['Cabin'].map(cabin_mapping)
    
    # 映射登船港口為數字
    data['Embarked'] = data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
    
    # 選擇特徵
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Cabin', 'Embarked']
    X = data[features]
    
    return X

# 對訓練集和測試集進行預處理
X_train = preprocess_data(train_data)
X_test = preprocess_data(test_data)

# 標準化數據
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 創建標籤
y_train = train_data['Survived']

# 分割數據集
X_train_split, X_valid_split, y_train_split, y_valid_split = train_test_split(
    X_train_scaled, y_train, test_size=0.2, random_state=42
)

# 訓練KNN模型
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_split, y_train_split)

# 預測驗證集
y_valid_pred = knn.predict(X_valid_split)

# 計算準確率
accuracy = accuracy_score(y_valid_split, y_valid_pred)
print(f'Validation Accuracy: {accuracy}')
