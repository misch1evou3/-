# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 17:06:13 2023

@author: User
"""

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = {}

class Gradebook:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def add_score(self, student, subject, score):
        try:
            student.scores[subject] = score
        except KeyError:
            raise ValueError("成績有缺少")

    def average(self, subject):
        total = 0
        count = 0
        for student in self.student_list:
            if subject in student.scores:
                total += student.scores[subject]
                count += 1
        if count == 0:
            raise ValueError("成績有缺少")
        return total / count
