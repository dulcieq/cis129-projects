#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 15:10:54 2024

@author: dquinn
"""

total_bottles = 0
total_payout = total_bottles * 0.1
today_bottles = 0
counter = 1
keep_going = 'y' 

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

    keep_going = input("Input another week's data?")
    counter = 1
    total_payout = 0
    total_bottles = 0
    
