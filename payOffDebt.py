# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 16:46:52 2018

@author: positiveoutlier

Created a number of functions that can be used in debt calculations.
"""

# ik zou een functie remainingBalance(balance, annualInterestRate, monthlyPayment) maken die je kan aanroepen vanuit zowel remainingBalance(balance, annualInterestRate, monthlyPaymentRate) als minimumFixedMonthlyPaymentInTens als minimumFixedMonthlyPaymentInCents
# dan heb je die code op 1 plek en als die moet wijzigen hoef je maar 1 plek aan te passen en kan je nooit een plek vergeten

def remainingBalance(balance, annualInterestRate, monthlyPaymentRate):
    """ Using the balance, annual interest rate and the minimum
        required monthly payment, this function calculates
        the remaining balance after one year of repayments """
    for month in range(12):
        month += 1 #als je range(1, 13) gebruikt hoef je dit niet meer te doen
        monthlyRepayment = round(balance * monthlyPaymentRate, 2) #heel belangrijk als je met cijfers werkt om zoveel mogelijk floats (kommagetallen) te vermijden en ze proberen te vervangen door integers (gehele getallen), meestal gebeurt dit door met centen en percentages (getallen tusen 0 en 100) te werken ipv euro's en getallen tussen de 0 en 1
        unpaidBalance = balance - monthlyRepayment
        monthlyInterest =  unpaidBalance * (annualInterestRate / 12) #annualInterestRate / 12 kan je evt. in een variabele monthlyInterestRate zetten
        balance = round(unpaidBalance + monthlyInterest, 2)
	print("Remaining balance: " + str(balance)) #ik zou de functie lekker laten rekenen en alleen een bedrag teruggeven, dan kan je dit later printen of wat dan ook er mee doen, ook is dit fijn als je unit tests gaat maken, wat ik wel aanraad voor dit soort functies
        
remainingBalance(42, 0.2, 0.04)
        
def minimumFixedMonthlyPaymentInTens(balance, annualInterestRate):
    """ Using the balance and the annual interest rate, this function
        calculates the minimum required monthly payment which will
        result in the debt being paid off in a year.
        The monthly payment is a fixed payment (i.e. will be the 
        same amount eacht month), and a multiple of ten.
        This could potentially lead to a negative balance at the end
        of the year, which is fine."""
    monthlyRepayment = 0 #kan je dit niet zetten op balance gedeeld door 12 en dan naar het 10tal erboven afgerond? of moet je rekening houden met negatieve rente? Dan nog zou je dit met een if statement in kunnen stellen
    remainingBalance = balance
    while remainingBalance > 0 and monthlyRepayment < balance:
        monthlyRepayment += 10
        remainingBalance = balance
        for month in range(12):
            month += 1
            unpaidBalance = remainingBalance - monthlyRepayment
            monthlyInterest =  unpaidBalance * (annualInterestRate / 12)
            remainingBalance = unpaidBalance + monthlyInterest
            print("MonthlyRepayment:" + str(monthlyRepayment) + " Month: " + str(month) + " Balance: " + str(remainingBalance))
    print("Lowest payment: " + str(monthlyRepayment))
    
minimumFixedMonthlyPaymentInTens(200, 0.2)

def minimumFixedMonthlyPaymentInCents(balance, annualInterestRate):
    """ Using the balance and the annual interest rate, this function
        calculates the minimum required monthly payment which will
        result in the debt being paid off in a year.
        The monthly payment is a fixed payment (i.e. will be the 
        same amount eacht month) and will be calculated using
        bi-section search. The delta is 0.01, which means that the
        remaining balance at the end of the year must be either
        smaller than 0.01 or greater than -0.01.
    """
    monthlyInterest = annualInterestRate / 12
    lowerBound = balance / 12
    upperBound = (balance * (1 + monthlyInterest)**12) / 12
    delta = 0.01
    while True:
        remainingBalance = balance
        monthlyRepayment = (lowerBound + upperBound) / 2
        for month in range(12):
            month += 1
            unpaidBalance = remainingBalance - monthlyRepayment
            monthlyInterest =  unpaidBalance * (annualInterestRate / 12)
            remainingBalance = unpaidBalance + monthlyInterest
        if remainingBalance > delta:
            lowerBound = monthlyRepayment
        elif remainingBalance < -delta:
            upperBound = monthlyRepayment
        else:
            break
    print("Lowest payment: {:0.2f}".format(monthlyRepayment))
    
minimumFixedMonthlyPaymentInCents(999999, 0.18)     