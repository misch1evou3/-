# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#購買單一書籍
class purchaseable:
    def purchase(self, quantity, unit_price ):
        total_cost = quantity * unit_price
        return total_cost
    
#計算消費金額
class spendable:
    def spend(self, purchases):
        total_spend = sum(purchases)
        return total_spend
        
class discountable:
    def discount(self, price, discount):
        discount_price = price * (1-discount/100)
        return discount_price
    
class book(purchaseable, spendable, discountable):
    def __init__(self, isbn, name, author, price):
        self.isbn = isbn
        self.name = name
        self.author = author
        self.price = price
        
class book1(book):
    def __init__(self, isbn, name, author, price, stock):
        super().__init__(isbn, name, author, price)
        self.stock = stock
        
#顯示書籍資訊函數    
    def display_info(self):
        return f"Name:{self.name}, Author:{self.author}, Price: ${self.price}"
        
isbn = input("請輸入ISBN編號")
name = input("請輸入書名")
author = input("請輸入書籍作者")
price = float(input("請輸入書籍金額"))
stock = int(input("請輸入庫存數量"))
quantity = int(input("請輸入購買數量"))
discount = int(input("請輸入折扣百分比"))

#建立書籍
book = book1(isbn, name, author, price, stock)

#購買書籍
unit_price = book.price
total_cost = book.purchase(quantity, unit_price)

#總共消費金額
purchases = [total_cost]
total_spend = book.spend(purchases)

#計算折扣金額
discount_price = book.discount(book.price, discount)

print("購買成功!")

#顯示書籍資訊
print("書籍資訊:")
print(book.display_info())

print(f"購買數量:{quantity}")

#顯示消費金額
print(f"總消費金額: {total_spend}")

#顯示折扣後金額
print(f"折扣後價格: {discount_price}")

#更新後庫存數量
stock -= quantity
print(f"更新後庫存數量:{stock}")



        