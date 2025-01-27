'''
Jennifer Marlene Gutierrez Beteta
22 de enero de 2025.
Descripción:
Examen Parcial 3: Juego del ahorcado.
'''

import random

tablero = [" "] * 9  # Se crea una lista para 9 elementos, inicializada en espacios en blanco.
def Num_de_jugadores() -> int:
    '''
    Solicita al usuario el número de jugadores y valida la entrada.
    '''
    while True:
        print("Bienvenido al juego del Gato")
        print("[1].- Jugar con 1 jugador")
        print("[2].- Jugar con 2 jugadores")
        print("[0].- Salir")
        opcion = input("Ingresa una de las opciones: ")
        if opcion.isnumeric():  # Verificar si la entrada es un número.
            opcion = int(opcion)
            if opcion in (0, 1, 2):
                return opcion
        print("Por favor, ingresa una opción válida.")


def Imprimir_tablero()-> None:
    '''
    Función para la impresion del tablero.
    '''
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]}")
    print("--+---+--")
    print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("--+---+--")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")

def Verificar_ganador():
    '''
    Función para verificar ganador.
    '''
    # Combinaciones ganadoras
    combinaciones = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for c in combinaciones:
        if tablero[c[0]] == tablero[c[1]] == tablero[c[2]] != " ":  # Recorre cada combinación en la lista.
            return True
    return False

def Un_Jugador()-> None:
    '''
    Función para 2 jugadores.
    '''
    jugador = "X"  # El jugador siempre juega con "X"
    cpu = "O"  # La CPU juega con "O"

    for turno in range(9):
        Imprimir_tablero()

        if jugador == "X":  # Turno del jugador
            posicion = int(input(f"Jugador {jugador}, elige una posición (1-9): ")) - 1
            if tablero[posicion] == " ":
                tablero[posicion] = jugador
            else:
                print("Posición ocupada, intenta de nuevo.")
                continue
        else:  # Turno de la CPU
            print("Turno de la CPU...")
            posicion = random.choice([i for i, casilla in enumerate(tablero) if casilla == " "])    # Función que te permite iterar sobre una lista.
            tablero[posicion] = cpu

        # Verifica si alguien ganó
        if Verificar_ganador():
            Imprimir_tablero()
            print(f"¡{jugador} ha ganado!")
            return

        # Cambia el turno
        jugador = "O" if jugador == "X" else "X"

    # Si se llega aquí, es un empate
    Imprimir_tablero()
    print("¡Es un empate!")

def Dos_Jugardores()-> None:
    '''
    Función para 2 jugadores.
    '''
    jugador = "X"
    for turno in range(9):
        Imprimir_tablero()
        posicion = int(input(f"Jugador {jugador}, elige una posición (1-9): ")) - 1
        if tablero[posicion] == " ":
            tablero[posicion] = jugador
            if Verificar_ganador():
                Imprimir_tablero()
                print(f"¡Jugador {jugador} ha ganado!")
                return
            jugador = "O" if jugador == "X" else "X"    # Cambia el jugador de X a 0, o visevera.
        else:
            print("Posición ocupada, intenta de nuevo.")
    Imprimir_tablero()
    print("¡Es un empate!")
#
def Juego_Gato() -> None:
    opcion = None  #  Apliqué lo de la variable None
    while opcion  != 0:
        opcion = Num_de_jugadores()

        if opcion  == 1:
            Un_Jugador()
        elif opcion == 2:
            Dos_Jugardores()
        else:
            print("Opción inválida. Debes ingresar 1 o 2.")
    print("Se a salido del juego.....")

if __name__ == "__main__":
    Juego_Gato()









