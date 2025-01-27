'''
Jennifer Marlene Gutierrez Beteta
22 de enero de 2025.
Descripción:
Examen Parcial 3: Juego 4 en raya.
'''

tablero = [" "] * 42 # Se crea una lista para 9 elementos, inicializada en espacios en blanco.

def Imprimir_tablero():
    '''
    Función para la impresion del tablero.
    '''
    print(f"{tablero[36]} | {tablero[37]} | {tablero[38]} | {tablero[39]} | {tablero[40]} | {tablero[41]}")
    print(f"{tablero[30]} | {tablero[31]} | {tablero[32]} | {tablero[33]} | {tablero[34]} | {tablero[35]}")
    print(f"{tablero[24]} | {tablero[25]} | {tablero[26]} | {tablero[27]} | {tablero[28]} | {tablero[29]}")
    print(f"{tablero[18]} | {tablero[19]} | {tablero[20]} | {tablero[21]} | {tablero[22]} | {tablero[23]}")
    print(f"{tablero[12]} | {tablero[13]} | {tablero[14]} | {tablero[15]} | {tablero[16]} | {tablero[17]}")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]} | {tablero[9]} | {tablero[10]} | {tablero[11]}")
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]} | {tablero[3]} | {tablero[4]} | {tablero[5]}")

def Verificar_ganador():
    # Combinaciones ganadoras
    combinaciones = [
        [0,6,12,18],[6,12,18,24],
    ]
    for c in combinaciones:
        if tablero[c[0]] == tablero[c[1]] == tablero[c[2]] == tablero[c[3]]!= " ":  # Recorre cada combinación en la lista.
            return True
    return False

def Jugar():
    jugador = "X"
    for turno in range(9):
        Imprimir_tablero()
        posicion = int(input(f"Jugador {jugador}, elige una posición (1-7): ")) - 1
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
