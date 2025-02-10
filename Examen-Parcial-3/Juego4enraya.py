import random

# Tablero inicializado con espacios vacíos
tablero = [" "] * 42

def Num_de_jugadores() -> int:
    '''
    Solicita al usuario el número de jugadores y valida la entrada.
    '''
    while True:
        print("Bienvenido al juego del Gato")
        print("[1].- Jugar con cpu")
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
    Imprime el tablero.
    '''
    print(f"{tablero[36]} | {tablero[37]} | {tablero[38]} | {tablero[39]} | {tablero[40]} | {tablero[41]}")
    print(f"{tablero[30]} | {tablero[31]} | {tablero[32]} | {tablero[33]} | {tablero[34]} | {tablero[35]}")
    print(f"{tablero[24]} | {tablero[25]} | {tablero[26]} | {tablero[27]} | {tablero[28]} | {tablero[29]}")
    print(f"{tablero[18]} | {tablero[19]} | {tablero[20]} | {tablero[21]} | {tablero[22]} | {tablero[23]}")
    print(f"{tablero[12]} | {tablero[13]} | {tablero[14]} | {tablero[15]} | {tablero[16]} | {tablero[17]}")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]} | {tablero[9]} | {tablero[10]} | {tablero[11]}")
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]} | {tablero[3]} | {tablero[4]} | {tablero[5]}")


def Verificar_ganador()-> bool:
    '''
    Verifica si hay un ganador.
    :return: True si hay un ganador, False en caso contrario.
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

    # Verificar combinaciones
    for c in combinaciones:
        if tablero[c[0]] == tablero[c[1]] == tablero[c[2]] == tablero[c[3]] != " ":
            return True
    return False

def verificar_empate(tablero: list) -> bool:
    '''
    Verifica si el juego ha terminado en empate.
    Un empate ocurre cuando no hay casillas vacías en el tablero.
    '''
    return " " not in tablero


def obtener_jugada_cpu()-> int:
    '''
    Genera una jugada aleatoria para la CPU.
    Busca una columna válida (no llena) y selecciona la fila más baja disponible en esa columna.
    :return: Posición en el tablero para la jugada de la CPU.
    '''
    while True:
        columna = random.randint(0, 5)
        for fila in range(6):  # Busca la primera casilla vacía en la columna empezando desde abajo
            posicion = columna + fila * 6
            if tablero[posicion] == " ":
                return posicion


def Turno_computadora()-> None:
    '''
    La computadora elige una columna aleatoria válida.
    '''
    posicion = obtener_jugada_cpu()
    if posicion is not None:
        tablero[posicion] = "O"
        print("La computadora ha jugado.")


def Jugar_cpu()-> None:
    '''
    Función principal para jugar contra la CPU.
    '''
    jugador = "X"
    while True:
        Imprimir_tablero()
        if jugador == "X":
            columna = input(f"Jugador {jugador}, elige una columna (1-6): ")

            # Validar si la entrada es un número y está en el rango correcto
            if not columna.isdigit() or not (1 <= int(columna) <= 6):
                print("Entrada inválida. Ingresa un número del 1 al 6.")
                continue

            columna = int(columna) - 1
            for fila in range(6):  # Busca la primera casilla vacía
                posicion = columna + fila * 6
                if tablero[posicion] == " ":
                    tablero[posicion] = jugador
                    break
            else:
                print("Columna llena. Intenta en otra columna.")
                continue
        else:
            Turno_computadora()

        # Verificar ganador
        if Verificar_ganador():
            Imprimir_tablero()
            print(f"Jugador {jugador} ha ganado!")
            return

        # Verificar empate
        if verificar_empate(tablero):
            Imprimir_tablero()
            print("El juego ha terminado en empate.")
            return

        # Cambiar de jugador
        jugador = "O" if jugador == "X" else "X"


def Jugar_jugadores()-> None:
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

        # Verificar empate
        if verificar_empate(tablero):
            Imprimir_tablero()
            print("El juego ha terminado en empate.")
            return

        # Cambiar de jugador
        jugador = "O" if jugador == "X" else "X"


def Juego_4raya() -> None:
    opcion = None  # Apliqué lo de la variable None.

    while opcion != 0:
        opcion = Num_de_jugadores()

        if opcion == 1:
            Jugar_cpu()
            break
        elif opcion == 2:
            Jugar_jugadores()
            break
        else:
            print("Se ha salido del juego...")
            break

if __name__ == "__main__":
    Juego_4raya()
