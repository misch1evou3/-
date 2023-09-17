# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 13:58:54 2023

@author: User
"""

def circle_calculator():
    radius = float(input("請輸入圓半徑: "))
    area1 = 3.1415926 *radius **2
    perimeter1 = 3.1415926 *radius *2
    print(f"所求圓周長為: {perimeter1}\n所求圓面積為: {area1}")
def rectangle_calculator():
    length = float(input("請輸入矩形長度:"))
    width = float(input("請輸入矩形寬度:"))
    area2 = length *width
    perimeter2 = (length+width) *2
    print(f"所求矩形面積為:{area2}\n所求矩形周長為:{perimeter2}")
def triangle_calculator():
    side1 = float(input("請輸入三角形第一個邊長"))
    side2 = float(input("請輸入三角形第二個邊長"))
    side3 = float(input("請輸入三角形最後一個邊長"))
    perimeter3 = side1+side2+side3
    s = perimeter3/2
    area3 = (s *(s-side1) *(s-side2) *(s-side3)) **0.5
    if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
        print(f"所求三角形面積為:{area3}\n所求三角形周長為:{perimeter3}")
    else:
        print("您所輸入的三邊長不符合三角形定理")
def main(value = True):
    while value == True:
        choice = int(input("請輸入代號以選擇您需要的功能\n1. 圓形計算機\n2. 矩形計算機\n3. 三角形計算機\n4. 退出此功能"))
        if choice == 1:
            circle_calculator()
        elif choice == 2:
            rectangle_calculator()
        elif choice == 3:
            triangle_calculator()
        elif choice == 4:
            value = False
        else:
            print("無效指令，請重新輸入")
main()