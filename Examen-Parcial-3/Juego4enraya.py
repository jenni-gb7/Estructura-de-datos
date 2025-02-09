'''
Jennifer Marlene Gutierrez Beteta
22 de enero de 2025.
Descripción:
Examen Parcial 3: Juego 4 en raya.
'''

tablero = [" "] * 42  # Se crea una lista para 42 elementos, inicializada en espacios en blanco.

def Imprimir_tablero():
    '''
    Función para la impresión del tablero.
    '''
    print(f"{tablero[36]} | {tablero[37]} | {tablero[38]} | {tablero[39]} | {tablero[40]} | {tablero[41]}")
    print(f"{tablero[30]} | {tablero[31]} | {tablero[32]} | {tablero[33]} | {tablero[34]} | {tablero[35]}")
    print(f"{tablero[24]} | {tablero[25]} | {tablero[26]} | {tablero[27]} | {tablero[28]} | {tablero[29]}")
    print(f"{tablero[18]} | {tablero[19]} | {tablero[20]} | {tablero[21]} | {tablero[22]} | {tablero[23]}")
    print(f"{tablero[12]} | {tablero[13]} | {tablero[14]} | {tablero[15]} | {tablero[16]} | {tablero[17]}")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]} | {tablero[9]} | {tablero[10]} | {tablero[11]}")
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]} | {tablero[3]} | {tablero[4]} | {tablero[5]}")

def Verificar_ganador():
    '''
    Función para verificar si hay un ganador.
    '''
    combinaciones = []

    # Horizontales
    for fila in range(0, 42, 6):
        for col in range(3):
            combinaciones.append([fila + col, fila + col + 1, fila + col + 2, fila + col + 3])

    # Verticales
    for col in range(6):
        for fila in range(18):
            combinaciones.append([fila + col, fila + col + 6, fila + col + 12, fila + col + 18])

    # Diagonales (\)
    for fila in range(18):
        for col in range(3):
            combinaciones.append([fila + col, fila + col + 7, fila + col + 14, fila + col + 21])

    # Diagonales (/)
    for fila in range(18):
        for col in range(3, 6):
            combinaciones.append([fila + col, fila + col + 5, fila + col + 10, fila + col + 15])

    # Verificar las combinaciones
    for c in combinaciones:
        if tablero[c[0]] == tablero[c[1]] == tablero[c[2]] == tablero[c[3]] != " ":
            return True
    return False

def Jugar():
    '''
    Función principal para jugar.
    '''
    jugador = "X"
    while True:
        Imprimir_tablero()
        columna = input(f"Jugador {jugador}, elige una columna (1-6): ")

        # Validar si la entrada es un número y está en el rango correcto
        if not columna.isdigit() or not (1 <= int(columna) <= 6):
            print("Entrada inválida. Ingresa un número del 1 al 6.")
            continue

        columna = int(columna) - 1  # Convertir a índice de la lista
        # Colocar la ficha en la posición más baja disponible de la columna
        for fila in range(6):
            posicion = columna + fila * 6
            if tablero[posicion] == " ":
                tablero[posicion] = jugador
                break
        else:
            print("Columna llena. Intenta en otra columna.")
            continue

        # Verificar ganador
        if Verificar_ganador():
            Imprimir_tablero()
            print(f"¡Jugador {jugador} ha ganado!")
            return

        # Cambiar de jugador
        jugador = "O" if jugador == "X" else "X"

if __name__ == "__main__":
    Jugar()
