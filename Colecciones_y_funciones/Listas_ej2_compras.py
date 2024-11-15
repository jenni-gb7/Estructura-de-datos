'''
Jennifer Marlene Gutierrez Beteta
13 de noviembre de 2024.
Descripción:
Ejericio 2, Listas de compras.
'''


productos = []
cantidades = []
opcion  = None
contador = 0
while opcion != 0:
    print("*** Listas de compras**+")
    print(" ")
    print("[0].- Salir")
    print("[1].- Ver lista de compras")
    print("[2].- Añadir productos a la lista")
    print("[3].- Eliminar productos de la lista")
    print(" ")
    opcion  = int(input("Ingresa una opción: "))
    if opcion   == 1:
        numero = 0
        for producto in productos:
            print(f"Cantidad: {cantidades[numero]} Producto: {producto}")
            numero += 1
    elif opcion == 2:
        print()
        producto_anadido = input("Ingrese el producto: ")
        cantidad_anadida = input("Ingrese la cantidad del producto: ")
        productos.append(producto_anadido)
        cantidades.append(cantidad_anadida)
        contador += 1
        print()
    elif opcion == 3:
        eliminar_producto = input("Ingrese el producto que desea eliminar: ")
        numero_producto = 0

        while productos[numero_producto] != eliminar_producto:
            numero_producto += 1

        productos.remove(eliminar_producto)
        del cantidades[numero_producto]

    else:
        print()
        print("Opción incorrecta")
        print()
print()
print("Saliendo del programa...")



