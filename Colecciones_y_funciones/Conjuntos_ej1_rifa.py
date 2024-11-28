'''
Jennifer Marlene Gutierrez Beteta
26 de noviembre de 2024.
Descripción:
Este programa es una rifa, en donde se registra el correo electrónico y solamente permite ingresar un correo por participante.
'''
'''Se debe mostrar el siguiente menú:

  ***  Rifa de una computadora  ***

1) Ver correos de participantes.

2) Agregar correo de participante.

3) Eliminar correo de participante.

4) Seleccionar ganador.

0) Salir.

Cualquier otro caso -> Opción no válida.

Para ello:

a) Utilice un conjunto para almacenar los correos de los participantes.

b) Utilice un valor aleatorio utilizando la función random.choice(lista). Notar que hay que convertir primero a una lista.'''

print()
print("***  Rifa de una computadora  ***")
print()
opcion = None

correos = set()

def Menu()
    print()
    print("[0].- Salir")
    print("[1].- Ver correos de participantes.")
    print("[2].- Agregar correo de participante.")
    print("[3].- Eliminar correo de participante.")
    print("[4].- Seleccionar ganador.")
    print()
    opcion = int(input("Ingresa una opción: "))
    return opcion
    if opcion == 1:
        numero = 1
        for Correo in Correos:
            print(f"{numero}._ {Correo}")
            numero += 1
        else:
            print(f"No hay participantes para mostrar.")
    elif opcion == 2:
        Lista_correos = input("Agrega tu correo electronico:")
        Conjuntos_correos = list(Lista_correos)
        Lista_correos.add(Conjuntos_correos)

        print()
    elif opcion == 3:
        Correo_eliminar = input("Agrega tu correo electronico:")
        Conjuntos_correos.remove(Correo_eliminar)
    elif opcion == 4:
        print("El correo ganador es:")

    else:
        print()
        print("Opción incorrecta")
        print()
print()
print("Saliendo del programa...")