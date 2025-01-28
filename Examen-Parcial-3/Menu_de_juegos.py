'''
Jennifer Marlene Gutierrez Beteta
22 de enero de 2025.
Descripción:
Examen Parcial 3: Menu
'''

import Juego_Ahorcado
import Juego_Gato
import Juego_4_en_raya

def Menu_juegos() -> int:
    '''
    Solicita al usuario el número de jugadores y valida la entrada.
    '''
    while True:
        print("Bienvenido al menu de juegos")
        print("[1].- Ahorcado")
        print("[2].- Gato")
        print("[0].- Salir")
        opcion = input("Ingresa una de las opciones: ")
        if opcion.isnumeric():  # Verificar si la entrada es un número.
            opcion = int(opcion)
            if opcion in (0, 1, 2):
                return opcion
        print("Por favor, ingresa una opción válida.")


def Juegos() -> None:
    opcion = None  #  Apliqué lo de la variable None
    while opcion  != 0:
        opcion = Menu_juegos

        if opcion  == 1:
            Juego_Ahorcado
        elif opcion == 2:
            Dos_Jugardores()
        else:
            print("Opción inválida. Debes ingresar 1 o 2.")
    print("Se a salido del juego.....")