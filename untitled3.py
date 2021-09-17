fila = 0;
for i in range(1,lineas+1):
    fila +=2;
for j in range(lineas-i):
    print (”“,end =””)
for k in range(i,fila):
    print (k%10,end=””)
for l in range(fila-2,i-1,-1):
    print (l%10,end=””)  