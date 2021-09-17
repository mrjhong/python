
#codigo, nombre, genero, carrera y promedio

#estudiantes mayor promedio, cuantos mujeres , cuantos hombres 

diccionario = {}
lista = []
i = 0
cent= 1
while(cent != 0):

    codigo = input("Codigo ")
    nombre = input("nombre ")
    genero = input("genero ")
    carrera = input("Carrera ")
    promedio = float(input("promedio "))
    
    estudiantes = {"codigo":codigo,
                    "nombre":nombre,
                    "genero":genero,
                    "carrera":carrera,
                    "promedio":promedio}
    
    diccionario.update({i:estudiantes})
    i += 1
    
    cent= int(input("1.SI o 0.No"))

print(diccionario)

# =============================================================================
# mayor = -1 # uno que no este entre los datos analizar, para que tome como mayor mi primer item
# 
# for i in range (0,len(lista),1):
#     m = lista[i]["promedio"] 
#     if m > mayor:
#         mayor = m
#         e = lista[i]["nombre"] #Toma la el mismo diccionario donde esta el > promedio y de a
#         
# print("El promedio mayor es ",mayor, "El estudiantes ", e)
# 
# cm = 0
# ch = 0
# cont_pila = 0
# for i in range (0,len(lista),1):
#     cant_genero = lista[i]["genero"]
#     if cant_genero == "femenino":
#         cm += 1
#         pro = lista[i]["promedio"]
#         if pro > 4 :
#             cont_pila += 1
#             
#             
#     else:
#         if cant_genero == "masculino":
#             ch += 1
#     
# print("Cantidad de mujeres ",cm)
# print("Cantidad de hombres ",ch)
# if cont_pila >= 1:
#     print("Hay al menos una mujer pila ")
# print("Hay ",cont_pila," mujeres pilas ")
# 
# =============================================================================
        
        
    











    