# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:05:43 2023

@author: User
"""
#inventory_module.py

inventory = {}

def add_item(name,quantity):
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity
        
def remove_item(name,quantity):
    if name in inventory and inventory[name] >= quantity:
        inventory[name] -= quantity
        if inventory[name] == 0:
            del inventory[name]
    else:
        print("庫存不足或查無此庫存")
        
def show_item(name,quantity):
    for item, quantity in inventory.items():
        print(f"書名：{name}\n庫存：{quantity}")
        