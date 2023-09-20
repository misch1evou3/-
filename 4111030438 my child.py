# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:31:30 2023

@author: User
"""
books = [{"name":"book1","price":100},
         {"name":"book2","price":210},
         {"name":"book3","price":340},
         {"name":"book4","price":180}]
service = 1
while service == 1:
    choose = int(input("請輸入編號選擇您要的服務\n1.訂購書籍\n2.增加書籍\n3.退出"))
    if choose == 1:
            orders = [{"name":input("請輸入書名品項"),"quantity":input("請輸入購買數量")},]
    elif choose == 2 :
            book = input("請輸入書籍名稱")
            price = input("請輸入書籍價格")
            books.append({"name":book,"price":price})
    elif choose == 3:
            service = 0

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