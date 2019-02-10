#Entrada de datos

import modejercicio1

#Entrada de datos:altura 
altura=altura=modejercicio1.validacion("Introduzca la altura de nuevo: ")

#Procesamiento de datos:altura
while not modejercicio1.esdecimal(altura):
       altura=modejercicio1.validacion("Introduzca la altura de nuevo: ")
print("La altura es:",altura)
        
#Entrada de datos:base              
base=modejercicio1.validacion("Introduzca la base: ")
 
#Procesamiento de datos:base
while not modejercicio1.esdecimal(base):     
    base=input("Introduzca la base de nuevo: ")
    base=base.replace(",",".")
print("La base es:",base)

#Imprime resultado
altura=float(altura)
base=float(base)

area=round((altura*base)/2,2)
print("El área del triángulo es:", area)




                     


                     
            