#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:57:23 2021

@author: jhon
"""
destino = int()
tenvio = int()
valenvio = int()
# definicion de variables
total = int()
total2 = int()
total3 = int()
totalcomp =int()
totaldesc = int()
valproduct = int()
valdescuento = int()
valenvio = 0
res2 = 1
while True:

    res= int(input("> "))# 1. opcion=2
    

    if res==2:   #opcion=1
      
         tenvio = int(input("> "))     
         
           
        
         destino = int(input("> "))
         
       
  
         
         
    while res2==1:        
        ref = str(input("> "))
        producto = str(input("> "))
        cantproduct = int(input("> "))
        valproduct = int(input("> "))
        
        
        if cantproduct>3:
            valdescuento = ((5*valproduct)/100)*cantproduct
            total = valproduct*cantproduct
            total2= total+total2
            totalcomp = totalcomp+total
            totaldesc = totaldesc+valdescuento
           # print("valor del producto con descuento ",total)     
        else:
            total= valproduct*cantproduct 
            total2= total+total2
            totalcomp = totalcomp+total
            
        total3= total2+total3
         
        res2 = int(input("> "))
        if res2 == 2:break
            
            
            
    if tenvio==1 and totalcomp>=800000 and destino==1:
        valenvio = 0

    elif destino==1 and totalcomp>=500000 and tenvio==2:
    			     valenvio = 0
    				#print("ENVIO GRATIS")
    elif destino==1 and tenvio==1:
    					valenvio = 8000

    elif tenvio==2 and destino==1:
    					valenvio = 4000

    			
    elif destino==2 and totalcomp>=1000000 and tenvio==2:
                    valenvio = 0

    elif tenvio==1 and destino==2:#envio rapido
    					valenvio = 10000

    elif tenvio==2 and destino==2:#envio normal
    					valenvio = 5000

    			# internacional
    elif destino==3 and totalcomp>=2000000 and tenvio==2:
    			   valenvio = 0
    elif tenvio==1 and destino==3:
    					valenvio = 40000

    elif tenvio==2 and destino==3:
    					valenvio = 20000

              
    print(total2) 
    print(round(totaldesc))
    print(round(valenvio))
    print(round((totalcomp+valenvio)-totaldesc))

    if res==4:break