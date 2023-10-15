# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:04:05 2023

@author: User
"""

class School_system():
    def __init__(self, name, code, time, professor):
        self.name = name
        self.code = code
        self.time = time
        self.professor = professor
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def display_students(self):
        student_list = [student.name for student in self.students]
        return ", ".join(student_list)

class School_student():
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []

    def enroll_course(self, course):
        self.enrolled_courses.append(course)
        course.add_student(self)

    def drop_course(self, course):
        self.enrolled_courses.remove(course)
        course.remove_student(self)

    def display_enrolled_courses(self):
        course_list = [course.name for course in self.enrolled_courses]
        return ", ".join(course_list)

    def display_student_courses(self):
        return self.display_enrolled_courses()

def main():
    school_courses = []
    school_students = []

    while True:
        print("1.教授")
        print("2.學生")
        print("3.退出")
        cho = int(input("請輸入代碼以選擇服務身分"))
        
        if cho == 1:
            while True:
                print("1.加增課程")
                print("2.列出所有課程")
                print("3.列出所有學生清單")
                print("4.查看修讀課程的學生")
                print("5.查看學生選課情況")
                print("6.列印目前所有學生的選課情況")
                print("7.退出")
                cho = int(input("請輸入代碼以選擇動作"))
                
                if cho == 1:
                    name = input("請輸入課程名字")
                    code = input("請輸入課程代碼")
                    time = input("請輸入課程時間")
                    professor = input("請輸入教授姓名")
                    school = School_system(name, code, time, professor)
                    school_courses.append(school)
                    print(f'成功新增{name}課程')
                    
                if cho == 2:
                    for course in school_courses:
                        print(f"課程名稱:{course.name}")
                        print(f"課程代碼:{course.code}")
                        print(f"課程時段:{course.time}")
                        print(f"課程教授名稱:{course.professor}")
                        
                if cho == 3:
                    for student in school_students:
                        print(f"學生姓名: {student.name}, 學號: {student.student_id}")
                        
                if cho == 4:
                    course_name = input("請輸入課程名字或代碼以查看學生修習課程")
                    for course in school_courses:
                        if course_name == course.name or course_name == course.code:
                            students_in_course = course.display_students()
                            print(f"修讀 {course.name} 課程的學生: {students_in_course}")
                            break
                    else:
                        print("查無此課程名稱或課程代碼")
                        
                if cho == 5:
                    student_courses = student.display_student_courses()
                    print(f"{student.name} 選修的課程: {student_courses}")
                    
                if cho == 6:
                    for s in school_students:
                        student_courses = s.display_student_courses()
                        print(f"{s.name} 選修的課程: {student_courses}")
                        
                if cho == 7:
                    print("成功退出教授身分")
                    break
        
        if cho == 2:
            real_name = input("請輸入姓名")
            student_id = int(input("請輸入學號"))
            student = School_student(real_name, student_id)
            school_students.append(student)
            
            while True:
                print("1.加選")
                print("2.退選")
                print("3.列出已選課程")
                print("4.列出所有課程")
                print("5.退出")
                cho = int(input("請輸入代碼以選擇動作"))
                
                if cho == 1:
                    search = input("請輸入課程名字或課程代碼")
                    for course in school_courses:
                        if search == course.name or search == course.code:
                            student.enroll_course(course)
                            print(f"{student.name} 成功加選 {course.name}")
                            break
                    else:
                        print("查無此課堂名稱或課堂代碼")
                    
                if cho == 2:
                    search = input("請輸入課程名字或課程代碼")
                    for course in student.enrolled_courses:
                        if search == course.name or search == course.code:
                            student.drop_course(course)
                            print(f"{student.name} 成功退選 {course.name}")
                            break
                    else:
                        print("查無此課堂名稱或課堂代碼")
                    
                if cho == 3:
                    enrolled_courses = student.display_enrolled_courses()
                    print(f"{student.name} 已選修的課程: {enrolled_courses}")
                    
                if cho == 4:
                    for course in school_courses:
                        print(f"課程名稱:{course.name}")
                        print(f"課程代碼:{course.code}")
                        print(f"課程時段:{course.time}")
                        print(f"課程教授名稱:{course.professor}")
                    
                if cho == 5:
                    print("成功退出學生身分")
                    break
        
        if cho == 3:
            print("感謝使用本服務")
            break

if __name__ == "__main__":
    main()
