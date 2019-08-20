#!-*-coding:utf8 -*-
'''
Orientação a objetos
'''
class Dog:
    kind = 'canine'
    def __init__(self, name):
        self.name = name

our_dog = Dog('Sissi')
print(our_dog.name)