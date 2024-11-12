'''
Jennifer Marlene Gutierrez Beteta
11 de noviembre de 2024.
Descripción:
Funciones.
'''

# Para utilizar funciones se ocupa la palabra reservada (def):

def hola(nombre):
    print(f"Hola {nombre}")
nombre = input("Ingrese nombre: ")
hola(nombre)
print("Adiós")

# Ejemplo 1:

# Se implementa la función menú.
def menu():
    print(" ")
    print("*** Ménu  ***")
    print(" ")
    print("[0].- Salir")
    print("[1].- Suma")
    print("[2].- Resta")
    print("[3].- Multiplicación")
    print("[4].- División")
    print("[5].- División entera")
    print("[6].- Exponenciación")
    print(" ")
    opcion = int(input("Ingresa una opción: "))
    return opcion

# Se implementa la función calculadora.
def calculadora(opcion,numero_1,numero_2 ):
    if opcion == 1:
        resultado = numero_1 + numero_2
    elif opcion == 2:
        resultado = numero_1 - numero_2
    elif opcion == 3:
        resultado = numero_1 * numero_2
    elif opcion == 4:
        resultado = numero_1 / numero_2
    elif opcion == 5:
        resultado = numero_1 / numero_2
    elif opcion == 6:
        resultado = numero_1 ** numero_2
    else:
        print("No valido")
    return resultado


# Se declaran las funciones.
opcion = menu()
numero_1 = float(input("Ingresa el primer número: "))
numero_2 = float(input("Ingresa el segundo número: "))
resultado = calculadora(opcion,numero_1,numero_2)
print(f"resultado: {resultado: .3f}")