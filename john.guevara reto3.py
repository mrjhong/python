from datetime import  datetime
destino = int()
cliente=[]
cliente2=[]
clientes=[]

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
fac=6380
numcomp=0
numcomp2=0
i=0
tur2=0
tur1=0
turno=int()

while True:
    print("MENU DE OPCIONES,\n1.DATOS DEL CLIENTE,\n2.DATOS DE LA COMPRA,\n3.IMPRESION CANTIDAD DE COMPRAS POR TURNO,\n4.IMPRESION VALOR COMPRAS POR TURNO,\n5.DATOS DEL ENVIO,\n6.SALIR,\n")
    while True:
        try:
             while True:
                 print("ESCOJA UNA OPCION ENTRE 1 Y 6")
                 res= int(input("> "))# 1. opcion=2
                 if res>0 and res<7:break
        except Exception:
           print("OPCION INCORRECTA ESCOJA UN NUMERO ENTRE 1 Y 6 MENU DE OPCIONES,\n1.DATOS DEL CLIENTE,\n2.DATOS DE LA COMPRA,\n3.IMPRESION CANTIDAD DE COMPRAS POR TURNO,\n4.IMPRESION VALOR COMPRAS POR TURNO,\n5.DATOS DEL ENVIO,\n6.SALIR,\n")
        if res>0 and res<7:break
        
        ###################OPCION1######################################
   
    if res==1:
        
       while True:
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
            
            
            while True:
                print("otro cliente")
                res2= (input("> "))
                if res2 =="2" or res2=="1":break
            if res2 =="2":break
       print(len(clientes) ," clientes")
            #  ##########=======OPCION 2=========================

    if res==2:   
      while True:
        i=i+1
        while True:
          try:
               while True:
                   print("tipo de envio, \n1.rapido, \n2.normal")
                   tenvio = int(input("> "))
                   if tenvio>0 and tenvio<3:break
          except Exception:
             print("OPCION INCORRECTA ESCOJA UN NUMERO ENTRE 1 Y 2 ")
          if tenvio>0 and tenvio<3:break
        datos_compra.append(tenvio)  
        
        
        while True:
          try:
               while True:
                   print("destino, \n1.local, \n2.nacional, \n3.internacional")
                   destino = int(input("> "))
                   if destino>0 and destino<4:break
          except Exception:
             print("OPCION INCORRECTA ESCOJA UN NUMERO ENTRE 1 Y 4 ")
          if destino>0 and destino<4:break
        datos_compra.append(destino)  
                  
        fac=fac+1  
        print("numero de factura ",fac) 
        
      
        
        

            
             
        while True:        
           
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
            
            datos_compra2=list(datos_product) 
            datos_compra.append(datos_compra2)
            datos_product.clear() 
            print(datos_compra)
            
            
            while True:
                print("otro producto")
                res2= (input("> "))
                if res2 =="2" or res2=="1":break
            if res2 =="2":break
        
        hora=datetime.now().time()
        hour= datetime.strptime("12:00:00", "%X").time()
        hour2= datetime.strptime("23:59:00", "%X").time()
        if hora>hour and hora<=hour2:
            numcomp=numcomp+1
            t1compra=round((totalcomp+valenvio)-totaldesc)
            tur1=tur1+t1compra
        else:
            numcomp2=numcomp2+1
            t2compra=round((totalcomp+valenvio)-totaldesc)
            tur2=tur2+t1compra    
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
        
        print(hora)
        while True:
            print("otra compra")
            res2= (input("> "))
            if res2 =="2" or res2=="1":break
        if res2 =="2":break
    if res==3:
        while i!=0:
            print("1.turno1, \n2.turno2, \n3.salir")
            while True:
                try:
                     while True:
                         print("ESCOJA UNA OPCION ENTRE 1 Y 3")
                         turno=int(input("> "))# 1. opcion=2
                         if turno>0 and turno<4 :break
                except Exception:
                   print("datos incorrectos")
                if turno>0 and turno<4 :break
            if turno==1:
                print(numcomp)
            if turno==2:
                print(numcomp2)
            if turno==3  :break
     
    if res==4:  
        print("total ventas turno 1")
        print(tur1)
        print("total ventas turno2")
        print(tur2) 
    if res==5:
        while True: 

            
            
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

                
            cliente2d=list(cliented) 
            clientesd.append(cliente2d)
            cliented.clear() 
             
             
            while True:
            
                 res2= int(input("> "))
                 if res2 ==2 or res2==1:break
            if res2 ==2:break
             
            print(len(clientesd))
    if res==6:break