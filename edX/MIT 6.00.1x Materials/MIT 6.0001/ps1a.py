# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 23:51:39 2021

@author: ray-h
"""

# Part A - House hunting

# Algorithm A
# annual_salary = float(input("Enter your annual salary: "))

# portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

# total_cost = float(input("Enter the cost of your dream home: "))

# portion_down_payment = 0.25 # 25% of down payment

# down_payment = total_cost * portion_down_payment

# current_savings = 0

# investment_savings = 0

# months = 0

# monthly_salary = annual_salary / 12

# while current_savings < down_payment:
    
#     value_portion_saved = monthly_salary * portion_saved
    
#     investment_savings = current_savings * (0.04 / 12)
    
#     current_savings += investment_savings + value_portion_saved
    
#     months += 1
    
# print("Number of months: " + str(months))

# Algorithm B
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25

current_savings = 0
months = 0

while current_savings < total_cost * portion_down_payment:
    
    current_savings += (annual_salary / 12) * portion_saved
    
    current_savings += current_savings * (0.04 / 12)
    
    months += 1
    
print(f"\nNumber of months: {months}")