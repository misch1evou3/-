# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:41:04 2023

@author: User
"""

class Product:
    def __init__(self, product_id, product_name, unit_price, stock_quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.unit_price = unit_price
        self.stock_quantity = stock_quantity

    def sell(self, quantity):
        if quantity <= self.stock_quantity:
            self.stock_quantity -= quantity
            total_price = self.unit_price * quantity
            if total_price > 1000:
                discounted_price = total_price * 0.8
            elif total_price > 500:
                discounted_price = total_price * 0.9
            else:
                discounted_price = total_price
            print(f"總價: ${total_price}, 打折後價格: ${discounted_price}")
        else:
            print("庫存不足")


products = {}

while True:
    print("操作選項:")
    print("1: 添加新產品")
    print("2: 銷售")
    print("3: 查詢庫存")
    print("4: 退出程式")

    choice = input("請輸入操作編號: ")

    if choice == "1":
        product_id = input("輸入產品編號: ")
        product_name = input("輸入產品名稱: ")
        unit_price = float(input("輸入單價: "))
        stock_quantity = int(input("輸入初始庫存數量: "))
        new_product = Product(product_id, product_name, unit_price, stock_quantity)
        products[product_id] = new_product
        print("產品已添加到字典中")

    elif choice == "2":
        product_id = input("輸入產品編號: ")
        if product_id in products:
            quantity = int(input("輸入銷售數量: "))
            print(f"成功銷售{quantity}單位的{product_name}")
            products[product_id].sell(quantity)
        else:
            print("找不到該產品編號")

    elif choice == "3":
        product_id = input("輸入產品編號: ")
        if product_id in products:
            product = products[product_id]
            print(f"產品編號: {product.product_id}")
            print(f"產品名稱: {product.product_name}")
            print(f"單價: {product.unit_price}")
            print(f"庫存數量: {product.stock_quantity}")
        else:
            print("找不到該產品編號")

    elif choice == "4":
        print("程式已退出")
        break

    else:
        print("輸入無效，請重新輸入")


