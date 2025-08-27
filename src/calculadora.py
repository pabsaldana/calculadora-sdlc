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
    opcion= int(input("Ingrese opcion a trabajar: "))
    if opcion==1:
        print()
        sumar()
    elif opcion==2:
        print()
        restar()
    elif opcion==3:
        print()
        dividir()
    elif opcion==4:
        print("Calculadora para multiplicar")
        multiplicar()
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
    print()
    return
def dividir(numero1, numero2):
    print()
    return
def multiplicar():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación es: {resultado}")
    return
def elevar(numero1, numero2):
    print()
    return
def raiz_cuadrada(numero1, numero2):
    print()
    return
def tablas_multiplicar(numero1, numero2):
    print()
    return

menu()