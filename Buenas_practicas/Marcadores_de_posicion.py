'''
Jennifer Marlene Gutierrez Beteta
08 de enero de 2025.
Descripción:
Ejercicio 2, Parcial 3.
'''


def Menu_opcion(opciones):
    pass # Pass,instrucción que no hace nada (se pueden utilizar Pass o ...).

def cadena_a_entero(cadena):
    pass

def cadena_a_flotante(cadena):
    rais = NotImplementedError("Implementar la función")

opcion = Menu_opcion()
# cadena_a_entero()
# cadena_a_flotante()
while opcion!= 0:
    if opcion== 1:
        num_cadena = input("Ingresa número a convertir en entero")
        cadena_a_entero(num_cadena)
    elif opcion == 2:
        num_cadena = input("Ingresa número a convertir en flotante")
        cadena_a_flotante(num_cadena)
        while numero != None:
    elif opcion == 0:
        print("Salir...")
    else:
        print("Opciónn no valida...")