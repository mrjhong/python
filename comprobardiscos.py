
"""
import math
import psutil
import csv
import socket
import os.path as path
import os


datos_Servidor=[]

if (path.exists("servidores.csv") == False):
    with open("servidores.csv","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Direccion de Equipo"';'"Espacio Disco"';'"nombre"';'"direccion"';'"telefono"';'"ciudad"';'"pais"])
cmd = '@echo off echo Welcome to MS DOS'
os.popen(cmd) 
          
direccion_equipo = socket.gethostbyname(socket.gethostname())

print(direccion_equipo)            
espacio_disco=psutil.disk_usage("c:/")
print(round(espacio_disco.free/1000000000))
print(espacio_disco.used/1000000000)

PRUEBAS_disco= psutil.getloadavg()
print(PRUEBAS_disco)
i = int(math.floor(math.log(espacio_disco.free, 1024)))
p = math.pow(1024, i)
s = round(espacio_disco.free / p, 2)
datos_Servidor.append(direccion_equipo)

with open('servidores.csv', 'r') as file:
    clientesread = csv.reader(file)
    clientest= list(clientesread)    


    
    
    
if (s<30):
    datos_Servidor.append("sin espacio")
    with open ("servidores.csv", "a", newline="")as file:
        writer = csv.writer(file, delimiter= ";")
        writer.writerow(datos_Servidor)
else:
    datos_Servidor.append("OK")
    with open ("servidores.csv", "a", newline="")as file:
        writer = csv.writer(file, delimiter= ";")
        writer.writerow(datos_Servidor)
        
