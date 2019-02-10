import modejercicio2
#defino listas vacías
prices=[]
cantidades=[]
totales=[]
 
long=len(prices)
indice=0
long=0

#Introduzco primer valor para precio y cantidad
print("Pulse 0 para salir")
precio=input("Precio")
precio=precio.replace(",",".")
while not modejercicio2.esdecimal(precio):
    
    precio = input("Introduzca un valor numerico para precio:")
    precio=precio.replace(",",".")
    
cantidad=input("Cantidad ")
cantidad=cantidad.replace(",",".")
while not modejercicio2.esentero(cantidad):    
        cantidad = input("Introduzca un valor numerico para cantidad:")
        cantidad=cantidad.replace(",",".")
        
#Introduzco primer carácter en las listas
total=float(precio)*int(cantidad)
prices.append(precio)
cantidades.append(cantidad)
totales.append(total)       
indice=1

#Introduzco precio y cantidad
while (float(precio)>0 and int(cantidad)>0):
       
    precio=input("Precio")
    precio=precio.replace(",",".")
    while not modejercicio2.esdecimal(precio):
    
        precio = input("Introduzca un valor numerico para precio:")
        precio=precio.replace(",",".")
    
    
                   
    cantidad=input("Cantidad ")
    cantidad=cantidad.replace(",",".")
 
    while not modejercicio2.esentero(cantidad):    
        cantidad = input("Introduzca un valor numerico para cantidad:")
        cantidad=cantidad.replace(",",".")
                   
    total=float(precio)*int(cantidad)
    prices.append(precio)
    cantidades.append(cantidad)
    totales.append(total)
    indice+=1
    long+=1

  
  
#Cuando precio o cantidad es 0, salgo del bucle e imprimo el resultado
print("Se ha introducido un 0 en precio o en cantidad")
print("")
sumat=0
sumac=0
for indice in range(0, long):
    sumat+=totales[indice]
    sumac+=int(cantidades[indice])
    if int(cantidades[indice])==1:    
        print(prices[indice],"€ -",cantidades[indice], "unidad -", totales[indice],"€")
    else:
        print(prices[indice],"€ -",cantidades[indice], "unidades -", totales[indice],"€")
        
print("---------------------")
print("Total: ", sumat,"€")
print ("Unidades:",sumac)
 


    


    
 





