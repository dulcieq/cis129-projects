#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:12:37 2024

@author: dquinn
"""

# Module 4 Lab-4
# Dulcie Quinn
# June 13th, 2024
# purpose: assigns a $6,000 store bonus if monthly sales 
#are more than $110,000; else if monthly sales are greater than or 
#equal to $100,000 the store bonus is $5,000, else if monthly sales 
#are greater than or equal to $90,000 the store bonus is $4,000, else if 
#monthly sales are greater than or equal to $80,000, the store bonus is 
#$3,000 otherwise a $0 amount or no store bonus is awarded.  T
#hey are using a percent of sales increase to determine if employees 
#get individual bonuses.  If sales increased by an amount greater than 
#or equal to 5% (0.05) then all employees get $75, else if sales increased 
#by an amount greater than or equal to 4%, employees get $50, else if sales 
#increased by an amount greater than or equal to 3% employees get $40 otherwise 
#they get $0. 

# declare local variables

monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0  # employee bonus amount
salesIncrease = 0  # percent of sales increase
prompt1 = 'How much were monthly sales?:  $' # prompt will be a string literal
prompt2 = 'How much did sales increase? (Enter a percentage w/o the symbol %):  '

monthlySales = float(input(prompt1))# include code to get the monthly Sales
salesIncrease = float(input(prompt2))# include code to get the Increase in Sales

# This code determines the storeAmount bonus

if monthlySales >= 110000:
		storeAmount = 6000
elif monthlySales >= 100000:
		storeAmount = 5000
elif monthlySales >= 90000:
		storeAmount = 4000
elif monthlySales >=80000:
		storeAmount = 3000
else:
		storeAmount = 0
	
# This code gets the percent of increase in sales
salesIncrease = salesIncrease / 100

# This code determines the empAmount bonus
if salesIncrease >= .05:
		empAmount = 75
elif salesIncrease >= .04:
		empAmount = 50
elif salesIncrease >= .03:
		empAmount = 40
else:
		empAmount = 0

# This code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $",empAmount)
if (storeAmount == 6000 ) and (empAmount == 75):
		print('Congrats! You have reached the highest bonus amounts possible! ')

