#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:57:13 2024

#Cafe simulation that allows user to select items to purchase, and produces a receipt of chosen items. 
#

#@author: dquinn (dquinn06@mail.pima.edu)
"""


#Welcome message and menu display

print('            ')
print('Welcome to the cafe!')
print('             ')
print('╔══ ❀•°❀°•❀ ══╗ ')
print('     MENU  ')
print('  Coffee - $5')
print('  Tea    - $5')
print('  Muffin - $4')
print('  Pupcup - $1')
print('╚══ ❀•°❀°•❀ ══╝ ')
print('         ')
print('         ')

#Select amt of items

coffee = input("How many coffees would you like? ")

coffee = int(coffee)    #user inputs # of coffees wanted

tea = input("How many teas would you like? ")

tea = int(tea) #user inputs # of teas wanted

muffin = input("How many muffins would you like? ")

muffin = int(muffin)    #user inputs # of muffins wanted

pupcup = input("How many teas would you like? ") #user inputs # of pupcups wanted

pupcup = int(pupcup) 

#calculate prices

cof_price = coffee * 5       #amount of coffees times price

tea_price = tea * 5 # amt tea times price

muf_price = muffin * 4       #amount of muffins times price

pup_price = pupcup * 1 #amt pupcup times price

subtotal = cof_price + muf_price + tea_price + pup_price   #total price for coffees and muffins w/o tax

tax_price = subtotal * 0.06         #6% tax on subtotal

total = subtotal + tax_price        #total of subtotal plus tax

#Show receipt

print('           ')                     #create blank border space
print('....::::**•°✾°•**::::....')       #create cute border

print('My Coffee and Muffin Shop')
print('Number of coffees bought?')
print(coffee)
print('Number of muffins bought?')
print(muffin)
print('....::::**•°✾°•**::::....')
print('             ') 
print('             ')                      #seperate counts and receipt
print('✯¸.•´*¨`*•✿ ✿•*`¨*`•.¸✯')
print('       ')
print('My Coffee and Muffin Shop Receipt')
print(coffee,'Coffee at $5 each: $', cof_price)
print(tea,'Tea at $5 each: $', tea_price)
print(muffin, 'Muffin at $4 each: $', muf_price) 
print(pupcup,'Pupcups at $1 each: $', pup_price)
print('Subtotal: $', subtotal)
print('6% tax: $', tax_price)
print('       ')
print('.•° ✿ °•.')
print('Total: $', total )
print('°•. ✿ .•°')
print('             ')
print('✯¸.•´*¨`*•✿ ✿•*`¨*`•.¸✯')

print('Thank you, come again!')       #thank you message




