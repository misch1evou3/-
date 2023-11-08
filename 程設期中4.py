# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:41:07 2023

@author: User
"""

def high_scores_student(students):
    high_score = []
    for key, value in students.items():
        if len([score for score in value if score > 80]) >= 2:
            high_score.append(key[1])
    return high_score

def main():
    times = int(input("請輸入學生數量: "))
    student_dict = {}
    for i in range(times):
        student_ID = input("請輸入學號: ")
        student_name = input("請輸入姓名: ")
        chinese_score = int(input("請輸入國文成績: "))
        englsih_score = int(input("請輸入英文成績: "))
        math_score = int(input("請輸入數學成績: "))
        nature_score = int(input("請輸入自然成績: "))
        social_score = int(input("請輸入社會成績: "))
        student_dict[(student_ID, student_name)] = [chinese_score, englsih_score, math_score, nature_score, social_score]
    return student_dict

if __name__ == "__main__":
    student_info = main()
    result = high_scores_student(student_info)
    print(result)
