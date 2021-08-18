# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:03:11 2021

@author: ray-h
"""

# Givens
# Outstanding balance on the card
balance = 484

# Annual interest rate as decimal
annualInterestRate = 0.2

# Minimum monthly payment as decimal
monthlyPaymentRate = 0.04



# To be solved
monthlyInterestRate = annualInterestRate / 12

months = 12

while months > 0:
    
    minimumMonthlyPayment = balance * monthlyPaymentRate

    monthlyUnpaidBalance = balance - minimumMonthlyPayment

    balanceUpdated = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
    balance = balanceUpdated
    
    months -= 1

print(round(balance, 2))