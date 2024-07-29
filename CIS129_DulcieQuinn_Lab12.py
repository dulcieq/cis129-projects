#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 19:46:39 2024

@author: Dulcie Quinn

CIS 129 Final Lab

Program creates a class for pets and prompts the user to enter info about their pet, 
updating the attributes associated. Can enter as many pets wanted. 


"""

keepgoing = 'y'

while keepgoing == 'y':
    print(' ')
    
    class pet: 
        def __init__(self,name = '',kind = '', age=''):
            self.name = name
            self.kind = kind
            self.age = age
            
        def changeName(self):
            self.name = str(input("Enter your pet's name: " ))
        
        def changeKind(self):
            self.kind = str(input("Enter your pet's species: "))
        
        def changeAge(self):
            self.age = float(input("Enter your pet's age: "))
    
    
    pt = pet()
    
    pt.changeName()
    pt.changeKind()
    pt.changeAge()
    
    print(' ')
    print(' ')
    
    print(f'Pet name: {pt.name}\nPet Kind: {pt.kind}\nPet age: {pt.age} years old')
    
    print(' ')
    print(' ')
    
    keepgoing = input('Enter another pet? (y/n)')
    
