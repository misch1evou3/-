# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 22:01:05 2023

@author: User
"""

class Book():
    def __init__(self, name, isbn, author, date, price, stock):
        self.name = name
        self.isbn = isbn
        self.author = author
        self.date = date
        self.price = price
        self.stock = stock    
        
class Bookstore():
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def show_book(self):
        for book in self.books:
            print(f"書名:{book.name}")
            print(f"ISBN編號:{book.isbn}")
            print(f"作者:{book.author}")
            print(f"出版日期:{book.date}")
            print(f"出版商:{book.price}")
            print(f"庫存:{book.stock}")
            
    def total_price(self, cart):
        total_price = 0
        for item in cart:
            book, quantity = item
            total_price += book.price * quantity
        return total_price
            
    def discount(self, price, discount):
        discount_price = price * (1 - discount / 100)
        return discount_price
    
    def buy_book(self, book, quantity):
        if book in self.books:
            if book.stock >= quantity:
                book.stock -= quantity
                return True
            else:
                print("庫存不足")
                return False
        else:
            print("書籍不存在")
            return False
       
    def display_cart(self, cart):
        for book, quantity in cart:
            print(f"書籍資訊: {book.name}, 購買數量: {quantity}")
            
    
def main():
    bookstore = Bookstore()  # 实例化 Bookstore 类
    cart = []
       
    while True:
        print("1.店家使用者")
        print("2.買家使用者")
        print("3.退出")
        cho = int(input("請輸入身分選擇服務項目"))
        if cho == 1:
            while True:
                title = input("已進入店家使用者模式(如欲新增書籍請輸入 '繼續' \n如欲結束新增書籍則請輸入 '結束' )")
                if title == '結束':
                    break
                elif title == '繼續':
                    name = input("請輸入書名")            
                    isbn = input("請輸入ISBN編號")
                    author = input("請輸入書籍作者")
                    date = int(input("請輸入出版日期\n(舉例：20180304)"))
                    price = float(input("請輸入書籍金額"))
                    stock = int(input("請輸入庫存數量"))
                    new_book = Book(name, isbn, author, date, price, stock)
                    bookstore.add_book(new_book)
                else:
                    print("無效的輸入，請輸入 '繼續' 或 '結束'")
            discount = int(input("請輸入折扣百分比(整數)"))
            print("當前庫存書籍資訊:")
            bookstore.show_book()
            print(f"設定折扣百分比為:{discount}")
        if cho == 2:
            while True:
                title = input("已進入買家使用者模式(如欲新增書籍購物車請輸入 '繼續' \n如欲結束新增書籍購物車則請輸入 '結束' )")
                if title == '結束':
                    break
                elif title == '繼續':
                    search = input("請輸入書名或ISBN編號")
                    for book in bookstore.books:
                        if book.name == search or book.isbn == search:
                            quantity = int(input("請輸入購買數量"))
                            if bookstore.buy_book(book, quantity):
                                cart.append((book, quantity))
                                print("購買成功!")
                                break
                    else:
                        print("書籍不存在")
                else:
                    print("無效的輸入，請輸入 '繼續' 或 '結束'")
            print("購買成功!")
            print("書籍購買資訊如下:")
            bookstore.display_cart(cart)
            total_price = bookstore.total_price(cart)
            discount_price = bookstore.discount(total_price, discount)
            print(f"消費總金額:{total_price}")
            print(f"折扣後金額:{discount_price}")
            print("更新後庫存如下:")
            bookstore.show_book()
        if cho == 3:
            print("感謝使用本服務!")
            break

if __name__ == "__main__":
    main()         
                
                
                
                
                    
                
                
           
            


                                  

        