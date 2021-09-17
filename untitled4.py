#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 12:22:36 2021

@author: jhon
"""
n = int(input(">")) 
fil=1 
count=1  
num=1 
space = ''  
for fil in range(1,n+1):  
   for num in range(1,fil+1): #z recorre de 1 hasta x. Ejemplo en la 4 (x=4 z=1,2,3,4)  
     space+=(str(count)+(' '))  
     count+=1  
   print(space)  
   space ='' 