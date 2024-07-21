#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 13:39:31 2024

@author: dquinn
"""
#✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧

import sys
import numpy as np
import csv

#✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧
print(' ')
print('Exercise 9.1')
print(' ')
print('✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧')
print(' ')

# get grades

keepgoing = True
grades = 0 
i = 0
grade_ar = []

print('Enter grades to compute average. Enter -1 to stop. Do not enter % sign.')
print(' ')

while keepgoing == True : 
    grade = float(input(f"Student {i+1}'s grade: "))
    if grade == -1:
        keepgoing = False
    else: 
        grades = grades + grade 
        grade_ar.append(grade)
        i = i + 1 
   
    
print(f'Average ({i} students): {np.average(grade_ar):.2f}%')

#sys.exit() 

print('Exercise 9.2')
print(' ')
print('✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧')

#✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧

# write to txt file 

with open('grades.txt', 'w') as storedgrades:
    for i in range(len(grade_ar)):
        storedgrades.write(f'{grade_ar[i]}\n')

#✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧

print(' ')
print('Exercise 9.2')
print(' ')
#read from txt file 

rgrades = []

with open('grades.txt', 'r') as readgrades:
    for i in readgrades:
        rgrades.append(float(i))

print('~ Grade Info ~')
for i in range(len(rgrades)):
    print(f'Grade {i+1} : {rgrades[i]}')

print(f'Count : {len(rgrades)} students')
print(f'Average : {np.average(rgrades):.2f}%')
print(f'Total : {np.sum(rgrades):.2f} points')
print(' ')

#✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧


print('✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧✧❁❁✧✿✿✧❁❁✧')
print(' ')
print('Exercise 9.3')
print(' ')

#dump to csv file

first = []
last = []
exam1 = []
exam2 = []
exam3 = []

keepgoing = True
i = 0 

print('To exit, enter -1 in "firstname" category. Do not enter % in "grade" categories.')
print(' ')


while keepgoing == True: 
    firstname = input(f"Student {i+1}'s firstname: ")
    if firstname == '-1': 
        keepgoing = False
        break
    lastname = input(f"Student {i+1}'s lastname: ")
    exam_1 = float(input(f"Student {i+1}'s exam 1 grade: "))
    exam_2 = float(input(f"Student {i+1}'s exam 2 grade: "))
    exam_3 = float(input(f"Student {i+1}'s exam 3 grade: "))
    print(' ')
    print('~~~')
    print(' ')
    
    first.append(firstname)
    last.append(lastname)
    exam1.append(exam_1)
    exam2.append(exam_2)
    exam3.append(exam_3)
    
    i += 1 
    

with open('grades.csv', 'a') as f:
    for fname,lname,ex1grade,ex2grade,ex3grade in zip(first,last,exam1,exam2,exam3):
        f.write(f'{fname},{lname},{ex1grade},{ex2grade},{ex3grade}\n')

print(' ')
print('Exited. "grades.csv" has been created.')



















































