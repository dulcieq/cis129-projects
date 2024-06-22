#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:10:54 2024

@author: Dulcie Quinn


Allows a grocery store to keep track of the total number of bottles collected for seven days.

The program will calculate the total number of bottles returned for the week and the amount paid out (the total returned times .10 cents). 

The output of the program includes the total number of bottles returned and the total paid out.  

The program will ask the user if they have more data to enter and will end the program if they do not. 


"""

#define variables and set to 0
total_bottles = 0
total_payout = total_bottles * 0.1
today_bottles = 0
counter = 1
keep_going = 'y' 

#loop the program as long as the user has more data to enter
while keep_going == 'y': 
    #get week's data
    while counter <= 7:
        print('Enter # of bottles for day #', counter, ':')
        today_bottles = int(input())
        total_bottles = total_bottles + today_bottles
        counter = counter + 1

    #calc payout
    total_payout = 0 
    total_payout = total_payout + total_bottles * 0.1

    #print info

    print('Total Bottles:', total_bottles)
    print('Total Payout: $', total_payout)
    
    #continue or not

    keep_going = input("Input another week's data?")
    
    #reset counters to 0 or else results accumulate
    counter = 1
    total_payout = 0
    total_bottles = 0
    
