# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 00:16:12 2021

@author: ray-h
"""

# Part B - Saving, with a raise
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25

current_savings = 0
months = 0

while current_savings < total_cost * portion_down_payment:
    
    if months % 6 == 0 and months != 0:
        annual_salary *= (1 + semi_annual_raise)
    
    current_savings += (annual_salary / 12) * portion_saved
    
    current_savings += current_savings * (0.04 / 12)
    
    months += 1
    
print(f"\nNumber of months: {months}")