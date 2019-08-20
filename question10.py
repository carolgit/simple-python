#!-*-coding:utf8 -*-
'''
Verifique se o numero é divisivel por um outro numero, aceitando valores do usuário
'''

def divisivel(num, bynum):
    if num % bynum == 0:
        return True
    else:
        return False

first_num = input('Enter a number:')
secound_num = input('Enter other number:')

print(divisivel(first_num, secound_num))
