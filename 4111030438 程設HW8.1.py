# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 17:00:43 2023

@author: User
"""

def sum_values_in_dicts(dict1, dict2):
    result = {}
    for key in dict1:
        if key in dict2:
            result[key] = dict1[key] + dict2[key]
    return result

dict1 = {'a': 5, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'a': 10, 'b': 3, 'e': 5, 'f': 7}

output = sum_values_in_dicts(dict1, dict2)
print(output)
