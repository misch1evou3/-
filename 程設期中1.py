# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:29:00 2023

@author: User
"""

def create_tuple():
    arr = []
    while True:
        num = int(input())
        if num != -9999:
            arr.append(num)
        else:
            break
    return tuple(arr)

print("create tuple1:")
tuple1 = create_tuple()
print("create tuple2:")
tuple2 = create_tuple()

combined_tuple = tuple1 + tuple2
combined_list = list(combined_tuple)

print(f"combined tuple before sorting: {combined_tuple}")
combined_list.sort()
print(f"combined list after sorting: {combined_list}")
