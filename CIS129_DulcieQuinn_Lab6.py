#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 17:56:31 2024

@author: Dulcie Quinn

Calculates the number of packages of hot dogs and 
the number of packages of hot dog buns needed for a 
cookout, with the minimum amount of leftovers. 

"""

#set initial variables to 0 and recieve input from user
total_hotdogs = 0
attendees = 0
hotdogs_per = 0
attendees = int(input('# of people attending: '))
hotdogs_per = int(input('# of hotdogs per person: '))

#determine total hotdogs needed
total_hotdogs = attendees * hotdogs_per


print('total hotdogs needed:', total_hotdogs)

#set amount per package
DOGS = 10
BUNS = 8

#initialise variables for calculating 

dogs_left = 0
buns_left = 0
min_dogs = 0
min_buns = 0

#calculate minimums and leftovers
dogs_left = (DOGS - total_hotdogs % DOGS) % DOGS
min_dogs = int(total_hotdogs / DOGS) + (0 **(0 ** dogs_left))
buns_left = (BUNS - total_hotdogs % BUNS) % BUNS
min_buns = int(total_hotdogs / BUNS) + (0**(0** buns_left))

#show results to user
print('Minimum packages of hot dogs needed:', min_dogs)
print('Minimum packages of hot dog buns needed:', min_buns)
print('Hot dogs remaining:', dogs_left)
print('Hot dog buns remaining:', buns_left)

