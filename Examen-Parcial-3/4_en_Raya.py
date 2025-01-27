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
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]} | {tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("--+---+---+---+---+--")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]} | {tablero[9]} | {tablero[10]} | {tablero[11]}")
    print("--+---+---+---+---+--")
    print(f"{tablero[12]} | {tablero[13]} | {tablero[14]} | {tablero[15]} | {tablero[16]} | {tablero[17]}")
    print("--+---+---+---+---+--")
    print(f"{tablero[18]} | {tablero[19]} | {tablero[20]} | {tablero[21]} | {tablero[22]} | {tablero[23]}")
    print("--+---+---+---+---+--")
    print(f"{tablero[24]} | {tablero[25]} | {tablero[26]} | {tablero[27]} | {tablero[28]} | {tablero[29]}")
    print("--+---+---+---+---+--")
    print(f"{tablero[30]} | {tablero[31]} | {tablero[32]} | {tablero[33]} | {tablero[34]} | {tablero[35]}")
    #print("--+---+---+---+---+--")
    print(f"{tablero[36]} | {tablero[37]} | {tablero[38]} | {tablero[39]} | {tablero[40]} | {tablero[41]}")

def Verificar_ganador():
    # Combinaciones ganadoras
    combinaciones = [
        [0, 1, 2,3], [1,2,3,4], [2,3,4,5],  # Filas
        [6,7,8,9], [7,8,9,10], [8,9,10,11],
        [12,13,14,15],[13,14,15,16],[14,15,16,17],
        [18,19,20,21],[19,20,21,22],[20,21,22,23],
        [24,25,26,27],[25,26,27,28],[26,27,28,29],
        [30,31,32,33],[31,32,33,34],[32,33,34,35],
        [36,37,38,39],[37,38,39,40],[38,39,40,41],
        [0,6,12,18,24,30,36],[1,7,13,19,25,31,37]
             # Diagonales
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
