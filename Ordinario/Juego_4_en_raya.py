'''
Jennifer Marlene Gutierrez Beteta
22 de enero de 2025.
Descripción:
Examen Parcial 3: 4 en raya.

'''# Colores
AZUL = "\033[94m"
RESET = "\033[0m"
import random

def inicializar_tablero() -> list:
    """
    Crea un tablero vacío para el juego 4 en raya.
    :return: Lista con 42 espacios representando el tablero vacío.
    """
    return [" "] * 42


def Num_de_jugadores() -> int:
    """
    Solicita al usuario el número de jugadores y valida la entrada.
    :return: Entero que indica el modo de juego (0: Salir, 1: Contra CPU, 2: Dos jugadores).
    """
    CUATRO_EN_RAYA = """
              EEEEE  N   N     RRRR   AAAAA  Y   Y  AAAAA
           4  E      NN  N     R   R  A   A   Y Y   A   A
        4444  EEEE   N N N     RRRR   AAAAA    Y    AAAAA
           4  E      N  NN     R  R   A   A    Y    A   A
           4  EEEEE  N   N     R   R  A   A    Y    A   A
        """
    # Imprimir el texto con colores
    print(AZUL + CUATRO_EN_RAYA + RESET)

    while True:
        print("Bienvenido al juego 4 en raya")
        print("[1].- Jugar con CPU")
        print("[2].- Jugar con 2 jugadores")
        print("[0].- Salir")
        opcion = input("Ingresa una de las opciones: ")
        if opcion.isnumeric():
            opcion = int(opcion)
            if opcion in (0, 1, 2):
                return opcion
        print("Por favor, ingresa una opción válida.")


def Imprimir_tablero(tablero: list) -> None:
    """
    Imprime el estado actual del tablero en la consola.
    :param tablero: Lista representando el tablero de juego.
    """
    for fila in range(6, -1, -1):
        print(" | ".join(tablero[fila * 6:(fila + 1) * 6]))
    print("-" * 25)


def Verificar_ganador(tablero: list) -> bool:
    """
    Verifica si hay un ganador en el juego.
    :param tablero: Lista representando el tablero de juego.
    :return: True si hay un ganador, False en caso contrario.
    """
    combinaciones = []
    for fila in range(0, 42, 6):
        for col in range(3):
            combinaciones.append([fila + col, fila + col + 1, fila + col + 2, fila + col + 3])
    for col in range(6):
        for fila in range(18):
            combinaciones.append([fila + col, fila + col + 6, fila + col + 12, fila + col + 18])
    for fila in range(18):
        for col in range(3):
            combinaciones.append([fila + col, fila + col + 7, fila + col + 14, fila + col + 21])
    for fila in range(18):
        for col in range(3, 6):
            combinaciones.append([fila + col, fila + col + 5, fila + col + 10, fila + col + 15])

    for c in combinaciones:
        if tablero[c[0]] == tablero[c[1]] == tablero[c[2]] == tablero[c[3]] != " ":
            return True
    return False


def verificar_empate(tablero: list) -> bool:
    """
    Verifica si el juego ha terminado en empate.
    :param tablero: Lista representando el tablero de juego.
    :return: True si todas las casillas están ocupadas, False en caso contrario.
    """
    return " " not in tablero


def Jugar_jugadores() -> None:
    """
    Función principal para jugar con dos jugadores.
    """
    tablero = inicializar_tablero()
    jugador = "X"
    while True:
        Imprimir_tablero(tablero)
        columna = input(f"Jugador {jugador}, elige una columna (1-6): ")
        if not columna.isdigit() or not (1 <= int(columna) <= 6):
            print("Entrada inválida. Ingresa un número del 1 al 6.")
            continue
        columna = int(columna) - 1
        for fila in range(6):
            posicion = columna + fila * 6
            if tablero[posicion] == " ":
                tablero[posicion] = jugador
                break
        else:
            print("Columna llena. Intenta en otra columna.")
            continue
        if Verificar_ganador(tablero):
            Imprimir_tablero(tablero)
            print(f"¡Jugador {jugador} ha ganado!")
            return
        if verificar_empate(tablero):
            Imprimir_tablero(tablero)
            print("El juego ha terminado en empate.")
            return
        jugador = "O" if jugador == "X" else "X"


def Juego_4raya() -> None:
    """
    Ejecuta el juego 4 en raya, permitiendo repetir rondas hasta que el usuario decida salir.
    """
    while True:
        opcion = Num_de_jugadores()
        if opcion == 1:
            Jugar_jugadores()
        elif opcion == 2:
            Jugar_jugadores()
        else:
            print("Se ha salido del juego...")
            break


if __name__ == "__main__":
    Juego_4raya()
