#!-*-coding:utf8 -*-
'''
Calcular o produto de uma lista de inteiros usando um loop que não seja o for
'''

list = [1,2,3,4]
product = 1
while len(list) > 0:
    product *= list[0]
    list.remove(list[0])
    print(list)
    
print(product)