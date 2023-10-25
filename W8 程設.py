# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = [10, 15, 21, 28, 33, 40]
b = [10, 40, 30 ,20 ,50]
c = [['Justin', 89, 90, 100],
     ['Tom', 92, 87, 100],
     ['Jane', 90, 90, 100],
     ['Philip', 89, 95, 100]
]
d = {'a':5, 'b':1, 'c':3, 'd':4, 'e':2}
e = {1:'apple', 2:'orange', 3:'pineapple', 4:'watermelon'}

def remove_odd_num():
    result = [x for x in a if x % 2 == 0]
    return result

def sec_maximum():
    nb = sorted(b)
    result = nb[3]
    return result

def avg_maximum(scores):
    highest_avg = 0
    
    for student in scores:
        score = student[1:]
        avg_score = sum(score) / len(score)
        
        if avg_score > highest_avg:
            highest_avg = avg_score
            
    return highest_avg

def three_key():
    sort_value = sorted(d.items(), key = lambda x:x[1])
    result = [sort_value[4], sort_value[3], sort_value[2]]
    return result
        
def element_deletion(strings: dict):
    return {key:value for key, value in strings.items() if len(value) >= 6}
    
    
print(remove_odd_num())
print(sec_maximum())
print(avg_maximum(c))
print(three_key())
print(element_deletion({1:'apple', 2:'orange', 3:'pineapple', 4:'watermelon'}))