'''
Jennifer Marlene Gutierrez Beteta
12 de noviembre de 2024.
Descripción:
.
'''

print("*** Videos de You Tube  ***")

# Se implementa la función menú.
def menu():
    print(" ")
    print("*** Ménu  ***")
    print(" ")
    print("[0].- Salir")
    print("[1].- Ver lista de videos por añadidos ")
    print("[2].- Ordenar por orden de A-Z ")
    print("[3].- Ordenar por orden de Z-A ")
    print("[4].- Añadir video")
    print("[5].- Añadir varios videos")
    print("[6].- Eliminar video")
    print(" ")
    opcion = int(input("Ingresa una opción: "))
    return opcion

# Se implementa la función calculadora.
def videos(opcion):
    if opcion == 1:
        alumnos = []
        print(alumnos)
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
        print("Saliendo del programa")
    return resultado


# Se declaran las funciones.
opcion = menu()
alumnos = []