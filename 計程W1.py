# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:48:00 2023

@author: User
"""
height=float(input("請輸入您的身高(公尺)："))
weigh=float(input("請輸入您的體重(公斤)："))
BMI= height/(weigh**2)
print(f"您的BMI是：{BMI:.2f}")