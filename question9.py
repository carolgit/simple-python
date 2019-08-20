#!-*-coding:utf8 -*-
'''
Calcule o maximo e o minimo de uma sequencia de numeros
'''

list = [1,2,3,5,9,12,3,4,2]

def max_min(list):
    max = list[0]
    min = list[0]
    for num in list:
        if num > max:
            max = num
        elif num < min:
            min = num
    return max, min

max, min = max_min(list)
print(max, min)