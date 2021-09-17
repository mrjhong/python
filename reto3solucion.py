from datetime import date, datetime
opcion=0
datos_cliente=[]
datos_compra=[]
datos_envio=[]

while (opcion!=6):
    #print("\n\t********************************************")
    #print("\t*      Menu de Opciones Compra             *")
    #print("\t********************************************")
    #print("\t1. Datos del cliente")
    #print("\t2. Datos, cálculo Compra e impresion compra")
    #print("\t3.Impresión Cantidad de compras por turno")
    #print("\t4.Impresión valor compras por turno")
    #print("\t5. Datos de envio")
    #print("\t6. Terminar")
    #print("\t********************************************")
           
    opcion=int(input("> ")) # 1. opcion
    if (opcion>=0 and opcion<=6):
         if (opcion==1):
            i=0
            while(True):
                datos_cliente.append([])
                #print("\n\t********************************************")                
                #print("\t*              Datos del Cliente            *")
                #print("\t********************************************")
                while(True):
                    tdo_cli=str(input("> ")) #2\tTipo Doc.Identidad   -->: "))
                    if(tdo_cli == ""):
                        #print("\n\tNo puede estar vacío")
                        continue
                    else:
                        datos_cliente[i].append(tdo_cli)
                        break
                while(True):
                    ndoc_cli=str(input("> ")) #3\tNo. Doc.Identidad    -->: "))    
                    if(ndoc_cli == ""):
                        #print("\n\tNo puede estar vacío")
                        continue
                    else:
                        datos_cliente[i].append(tdo_cli)
                        break
                while(True):
                    nom_cli=str(input("> ")) #4\tNombre                -->: "))
                    if(nom_cli == ""):
                        #print("\n\tNo puede estar vacío")
                        continue
                    else:
                        datos_cliente[i].append(nom_cli)
                        break
                while(True):
                    dir_cli=str(input("> ")) #5\tDirección             -->: "))
                    if(dir_cli == ""):
                        #print("\n\tNo puede estar vacío")
                        continue
                    else:
                        datos_cliente[i].append(dir_cli)
                        break
                while(True):
                    tel_cli=str(input("> ")) #6\tNúmero telefónico     -->: "))
                    if(tel_cli == ""):
                        #print("\n\tNo puede estar vacío")
                        continue
                    else:
                        datos_cliente[i].append(tel_cli)
                        break
                while(True):
                    ciu_cli=str(input("> ")) #7\tCiudad                -->: "))
                    if(ciu_cli == ""):
                        #print("\n\tNo puede estar vacío")
                        continue
                    else:
                        datos_cliente[i].append(ciu_cli)
                        break
                while(True):
                    pai_cli=str(input("> ")) #8\tPaís                  -->: "))
                    if(pai_cli == ""):
                        #print("\n\tNo puede estar vacío")
                        continue
                    else:
                        datos_cliente[i].append(pai_cli)
                        break
                op1=int(input("> ")) #9\tIngresar Otro ? (1=Si ; 2=No) -->  "))
                if(op1==1):
                    #print("\n\t-->Datos Ingresados correctamente")
                    i+=1
                    continue
                else:
                    #print("\n\t-->Datos Ingresados correctamente")
                    break
            #print(datos_cliente)
            nro_clientes= len(datos_cliente)
            if(nro_clientes>=0):
                print(nro_clientes) #A No. de clientes: ",nro_clientes)
            else:
                print(nro_clientes) #A lista vacía")
                
         elif(opcion==2):
            # print("\n\t********************************************")                
            # print("\t* Datos, Cálculo Compra e Impresion Compra *")
            # print("\t********************************************")
            j=0
           
            op=1
            total_compra=0
            vpc=0
            v_dcto=0
            cant_prod_comprados=0
            total_c=0
            fra=1
            while(True):
                datos_compra.append([])
                print(fra) # \n\t *** Factura  No. ", fra, "***")
                datos_compra[j].append(fra)
                d=date.today()
                print(d)
                datos_compra[j].append(d)
                h=datetime.now().time()
                print(h)
                datos_compra[j].append(h)
                while(True):
                    try:
                        forma_envio=int(input("> Envio")) # 2. forma de envio
                        if(forma_envio >=1 and forma_envio<=2):
                            datos_compra[j].append(forma_envio)
                            break
                        else:
                            print("\n\tDebe ser 1=rapido o 2=normal ")
                            continue
                    except ValueError:
                        print("\n\tDebe ser numérico")
                        continue
                while(True):
                    try:
                        tipo_envio=int(input("> tipo envio")) # 3. tipo de envio
                        if(tipo_envio >=1 and tipo_envio<=3):
                            datos_compra[j].append(tipo_envio)
                            break
                        else:
                            print("\n\tDebe ser 1=Local, 2=Nacional, 3=Internal ")
                            continue
                    except ValueError:
                        print("\n\tDebe ser numérico")
                        continue
                while(True): 
                    while(True):
                        ref_p=str(input("> ref ")) # 4. referencia producto
                        if(ref_p == ""):
                            print("\n\tNo puede estar vacío")
                            continue
                        else:
                            datos_compra[j].append(ref_p)
                            break
                    while(True):
                        nombre_p=str(input("> nom")) # 5. nombre producto
                        if(nombre_p == ""):
                            print("\n\tNo puede estar vacío")
                            continue
                        else:
                            datos_compra[j].append(nombre_p)
                            break
                    while(True):
                        try:
                            cant=int(input("> cant ")) # 6. cantidad producto
                            if(cant > 0):
                                datos_compra[j].append(cant)
                                break
                            else:
                                print("\n\tDebe ser un valor positivo")
                                continue
                        except ValueError:
                            print("\n\tDebe ser numérico")
                            continue
                            
                    while(True):
                        try:
                            precio=int(input("> prec")) # 7. precio producto
                            if(precio > 0):
                                datos_compra[j].append(precio)
                                break
                            else:
                                print("\n\tDebe ser un valor positivo")
                                continue
                        except ValueError:
                            print("\n\tDebe ser numérico")
                            continue
                        
                    pc=int(cant*precio)
                    vpc=int(vpc+pc)
                    datos_compra[j].append(vpc)
                    if(cant>3):
                        dcto=int(pc*0.05)
                        v_dcto=int(v_dcto+dcto)
                    else:
                        dcto=0
                    
                    cant_prod_comprados+=1
                    datos_compra[j].append(v_dcto)    
                    # print("\n\t**************************************")                
                    # print("\tValor parcial de la compra--> $",pc)
                    # print("\t**************************************")
                    
                    if(forma_envio==1 and tipo_envio==1 and vpc>800000):
                        valor_envio=0
                    elif(forma_envio==2 and tipo_envio==1 and precio>500000):
                        valor_envio=0
                    elif(forma_envio==2 and tipo_envio==2 and precio>=1000000):
                        valor_envio=0
                    elif(forma_envio==2 and tipo_envio==3 and vpc>=2000000):
                        valor_envio=0
                    #valor envio     
                    elif(forma_envio==1 and tipo_envio==1):
                        valor_envio=8000
                    elif(forma_envio==1 and tipo_envio==2):
                        valor_envio=10000
                    elif(forma_envio==1 and tipo_envio==3):
                        valor_envio=40000
                    elif(forma_envio==2 and tipo_envio==1):
                        valor_envio=4000
                    elif(forma_envio==2 and tipo_envio==2):
                        valor_envio=5000
                    elif(forma_envio==2 and tipo_envio==3):
                        valor_envio=20000
                    
                    if(cant_prod_comprados>1 and (precio>=1000000 or precio>=2000000)):
                        valor_envio=0
                        
                    datos_compra[j].append(valor_envio)
                
                    total_compra=int(total_compra - dcto + valor_envio)
                    op2=int(input("> ")) # 8. otro producto? (1=Si ; 2=No)
                    
                    if(op2==1):
                        #datos_compra[j].append([])
                        continue
                    else:
                        break
                    
                total_c= int(total_c + vpc - v_dcto + valor_envio)
                datos_compra[j].append(total_c)
                # print("\n\t****************************************")
                # print("\t*         Resumen Compra               *")
                # print("\t****************************************")
                # print("\tValor compra             --> : $ ",vpc)
                # print("\tValor descuento          --> : $ ",v_dcto)
                # print("\tValor envio              --> : $ ",valor_envio)
                # print("\tValor final compra       --> : $ ",total_c)
                # print("\tNro. Articulos comprados --> :   ", cant_prod_comprados)
                # print("\t****************************************\n")
                print(int(vpc)) # A. valor compra
                print(int(v_dcto)) # B. descuento
                print(int(valor_envio)) # C. valor envio
                print(int(total_c)) # D. total
                
                print(datos_compra)
                
                op3=int(input("> otra compra")) # 9. otra compra? (1=Si ; 2=No)
                    
                if(op3==1):
                    fra=fra+1
                    j=j+1
                    vpc=0
                    v_dcto=0
                    valor_envio=0
                    total_c=0
                    continue
                else:
                    break
            ###
         if (opcion==3):
            #while(True):
            print("\n\t********************************************")
            print("\t*Impresión Cantidad de compras por turno        *")
            print("\t********************************************")
            cont_ct1=0
            cont_ct2=0
            while(True):
                if(len(datos_compra)!=0):
                    hora1 = datetime.strptime("12:00:00", "%X").time()
                    hora2 = datetime.strptime("23:59:59", "%X").time()
                    compras_turno=int(input("> Ingrese el Turno 1 o 2, 3=Salir ")) # (1=T1i ; 2=T2) -->  "))
                    #while(True):
                    if (compras_turno>=1 and compras_turno<=3):
                        if(compras_turno==1):
                            for i in range(0,len(datos_compra),1):
                                hora_compra=datos_compra[i][2]
                                if(hora_compra<=hora1):
                                    cont_ct1+=1
                            print("Numero de compras Turno 1: ",cont_ct1)
                            break
                    
                        elif(compras_turno==2):
                            print("turno 2  ", compras_turno)
                            for i in range(0,len(datos_compra),1):
                                hora_compra=datos_compra[i][2]
                                if(hora_compra>hora1 and hora_compra<=hora2):
                                    cont_ct2+=1
                            print("Numero de compras Turno 2: ",cont_ct2)
                            break
                        elif(compras_turno==3):
                            break
                        
                    else:
                        print("Datos incorrectos, intente de nuevo")
                        break
                else:
                    print("\tLa lista de compras está vacia" )
                    break
         elif(opcion==4):
            while(True): 
                # print("\n\t********************************************")                
                # print("\t*              Datos de Envío               *")
                # print("\t********************************************")
                tdo_env=str(input("\tTipo Doc.Identidad   -->: "))
                ndoc_env=str(input("\tNo. Doc.Identidad    -->: "))
                nom_env=str(input("\tNombre                -->: "))
                dir_env=str(input("\tDirección             -->: "))
                tel_env=str(input("\tNúmero telefónico     -->: "))
                ciu_env=str(input("\tCiudad                -->: "))
                pai_env=str(input("\tPaís                  -->: "))
                empt_env=str(input("\tEmpr.Transportadora  -->: "))
                
                op3=int(input("\tIngresar Otro ? (1=Si ; 2=No) -->  "))
                if(op3==1):
                    # print("\n\t-->Datos Ingresados correctamente")
                    continue
                else:
                    # print("\n\t-->Datos Ingresados correctamente")
                    break
         
    else:
        # print("\n---> Opcion fuera de rango (opcion 1-4)\n")
        continue
