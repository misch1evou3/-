# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 20:20:44 2023

@author: User
"""

books = []

def add_book():
    book_name = input("請輸入書籍名稱: ")
    book_price = input("請輸入書籍價格: ")
    quantity = int(input("請輸入書籍數量: "))
    books.append({"書名": book_name, "金額": book_price ,"數量": quantity})
    print(f"{book_name} 已經新增到庫存中。")

def remove_book():
    book_name = input("請輸入要移除的書籍名稱: ")
    for item in books:
        if item["書名"] == book_name:
            books.remove(item)
            print(f"{book_name} 已經從庫存中移除。")
            break
    else:
        print(f"{book_name} 未找到於庫存中。")

def update_book():
    book_name = input("請輸入要更新的書籍名稱: ")
    quantity = int(input("請輸入新的庫存數量: "))
    for item in books:
        if item["書名"] == book_name:
            item["數量"] = quantity
            print(f"{book_name} 的庫存已更新為 {quantity}。")
            break
    else:
        print(f"{book_name} 未找到於庫存中。")
        
def show_books():
    print("庫存清單:")
    for item in books:
        print(f"書名: {item['書名']}, 金額: {item['金額']} ,數量: {item['數量']}")
    
while True:
    print("1.添加書籍")
    print("2.刪除書籍")
    print("3.更新書籍")
    print("4.顯示庫存")
    print("5.退出")
    cho = int(input("請輸入代碼以選擇服務項目(1/2/3/4/5)"))
    if cho == 1:
        add_book()
    elif cho == 2:
        remove_book()
    elif cho == 3:
        update_book()
    elif cho == 4:
        show_books()
    elif cho == 5:
        print("感謝您使用書籍庫存管理系統!")
        break
    else:
        print("輸入了無效的選項")  