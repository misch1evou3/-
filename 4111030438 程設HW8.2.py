# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 17:04:56 2023

@author: User
"""

def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

input_string = "hello world"
output = count_characters(input_string)
print(output)
