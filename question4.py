#!-*-coding:utf8 -*-
'''
Aceita um arquivo e imprimi a extenção
'''

file = input('Enter a file:')
file_info = file.split('.')
file_name = file_info[0]
file_extension = file_info[1]
print(file_extension)