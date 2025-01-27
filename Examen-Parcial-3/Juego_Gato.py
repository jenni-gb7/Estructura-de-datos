'''
Jennifer Marlene Gutierrez Beteta
22 de enero de 2025.
Descripción:
Examen Parcial 3: Juego del ahorcado.
'''

def Num_de_jugadores():
    print()
    print("Bienvenido al juego del Gato")
    print("[1].- Jugar con 1 jugador")
    print("[2].- Jugar con 2 jugadores")
    print("[0].- Salir")

    selccion = int(input("Ingresa una de las opciones: "))
    return selccion

tablero = [" "] * 9 # Se crea una lista para 9 elementos, inicializada en espacios en blanco.

def Imprimir_tablero():
    '''
    Función para la impresion del tablero.
    '''
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]}")
    print("--+---+--")
    print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("--+---+--")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")

def Verificar_ganador():
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

def Jugar():
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

if __name__ == "__main__":
    Jugar()









