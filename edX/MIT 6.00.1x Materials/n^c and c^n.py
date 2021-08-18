# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 21:11:55 2021

@author: ray-h
"""

from time import sleep

c = 2

n = 0
while True:
    n += 1
    print('c^n = ' + str(c**n))
    print('n^c = ' + str(n**c))
    sleep(1)