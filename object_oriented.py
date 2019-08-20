#!-*-coding:utf8 -*-
'''
Orientação a objetos
'''
class Dog:
    kind = 'canine'
    tricks = []
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

our_dog = Dog('Sissi')
print(our_dog.name, our_dog.kind)
our_dog.add_trick('roll over')
print(our_dog.tricks)