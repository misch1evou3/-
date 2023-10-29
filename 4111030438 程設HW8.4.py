# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 17:06:34 2023

@author: User
"""

class Employee:
    def __init__(self, employee_id, name):
        self.id = employee_id
        self.name = name

    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, salary):
        super().__init__(employee_id, name)
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self, employee_id, name, hourly_wage):
        super().__init__(employee_id, name)
        self.hourly_wage = hourly_wage
        self.hours_worked = 0

    def set_hours_worked(self, hours):
        assert hours > 0, "工作時數必須大於0"
        self.hours_worked = hours

    def calculate_salary(self):
        return self.hourly_wage * self.hours_worked

class Intern(Employee):
    def __init__(self, employee_id, name, stipend):
        super().__init__(employee_id, name)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend

class EmployeeManagementSystem:
    def __init__(self):
        self.employee_list = []
        self.current_employee_id = 1

    def add_employee(self, employee):
        employee.id = self.current_employee_id
        self.current_employee_id += 1
        self.employee_list.append(employee)

    def calculate_all_salary(self):
        total_salary = 0
        for employee in self.employee_list:
            total_salary += employee.calculate_salary()
        return total_salary

    def add_work_hours(self, employee, hours):
        try:
            assert isinstance(employee, PartTimeEmployee), "只能傳入PartTimeEmployee的物件"
            employee.set_hours_worked(hours)
        except AssertionError as e:
            print(e)

    def set_stipend(self, employee, stipend):
        try:
            assert isinstance(employee, Intern), "只能傳入Intern的物件"
            assert stipend > 0, "獎助學金必須大於0"
            employee.stipend = stipend
        except AssertionError as e:
            print(e)

    def set_full_time_salary(self, employee, salary):
        try:
            assert isinstance(employee, FullTimeEmployee), "只能傳入FullTimeEmployee的物件"
            assert salary > 0, "薪水必須大於0"
            employee.salary = salary
        except AssertionError as e:
            print(e)

    def print_all_employee(self):
        for employee in self.employee_list:
            print(f"員工編號: {employee.id}, 員工姓名: {employee.name}, 薪水: {employee.calculate_salary()}")

    def print_employee(self, employee):
        if employee in self.employee_list:
            print(f"員工編號: {employee.id}, 員工姓名: {employee.name}, 薪水: {employee.calculate_salary()}")
        else:
            print("找不到此員工")
