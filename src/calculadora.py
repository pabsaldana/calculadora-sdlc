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
        print("Calculadora para dividir:")
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
    print()
    return
def dividir():
    print("Ingrese los valores correspondientes")
    numero1 = int(input("Ingrese el dividendo: "))
    numero2 = int(input("Ingrese el divisor: "))
    print("Calculando.....")
    try:
        division = numero1 / numero2
        print("El valor de la division es: ")
        return round(division, 3)
    except ZeroDivisionError:
        print("No se puede dividir entre 0!!!")
def multiplicar(numero1, numero2):
    print()
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