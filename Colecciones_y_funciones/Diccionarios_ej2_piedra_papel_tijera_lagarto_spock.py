'''
Jennifer Marlene Gutierrez Beteta
02 de diciembre de 2024.
Descripción:
#Este programa es una versión mejorada del juego "Piedra, papel, tijeras, lagarto, Spock".
#Utiliza un diccionario para definir las reglas del juego y permite llevar un registro de victorias, empates y derrotas.'''

'''
Escribe un programa de nombre Diccionarios_ej2_piedra_papel_tijera_lagarto_spock.py que realice lo siguiente:
Este programa es una versión mejorada del juego de piedra, papel y tijeras. Las reglas se muestran en el siguiente video:
Se debe mostrar el siguiente menú:

  ***  Juego de piedra, papel, tijeras, lagarto, spock  ***
1) Piedra.
2) Papel.
3) Tijeras.
4) Lagarto.
5) Spock.
6) Ver reglas.
0) Salir.

Cualquier otro caso -> Opción no válida.
Para ello:
a) Muestre el menú en una función que pida al usuario una de las opciones.
b) Utilice un diccionario para las distintas combinaciones.
c) Realice la lógica adecuada para determinar al ganador.
d) Muestre la elección del jugador y la del cpu.
e) Muestre la cantidad de victorias, empates y derrotas.
f) Repita nuevamente el menú hasta salir.
'''

from random import random, choice # La selección aleatoria de la CPU.

# Inicialización de variables.
Opcion = None
Victorias_jugador = 0 # Contador de victorias del jugador.
Empates = 0 # Contador de empates.
Victorias_CPU = 0  # Contador de victorias del CPU.

# Opciones del juego y los resultados.
PIEDRA = "Piedra."
PAPEL = "Papel."
TIJERA = "Tijera."
LAGARTO = "Lagarto."
SPOCK = "Spock."
JUGADOR = "Gana el jugador."
EMPATE = "Empate."
CPU = "Gana la CPU."

# Función que muestra el menú de las opciones del jugador.
def Menu():
    print("  ***  Juego de piedra, papel o tijeras  ***")
    print(f"Victorias del jugador: {Victorias_jugador}, empates: {Empates} y victorias del CPU: {Victorias_CPU}  ")
    print("[0].- Salir.")
    print("[1].- Piedra.")
    print("[2].- Papel.")
    print("[3].- Tijera.")
    print("[4].- Lagarto.")
    print("[5].- Spock.")
    print("[6].- Ver reglas.")

    print()
    Opcion = int(input("Ingresa una opción: "))
    return Opcion

# Función que realiza la elección del jugador y la del CPU.
def Eleccion_jugador(Opcion_jugador):
    Lista = []
    # opción del jugador según la entrada seleccionada.
    if Opcion_jugador == 1:
        Jugador = PIEDRA
    elif Opcion_jugador == 2:
        Jugador = PAPEL
    elif Opcion_jugador == 3:
        Jugador = TIJERA
    elif Opcion_jugador == 4:
        Jugador = LAGARTO
    elif Opcion_jugador == 5:
        Jugador = SPOCK
    else:
        Jugador = None

    Lista.append(PIEDRA)
    Lista.append(PAPEL)
    Lista.append(TIJERA)
    Lista.append(LAGARTO)
    Lista.append(SPOCK)

    #CPU elige aleatoriamente entre las opciones.
    Opcion_CPU = choice(Lista)
    return Jugador,Opcion_CPU

#Diccionario que define las reglas del juego.
Piedra_papel_tijera = {(PIEDRA, TIJERA): JUGADOR,
                       (PIEDRA, PAPEL): CPU,
                       (TIJERA, PAPEL): JUGADOR,
                       (TIJERA, PIEDRA): CPU,
                       (PAPEL, PIEDRA): JUGADOR,
                       (PAPEL, TIJERA): CPU,
                       (PIEDRA, LAGARTO): JUGADOR,
                       (LAGARTO, PIEDRA): CPU,
                       (LAGARTO, SPOCK): JUGADOR,
                       (SPOCK, LAGARTO): CPU,
                       (SPOCK, TIJERA): JUGADOR,
                       (TIJERA, SPOCK): CPU,
                       (TIJERA, LAGARTO): JUGADOR,
                       (LAGARTO, TIJERA): CPU,
                       (LAGARTO, PAPEL): JUGADOR,
                       (PAPEL, LAGARTO): CPU,
                       (PAPEL, SPOCK): JUGADOR,
                       (SPOCK, PAPEL): CPU,
                       (SPOCK, PIEDRA): JUGADOR,
                       (PIEDRA, SPOCK): CPU,
                       }

while Opcion != 0: #El juego continúa mientras el jugador no elija salir.
    Opcion = Menu()
    print()
    Opcion_Jugador, Opcion_CPU = Eleccion_jugador(Opcion)  # Obtiene la elección del jugador y del CPU.

    # Se obtiene el resultado del juego usando el diccionario.
    Resultado = Piedra_papel_tijera.get((Opcion_Jugador, Opcion_CPU), EMPATE)

    if Opcion == 0: #Salir del programa.
        print("Fin del programa.")
    #Mostrar las reglas del juego.
    elif Opcion == 6:
        print("Reglas:")
        print("Selecciona una de las opciones de acuerdo a lo siguiente:")
        print("-Tijeras cortan papel.")
        print("-Papel cubre piedra.")
        print("-Piedra aplasta lagarto.")
        print("-Lagarto envenena Spock.")
        print("-Spock destruye tijeras.")
        print("-Tijeras decapitan lagarto.")
        print("-Lagarto come papel.")
        print("-Papel desaprueba Spock.")
        print("-Spock vaporiza piedra.")
        print("-Piedra aplasta tijeras.")

    # Muestra el resultado.
    elif Resultado == JUGADOR:
        Victorias_jugador += 1
        print(f"Jugador: {Opcion_Jugador} CPU: {Opcion_CPU} {JUGADOR}")
    elif Resultado == CPU:
        Victorias_CPU += 1
        print(f"Jugador: {Opcion_Jugador} CPU: {Opcion_CPU} {CPU}")
    elif Resultado == EMPATE:
        Empates += 1
        print(f"Jugador: {Opcion_Jugador} CPU: {Opcion_CPU} {EMPATE}")
    else:
        print()
        print("Opción incorrecta.")

    print()