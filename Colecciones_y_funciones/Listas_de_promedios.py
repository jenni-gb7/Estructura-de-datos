'''
Jennifer Marlene Gutierrez Beteta
13 de noviembre de 2024.
Descripción:
Ejericio 3, Listas de promedio.
'''

print("*** Promedios del parcial 1  ***")

# Se implementa la función menú.
def menu():
    print(" ")
    print("*** Ménu  ***")
    print(" ")
    print("[0].- Salir")
    print("[1].- Ver calificación de alumno")
    print("[2].- Ver promedio de alumno")
    print("[3].- Añadir alumno")
    print("[4].- Eliminsr alumno")
    print("[5].- Ver promedio grupal")
    print(" ")
    opcion = int(input("Ingresa una opción: "))
    return opcion

def promedio(opcion):
    if opcion == 1:
        print(calificaciones)
        print(promedio)
    elif opcion == 2:
        productos.pop()
        print(productos)
        print()

        cantidad.pop()
        print(cantidad)
        print()

    else:
        print("No valido")
    return productos,cantidad


opcion = menu()
calificaciones = []
promedio = []