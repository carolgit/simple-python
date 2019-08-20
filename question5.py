#!-*-coding:utf8 -*-
'''
Calcular a difereça entre 2 datas
'''
from datetime import date

first_date = date(2019, 8, 20)
secound_date = date(2018,7,20)

diff = first_date - secound_date

print(diff.days)