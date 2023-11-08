# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:58:54 2023

@author: User
"""

from random import randint

menu = {1:'咖哩飯', 2:'麻醬麵', 3:'滷肉飯', 4:'招牌炒飯', 5:'古早味乾麵'}
price = {1:79, 2:50, 3:30, 4:65, 5:55}

print("以下是菜單")
print("--------------------------")
for i in menu.items():
    print(i[0],'. ',i[1],': ',price[i[0]],'元')
print("--------------------------")

print("現在可以進行活動~")
computer = ['剪刀', '石頭', '布']
discount = 1
pick = randint(0, 2)
guess = input("請輸入剪刀, 石頭, 布:")
print("店員出",{computer[pick]})

if computer[pick] == guess:
    discount = 0.9
    print("平手")
elif (computer[pick] == '剪刀' and guess == '布') or (computer[pick] == '石頭' and guess == '剪刀') or (computer[pick] == '布' and guess == '石頭'):
    print("你輸了~")
else:
    discount = 0.5
    print("你贏了~")
    
print("以下是您的消費明細")
print("--------------------------")
order = 0
for i in range(5):
    num = randint(0, 10)
    print(i + 1,'. ',menu[i + 1],' *',num,' ',price[i + 1],'元')
    order += num * price[i + 1]

if discount != 1:
    print(f"打{int(discount * 10)}折後, 總金額為{int(order * discount)}")
else:
    print(f"總金額為{int(order * discount)}")