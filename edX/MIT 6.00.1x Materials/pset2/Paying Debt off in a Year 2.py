# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:11:55 2021

@author: ray-h
"""

# Given
balance = 4773

annualInterestRate = 0.2



# Find

balanceUpdated = balance

minimumFixedPayment = 0

month = 0

while True:
    
    balanceUpdated = balance
    month = 0
    minimumFixedPayment += 10
    
    for month in range(12):    
        
        monthlyInterestRate = annualInterestRate / 12.0
        
        monthlyUnpaidBalance = balanceUpdated - minimumFixedPayment
        
        balanceUpdated = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        
    if balanceUpdated < 0:
        break
    
print("Lowest Payment: " + str(minimumFixedPayment))