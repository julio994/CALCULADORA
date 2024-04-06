from calculadora import suma

continuar = True

while(continuar):
    print("Calculadora")
    print("Elija la opción deseada:")
    print("1. Suma")
    print("2. Salir")

    opc = input("")
    if(opc == "1"):
        numeroUno = 0
        numeroDos = 0
        resultado = 0
        while(True):
            numeroUno = input("ingrese el primer numero: ")
            numeroDos = input("ingrese el segundo numero: ")
            resultado = suma(numeroUno,numeroDos)
            if(resultado != None):
                break
        print(f"{numeroUno}+{numeroDos}={resultado}")
    elif(opc == "2"):
        print("Calculadora cerrada...")
        continuar = False
    else:
        print("opción incorrecta")