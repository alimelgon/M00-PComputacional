#Valido si el dato introducido es numérico
def esdecimal(valor):
    try:
        float(valor)
        return True
    except:
        return False

#Si el dato no es numérico, lo pido de nuevo
def validacion(mensaje):
    coordenada=input(mensaje)
    coordenada=coordenada.replace(",",".")
    return coordenada
    
    