#!-*-coding:utf8 -*-
'''
Calcula o tempo de run do programa (diff entre start e end)
'''

from timeit import default_timer

def timer(n):
    #starting point
    start = default_timer()
    for i in range(0, n):
        print(i)
    #ending point
    end = default_timer() - start
    print(end)

timer(5)