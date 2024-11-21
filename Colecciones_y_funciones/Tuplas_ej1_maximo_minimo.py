'''
Jennifer Marlene Gutierrez Beteta
21 de noviembre de 2024.
Descripción:
Ejercicio 1 Tuplas.
Este programa muestra el valor máximo y mínimo de una lista de números. En este caso, la tupla se utiliza para devolver los valores máximo y mínimo de la función.
.
'''
from Sentencias_de_control.Sentencias_ejercicio1 import num_1

'''
Se debe mostrar el siguiente menú:

  ***  Valor máximo y mínimo de una lista de números del usuario  ***

1) Ver lista de números.

2) Añadir número a la lista.

3) Determinar el valor máximo y mínimo de la lista de números.

0) Salir.

Cualquier otro caso -> Opción no válida.'''

def menu1():
    print(" ***  Valor máximo y mínimo de una lista de números del usuario  ***")
    print()
    print("[0].- Salir")
    print("[1].- Ver listas de de números.")
    print("[2].- Añadir número a la lista.")
    print("[3].- Determinar el valor máximo y mínimo de la lista de números.")
    print()
    opcion_1 = int(input("Ingresa una opción:"))
    return opcion_1


def valores(opcion_1):
    if opcion_1 == 1:
        if Lista_de_num == 0 :
            print("No hay números para mostrar.")
        else:
            print(Lista_de_num, end=", ")
    elif opcion_1 == 2:
        num_1 = int(input("Ingresa un número:"))
        num_1 = Lista_de_num

    elif opcion_1 == 3:

    else:
        print("No válido.")

    return
opcion_1 = menu1()