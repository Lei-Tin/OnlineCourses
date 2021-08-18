# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:33:22 2021

@author: ray-h
"""

# Given

balance = 999999

annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12.0

# Lower bound
low = balance / 12

# Upper bound
high = (balance * (1 + monthlyInterestRate)**12) / 12

month = 0

epsilon= 0.0001

while True:
    
    balanceUpdated = balance
    
    lowestPayment = (low + high) / 2.0
        
    for month in range(12):    
        
        monthlyUnpaidBalance = balanceUpdated - lowestPayment
        
        balanceUpdated = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
    if balanceUpdated > 0:
        low = lowestPayment
        
    elif balanceUpdated < 0:
        high = lowestPayment
        
    if abs(balanceUpdated) - epsilon <= 0:
        break
        
print(round(lowestPayment, 2))