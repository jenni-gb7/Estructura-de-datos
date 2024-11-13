'''
Jennifer Marlene Gutierrez Beteta
13 de noviembre de 2024.
Descripción:
Ejericio 2, Listas de compras.
'''

print("*** Videos de You Tube  ***")

# Se implementa la función menú.
def menu():
    print(" ")
    print("*** Ménu  ***")
    print(" ")
    print("[0].- Salir")
    print("[1].- Añadir productos a la lista")
    print("[2].- Eliminar productos de la lista")
    print(" ")
    opcion = int(input("Ingresa una opción: "))
    return opcion

def compras(opcion):
    if opcion == 1:
        productos = [productos]
        productos = input("Ingrese el nombre del producto:")
        cantidad = [cantidad]
        cantidad = int(input("Ingrese la cantidad del producto:"))

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
productos = []
cantidad = []