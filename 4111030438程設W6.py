# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:51:27 2023

@author: User
"""

class School_system():
    def __init__(self, name, code, time, professor):
        self.name = name
        self.code = code
        self.time = time
        self.professor = professor        

class School_student():
    def __init__(self):
        self.table = []
        self.new_class = []

    def add_table(self, school_system):
        self.table.append(school_system)

    def add_course(self, search):
        found = False
        for course in self.table:
            if search == course.name or search == course.code:
                self.new_class.append(course)
                found = True
                break
        if not found:
            print("查無此課堂名稱或課堂代碼")

    def drop_class(self, search):
        found = False
        for course in self.new_class:
            if search == course.name or search == course.code:
                self.new_class.remove(course)
                found = True
                break
        if not found:
            print("查無此課堂名稱或課堂代碼")

    def display_table(self):
        for course in self.table:
            print(f"所選課程名稱:{course.name}")
            print(f"所選課程代碼:{course.code}")
            print(f"所選課程時段:{course.time}")
            print(f"所選課程教授名稱:{course.professor}")

def main():
    school_student = School_student()
    

    while True:
        print("1.教授")
        print("2.學生")
        print("3.退出")
        cho = int(input("請輸入代碼以選擇服務身分"))
        if cho == 1:
            name = input("請輸入課程名字")
            code = input("請輸入課程代碼")
            time = input("請輸入課程時間")
            professor = input("請輸入教授姓名")
            school = School_system(name, code, time, professor)
            school_student.add_table(school)
        if cho == 2:
            real_name = input("請輸入姓名")
            student_id = int(input("請輸入學號"))
            if real_name != "allen" or student_id != 4111030438:
                print("並非核可的學生使用者")
            else:
                print("成功驗證學生身分")
                while True:
                    print("1.加選")
                    print("2.退選")
                    print("3.退出")
                    cho = int(input("請輸入代碼以選擇動作"))
                    if cho == 1:
                        search = input("請輸入課程名字或課程代碼")
                        school_student.add_course(search)
                    if cho == 2:
                        search = input("請輸入課程名字或課程代碼")
                        school_student.drop_class(search)
                    if cho == 3:
                        print("成功退出學生身分")
                        break
        if cho == 3:
            print("感謝使用本服務")
            break

if __name__ == "__main__":
    main()

        