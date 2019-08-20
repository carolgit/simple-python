#!-*-coding:utf8 -*-
'''
Receber nome e sobrenome e imprimir ao contrário
'''

name = input('First name:')
last_name = input ('Last name:')

reversed_name = "{} {}".format(last_name, name)

print(reversed_name)