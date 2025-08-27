def menu():
    print("Welcome to my calculator")
    print("1) Suma")
    print("2) Resta")
    print("3) Division")
    print("4) Multiplicacion")
    print("5) Elevar")
    print("6) raiz")
    print("7) Tabla de multiplicar")
    print("8) Salir")
    opcion= int(input("Ingrese opcion a trabajar"))
    if opcion==1:
        print()
        sumar()
    elif opcion==2:
        print()
        restar()
    elif opcion==3:
        print()
        multiplicar()
    elif opcion==4:
        print()
        dividir()
    elif opcion==5:
        print()
        elevar()
    elif opcion==6:
        print()
        raiz_cuadrada()
    elif opcion==7:
        print()
        tablas_multiplicar()
    elif opcion==8:
        print()
    else:
        print("Opcion no encontrada")

def sumar(numero1, numero2):
    print()
    return
def restar(numero1, numero2):
    print('Ingresa los numeros a restar:')
    numero1 = int(input('Numero 1: '))
    numero2 = int(input('Numero 2: '))
    resu = numero1 - numero2
    print(f'{numero1} - {numero2} = {numero1 - numero2}')
    return resu
def dividir(numero1, numero2):
    print()
    return
def multiplicar(numero1, numero2):
    print()
    return
def elevar(numero1, numero2):
    print()
    return
def raiz_cuadrada(numero1):
    numero1 = int(input('Numero 1: '))
    raiz_cuadrada = numero1**0.5
    print(f"la raíz cuadrada de {numero1} es: {raiz_cuadrada}")
    print()
    return
def tablas_multiplicar(numero1, numero2):
    print()
    return
