def esdecimal(valor):
    try:
        float(valor)
        resultado=True
    except:
        resultado = False
    return resultado


def esentero(valor):
    try:
        int(valor)
        resultado=True
    except:
        resultado=False 
    return resultado

  