# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 17:06:36 2021

@author: admin
"""

def listar_animales(archivo:str)->list:
    lista_animales = []
    
    archivo = open("animales_vcorta.csv", "r")
    
    #encabezados = archivo.readline()
    
    linea = archivo.readline()
    
    while (len(linea) != 0):
        #lista_animales.append(encabezados)
        lista_animales.append(linea)
        linea = archivo.readline();
    
    archivo.close()        
    
    return lista_animales

def crear_animal(archivo:str)->dict:
    animal = {}
    archivo = open("animales_vcorta.csv", "r")
    
    encabezados = archivo.readline()
    linea = archivo.readline()
           
    encs = encabezados.split(";")
    dat = linea.split(";")
   
    i = 0
    while (i < len(encs) ):
        dato = dat[i].replace("\n", "")
        
        try:
            dato = int(dat[i])
            if (dato <= 1):
                dato = bool(dato)
        except:
            dato = dat[i].replace("\n", "")

        animal[encs[i].replace("\n","")] = dato
        i+=1
        
    archivo.close()       
    
    return animal    

#programa principal
archivo="animales_vcorta.csv"
r=listar_animales(archivo)
print("\n",r,"\n")
t=crear_animal("animales_vcorta.csv")
print(t)
