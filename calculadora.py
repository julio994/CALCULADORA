def suma(numero1,numero2 ):
    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
    except:
        print("debes ingresar solamente numeros")
        return None
    else:
        suma=numero1+numero2
        return suma

