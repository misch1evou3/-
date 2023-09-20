# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 17:12:31 2023

@author: User
"""
books = []
orders = []
while True:
    choose = int(input("請輸入編號選擇您要的服務\n1.訂購書籍\n2.增加書籍\n3.退出"))
    if choose == 1:
            book=input("請輸入書名品項")
            n=input("請輸入購買數量")
            orders.append({"name":book,"quantity":n})
    elif choose == 2 :
            book = input("請輸入書籍名稱")
            price = input("請輸入書籍價格")
            books.append({"name":book,"price":price})
    elif choose == 3:
            break

total_amount=0
for item in orders:
    for book in books:
        if item["name"] == book["name"]:
            total_amount+=int(book["price"])*int(item["quantity"])
            
if total_amount>1000:
    discount=0.6
    total_amount = total_amount*discount
    print(f"恭喜購滿六折折扣標準，您的購物金額為:{total_amount}")
elif total_amount>750:
    discount=0.8
    total_amount = total_amount*discount
    print(f"恭喜購滿八折折扣標準，您的購物金額為:{total_amount}")
elif total_amount>500:
    discount=0.9
    total_amount = total_amount*discount
    print(f"恭喜購滿九折折扣標準，您的購物金額為:{total_amount}")
    
else:
    print(f"您的購物金額為:{total_amount}")