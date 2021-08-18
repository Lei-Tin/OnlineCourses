# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

num = factorial(int(input("Number: ")))

print("The factorial of that is: " + str(num))