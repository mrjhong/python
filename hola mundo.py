#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 18:55:22 2021

@author: jhon
"""
diccionarioest={}
lista=[]
while True:
    codigo =(input("codigo "))    
    nombre =(input("nombre "))    
    genero =(input("genero "))    
    carrera =(input("carrera "))    
    promedio= float(input("promedio "))    
    diccionarioest={"codigo":codigo,
                   "nombre":nombre,
                   "genero":genero,
                   "carrera":carrera,
                   "promedi":promedio
                   }
    lista.append(diccionarioest)
    print("desea agregar mas estudiantes si o no")
    res=int(input())
    if res==0: break
print (lista)
print(max(diccionarioest))
