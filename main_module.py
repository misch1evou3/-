# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:33:10 2023

@author: User
"""
import inventory_module as im

def main():
    while True:
        cho = int(input("請輸入編碼以選取服務項目"))
        print("1.新增物品")
        print("2.移除物品")
        print("3.查看庫存")
        print("4.退出")
        if cho == 1:
            name = input("請輸入物品名稱")
            quantity = int(input("請輸入數量"))
            im.add_item(name,quantity)
            print(f"已成功新增{quantity}個{name}")
        if cho == 2:
            name = input("請輸入物品名稱")
            quantity = int(input("請輸入數量"))
            im.remove_item(name,quantity)
            print(f"已成功刪除{quantity}個{name}")
        if cho == 3:
            im.show_item(name,quantity)
        if cho == 4:
            print("感謝使用本服務")
            break        
if __name__ == "__main__":
    main()
        

    
            
                
                            
