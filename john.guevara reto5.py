from datetime import  datetime
import csv
import os.path as path
destino = int()
cliente=[]
cliente2=[]
clientes=[]
fac=5320
cliented=[]
cliente2d=[]
clientesd=[]
datos_compra=[]
datos_compra=[]
datos_product=[]
tenvio = int()
transporte = int()
valenvio = int()
# definicion de variables
total = int()
total2 = int()
total3 = int()
totalcomp =int()
totaldesc = int()
cantproduct = int()
valproduct = int()
valdescuento = int()
valenvio = 0
res2 = 1
res= int()
#fac=6380
numcomp=0
numcomp2=0
envio=0
h=0
i=0
tur2=0
tur1=0
turno=int()
if (path.exists("clientes.csv") ==False):
    with open("clientes.csv","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["tipo_documento","id","nombre","direccion","telefono","ciudad","pais"])
    
            
        
if (path.exists("compras.csv") ==False):
            with open("compras.csv","w",newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID","FACTURA","FORMA DE ENVIO","TIPO DE ENVIO","REFERENCIA","PRODUCTO","CANTIDAD","PRECIO","VALOR DE LA COMPRA","DESCUENTO","VALOR ENVIO","TOTAL","JORNADA"])
        

            
        
if (path.exists("envios.csv") ==False):
    with open("envios.csv","w",newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["factura","forma_entrega","tipo_entrega","empresa_transportadora"])

def imprimir_factura():
   factura=[]
   with open('clientes.csv', 'r') as file:
                 clientesread = csv.reader(file)
                 clientest= list(clientesread)
   with open('compras.csv', 'r') as file:
                 comprasread = csv.reader(file)
                 compratest= list(comprasread)
                 print(compratest[-1]) 
   with open('envios.csv', 'r') as file:
                 envioread = csv.reader(file)
                 enviotest= list(envioread)
                 print(enviotest[-1])              
                 
                 
                 print(clientest[-1])
                 print("*******FACTURA*******")
                 print("NUMERO DE FACTURA",compratest[-1][1])
                 factura.append(compratest[-1][1])
                 print("CLIENTE",clientest[-1][2])
                 factura.append(clientest[-1][2])
                 print("TIPO DE DOCUMENTO",clientest[-1][0]) 
                 factura.append(clientest[-1][0])
                 print("NUMERO DOCUMENTO",clientest[-1][1])
                 factura.append(clientest[-1][1])
                 print("DIRECCION",clientest[-1][3])
                 factura.append(clientest[-1][3])
                 print("TELEFONO",clientest[-1][4])
                 factura.append(clientest[-1][4])
                 print("CIUDAD",clientest[-1][5])
                 factura.append(clientest[-1][5])
                 print("PAIS",clientest[-1][6])
                 factura.append(clientest[-1][6])
                 print("TIPO DE DOCUMENTO",clientest[-1][0])
                 print("*******DATOS DEL PRODUCTO*******")
                 i=-1
                 while True:
                     
                     print("REFERENCIA",compratest[i][4])
                     factura.append(compratest[i][4])
                     comparativ=compratest[i][1]
                     print(comparativ)
                     print("PRODUCTO",compratest[i][5])                     
                     factura.append(compratest[i][5])
                     print("CANTIDAD",compratest[i][6])
                     factura.append(compratest[i][6])
                     print("VALOR  UNITARIO",compratest[i][7])
                     factura.append(compratest[i][7])

                     i=i-1
                     if comparativ!=compratest[-1][1]:break
                 print("VALOR  PRODUCTOS",compratest[-1][8])
                 factura.append(compratest[-1][8])
                 print("VALOR DESCUENTO",compratest[-1][9])
                 factura.append(compratest[-1][9])
                 print("VALOR ENVIO",compratest[1][10])
                 factura.append(compratest[-1][10])    
                 
                 print("VALOR DESCUENTO",compratest[-1][9])
                 factura.append(compratest[-1][9])
                 print("VALOR TOTAL A PAGAR *",compratest[-1][11],"*")
                 factura.append(compratest[-1][11])
                 print("*******DATOS DE ENVIO*******")
                 
                 print("DESTINATARIO",enviotest[-1][2])
                 factura.append(enviotest[-1][2])
                 print("TIPO DE DOCUMENTO DEL DESTINATARIO",enviotest[-1][0]) 
                 factura.append(enviotest[-1][0])
                 print("NUMERO DOCUMENTO DEL DESTINATARIO",enviotest[-1][1])
                 factura.append(enviotest[-1][1])
                 print("DIRECCION DE DESTINO",enviotest[-1][3])
                 factura.append(enviotest[-1][3])
                 print("TELEFONO DEL DESTINATARIO",enviotest[-1][4])
                 factura.append(enviotest[-1][4])
                 print("CIUDAD DE DESTINO",enviotest[-1][5])
                 factura.append(enviotest[-1][5])
                 print("PAIS DE DESTINO",enviotest[-1][6])
                 factura.append(enviotest[-1][6])
                 with open ("factura.csv", "a", newline="")as file:
                     writer = csv.writer(file, delimiter= ",")
                     writer.writerow(factura)
                 print("*****************************************")
def envios(): 
            while True:
                 try:
                     while True:
                          print("TIPO DE DOCUMENTO,\n1.CC,\n2.CE,\n3.NUIP ")
                          ti=(input(" "))
                          if  (ti.isspace()) is False:break
                 except Exception:
                   pass
                 if (ti.isspace()) is False and ti!="":break  
            cliented.append(ti)
             
            while True:
                try:
                     while True:
                         print("NUMERO DE DOCUMENTO DEL DESTINATARIO")
                         ni=(input("> "))
                         if  (ni.isspace()) is False:break
                except Exception:
                    print("OPCION INCORRECTA ")
                if (ni.isspace()) is False and ni!="":break  
            cliented.append(ni)
    
                
            while True:
                try:
                     while True:
                         print("NOMBRE DEL DESTINATARIO")
                         name=(input("> "))
                         if  (name.isalpha()) is True:break
                except Exception:
                    print("escriba su nombre sin espacios")
                if (name.isalpha()) is True:break         
            cliented.append(name)
    
    
            while True:
                try:
                     while True:
                         print("DIRECCION DE DESTINO")
                         adress=(input("> ")) 
                         if  (adress.isspace()) is False:break
                except Exception:
                    print("escriba su nombre sin espacios")
                if (adress.isspace()) is False and adress!="":break 
            cliented.append(adress)
    
    
            while True:
                try:
                     while True:
                         print("NUMERO TELEFONICO del DESTINATARIO")
                         tel=(input("> "))
                         if  (tel.isdigit()) is True and (len(tel))>=3:break
                except Exception:
                    print("numero de telefono invalido")
                if  (tel.isdigit()) is True and (len(tel))>=3:break
            cliented.append(tel)
    
    
            while True:
                try:
                     while True:
                         print("CIUDAD de destino")
                         city=(input("> "))
                         if  (city.isalpha()) is True: break
                except Exception:
                    print("escriba la ciudad  sin espacios")
                if  (city.isalpha()) is True:break            
            cliented.append(city)
            
    
            while True:
                try:
                     while True:
                         print("pais de destino")
                         pais=(input("> "))
                         if  (pais.isalpha()) is True: break
                except Exception:
                    print("escriba el pais sin espacios")
                if  (pais.isalpha()) is True:break 
            cliented.append(pais)
            

            while True:
                try:
                     while True:
                         print("empresa transportadora, \n1.empresaA, \n2-empresaB, \n3-empresaC")
                         transporte=int(input("> "))
                         if  transporte>0 and transporte<4: break
                except Exception:
                    
                    
                    print(transporte," no es un numero valido ")
                if  transporte>0 and transporte<4: break                 
            cliented.append(transporte)

                
             
            
            with open ("envios.csv", "a", newline="")as file:
                writer = csv.writer(file, delimiter= ",")
                writer.writerow(cliented)                                                         
def cant_turnos():
    tur2=0
    tur1=0
    with open('compras.csv', 'r') as file:
         comprasread = csv.reader(file)
         compratest= list(comprasread)
         
         for i in range (len(compratest)):
             jornada=compratest[i]
        
             if jornada[-1]=="mañana":
                 tur1=tur1+1
             if jornada[-1]=="tarde":
                 tur2=tur2+1
    print("que turno quiere ver MAÑANA = 1 ,TARDE = 2") 
    turno=int(input())   
    if turno==1:
                print("mañana")
                print(tur1)
            
    if turno==2:
                print("tarde")
                print(tur2)         
def process_turno():
    numcomp=0
    numcomp2=0
    tur2=0
    tur1=0
      
    hora=datetime.now().time()
    hour= datetime.strptime("12:00:00", "%X").time()
    hour2= datetime.strptime("23:59:00", "%X").time()
    if hora>hour and hora<=hour2:
        numcomp=numcomp+1
        t1compra=round((totalcomp+valenvio)-totaldesc)
        tur1=tur1+t1compra
        jornada="tarde"
    else:
        numcomp2=numcomp2+1
        t2compra=round((totalcomp+valenvio)-totaldesc)
        tur2=tur2+t2compra
        jornada="mañana"
    return jornada
def compras_turno():
    totalm=0
    totalt=0
    with open('compras.csv', 'r') as file:
         comprasread = csv.reader(file)
         compratest= list(comprasread)  
         #print(compratest)
         tamaño=int(len(compratest)-2)
         h=1
         i=0
         while True:
             jornada=compratest[h]
             h=h+1
             
             i=i+1
            # print(jornada)
# =============================================================================
             
             if jornada[-1]=="mañana":
              
                      totalmañana=int(jornada[-2])
                      totalm=totalmañana+totalm
             if jornada[-1]=="tarde":
                      totaltarde=int(jornada[-2])
                      totalt=totaltarde+totalt
# =============================================================================
             if i>tamaño:break        
    print("total compras por turno 1=mañana 2=tarde 3=salir")
    res=int(input())         
    if res==1:
        print("total ventas mañana ",totalm)
    if res==2:
        print("total ventas tarde ",totalt)
    return res    
def process_compra (fac,clientes):

    datos_compra=[]
    datos_compra=[]
    datos_product=[]
    tenvio = int()

    valenvio = int()
    # definicion de variables
    total = int()
    total2 = int()
    total3 = int()
    totalcomp =int()
    totaldesc = int()
    cantproduct = int()
    valproduct = int()
    valdescuento = int()
    valenvio = 0
    res2 = 1
    
    with open('clientes.csv', 'r') as file:
            csv_reader = csv.reader(file)
            clientest= list(csv_reader)   
            document=clientest[-1]
            ident=document[1]
          
                                
    while True:
      try:
           while True:
               print("tipo de envio, \n1.rapido, \n2.normal")
               tenvio = int(input("> "))
               if tenvio>0 and tenvio<3:break
      except Exception:
         print("OPCION INCORRECTA ESCOJA UN NUMERO ENTRE 1 Y 2 ")
      if tenvio>0 and tenvio<3:break
    
    
    while True:
      try:
           while True:
               print("destino, \n1.local, \n2.nacional, \n3.internacional")
               destino = int(input("> "))
               if destino>0 and destino<4:break
      except Exception:
         print("OPCION INCORRECTA ESCOJA UN NUMERO ENTRE 1 Y 4 ")
      if destino>0 and destino<4:break
    #datos_product.append(destino)  
              
        
         
    while True:
        datos_product.append(ident)
        datos_product.append(fac)       
        datos_product.append(tenvio)  
        datos_product.append(destino)
        while True:
             try:
                 while True:
                    print("referencia")             
                    ref =(input("> "))
                    if  (ref.isspace()) is False:break
             except Exception:
               pass
             if (ref.isspace()) is False and ref!="":break    
        datos_product.append(ref)
             
        while True:
             try:
                 while True:
                    print("producto")             
                    producto =(input("> "))
                    if  (producto.isspace()) is False:break
             except Exception:
               pass
             if (producto.isspace()) is False and producto!="":break             
        datos_product.append(producto)
        
        while True:
             try:
                 #while True:
                    print("cantidad producto")             
                    cantproduct = int(input("> "))
                    if cantproduct>0:break
             except Exception:
               pass
             if  cantproduct>0:break           
        datos_product.append(cantproduct)     
        
        while True:
             try:
                 #while True:
                    print("valor producto")             
                    valproduct = int(input("> "))
                    if valproduct>0:break
             except Exception:
               pass
             if  valproduct>0:break
        datos_product.append(valproduct)
        
     
         
        
        
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

    
        while True:
            print("otro producto")
            res2= (input("> "))
            if res2 =="2" or res2=="1":break
        
        if res2 =="1":
            datos_compra2=list(datos_product) 
            datos_compra.append(datos_compra2)
            datos_product.clear() 
            print(datos_compra)
# =============================================================================
#             with open ("compras.csv", "a", newline="")as file:
#                 writer = csv.writer(file, delimiter= ",")
#                 writer.writerows(datos_compra)
# =============================================================================
        if res2=="2":
            print(total2) 
            datos_product.append(total2)
            print(round(totaldesc)) 
            datos_product.append(totaldesc)
            print(round(valenvio))   
            datos_product.append(valenvio)            
            totalpay=(round((totalcomp+valenvio)-totaldesc))
            print(totalpay)
            datos_product.append(totalpay)
            turno=process_turno()           
            datos_product.append(turno)          
            datos_compra2=list(datos_product) 
            datos_compra.append(datos_compra2)
            datos_product.clear()
            print(datos_compra)
            with open ("compras.csv", "a", newline="")as file:
                writer = csv.writer(file, delimiter= ",")
                writer.writerows(datos_compra)
            
            break
          

    print("el envio va hacia el mismo cliente 1=si 2=no") 
    envio=int(input())
    if envio==1:
        datos_envio=document
        print(datos_envio)
        print("empresa transportadora")
        emp=input()
        datos_envio.append(emp)
        datos_envio.append(tenvio)  
        datos_envio.append(destino)
        with open ("envios.csv", "a", newline="")as file:
            writer = csv.writer(file, delimiter= ",")
            writer.writerow(datos_envio)
    return envio        
def proces_clientes():      
    
       
        while True:
             try:
                 while True:
                      print("TIPO DE DOCUMENTO,\n1.CC,\n2.CE,\n3.NUIP ")
                      ti=(input("h> "))
                      if  (ti.isspace()) is False:break
             except Exception:
               pass
             if (ti.isspace()) is False and ti!="":break  
        cliente.append(ti)
         
        while True:
            try:
                 while True:
                     print("NUMERO DE DOCUMENTO")
                     ni=(input("> "))
                     if  (ni.isspace()) is False:break
            except Exception:
                print("OPCION INCORRECTA ")
            if (ni.isspace()) is False and ni!="":break  
        cliente.append(ni)

            
        while True:
            try:
                 while True:
                     print("NOMBRE")
                     name=(input("> "))
                     if  (name.isalpha()) is True:break
            except Exception:
                print("escriba su nombre sin espacios")
            if (name.isalpha()) is True:break         
        cliente.append(name)


        while True:
            try:
                 while True:
                     print("DIRECCION")
                     adress=(input("> ")) 
                     if  (adress.isspace()) is False:break
            except Exception:
                print("escriba su nombre sin espacios")
            if (adress.isspace()) is False and adress!="":break 
        cliente.append(adress)


        while True:
            try:
                 while True:
                     print("NUMERO TELEFONICO")
                     tel=(input("> "))
                     if  (tel.isdigit()) is True and (len(tel))>=3:break
            except Exception:
                print("numero de telefono invalido")
            if  (tel.isdigit()) is True and (len(tel))>=3:break
        cliente.append(tel)


        while True:
            try:
                 while True:
                     print("CIUDAD")
                     city=(input("> "))
                     if  (city.isalpha()) is True: break
            except Exception:
                print("escriba la ciudad  sin espacios")
            if  (city.isalpha()) is True:break            
        cliente.append(city)
        

        while True:
            try:
                 while True:
                     print("pais")
                     pais=(input("> "))
                     if  (pais.isalpha()) is True: break
            except Exception:
                print("escriba el pais sin espacios")
            if  (pais.isalpha()) is True:break            
        cliente.append(pais)
        
        cliente2=list(cliente) 
        clientes.append(cliente2)
        cliente.clear() 

        print(clientes)     
        print(len(clientes) ," clientes")
        with open ("clientes.csv", "a", newline="")as file:
                writer = csv.writer(file, delimiter= ",")
                writer.writerows(clientes)
        return clientes         
# =============================================================================
#        a=arch_clientes("clientes.csv")
#        print(a)
#        print(a[-1][1])         
# =============================================================================





while True:
    
    print("MENU DE OPCIONES,\n1.DATOS DEL CLIENTE,\n2.DATOS DE LA COMPRA,\n3.IMPRESION CANTIDAD DE COMPRAS POR TURNO,\n4.IMPRESION VALOR COMPRAS POR TURNO,\n5.DATOS DEL ENVIO,\n6.IMPRIMIR FACTURA,\n7.SALIR")
    while True:
        try:
             while True:
                 print("ESCOJA UNA OPCION ENTRE 1 Y 7")
                 res= int(input("> "))# 1. opcion=2
                 if res>0 and res<8:break
        except Exception:
           print("OPCION INCORRECTA ESCOJA UN NUMERO ENTRE 1 Y 7 MENU DE OPCIONES,\n1.DATOS DEL CLIENTE,\n2.DATOS DE LA COMPRA,\n3.IMPRESION CANTIDAD DE COMPRAS POR TURNO,\n4.IMPRESION VALOR COMPRAS POR TURNO,\n5.DATOS DEL ENVIO,\n6.SALIR,\n")
        if res>0 and res<7:break
        
        ###################OPCION1######################################
   
    if res==1:
        
      proces_clientes()
      h=1     

    if res==2 and h==1:  
      if path.exists("clientes.csv"): 
          with open('clientes.csv', 'r') as file:
                 
                 clientesread = csv.reader(file)
                 clientest= list(clientesread)
                 clientes=clientest[-1]
                  
                    
                 print(clientes)   
          if path.exists("compras.csv"): 
              with open('compras.csv', 'r') as file:
                 
                 comprasread = csv.reader(file)
                 compratest= list(comprasread)
                 
                 if len(compratest)<2:  
                    fac=5320
                 else:
        
                    dbcompra=compratest[-1]
                    fac=int(dbcompra[1])
                    #int=fac
                    print(fac)
          else:
              fac=5320      
      
          fac=fac+1  
          envio=process_compra(fac,clientes)
          
      else:
        print("no hay clientes")
        
    if res==3:
      cant_turnos()
      
    if res==4 :
       while True: 
           res=compras_turno()
           if res==3:break
    if res==5:
         if envio==2:
             envios()
         else:
             print("los datos de envio son los mismos no nesesita digitarlos de nuevo")
             
    if res==6:
        imprimir_factura()
    if res==7:break
    