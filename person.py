#!-*-coding:utf8 -*-
'''
Orientação a objetos Herança
'''
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def get_name(self):
        return self.first+ " "+ self.last


class Employee(Person):
    def __init__(self, first, last, employeeNumber):
        Person.__init__(self, first, last)
        self.employeedNumber = employeeNumber

    def get_employee(self):
        return self.get_name()+", "+"{}".format(self.employeedNumber)


ana = Person('ana', 'ferreira')
print(ana.get_name())
ana_employee = Employee('ana', 'ferreira', 1)
print(ana_employee.get_employee())