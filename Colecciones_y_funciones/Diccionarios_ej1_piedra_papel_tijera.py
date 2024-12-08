'''
Jennifer Marlene Gutierrez Beteta
02 de diciembre de 2024.
Descripción:
Este programa es una versión del juego "Piedra, papel o tijeras" que utiliza un diccionario.
Permite registrar las victorias del jugador, los empates y las victorias del CPU.'''

'''
Escribe un programa de nombre Diccionarios_ej1_piedra_papel_tijera.py que realice lo siguiente:
Este programa es una nueva versión del juego realizado de piedra, papel y tijeras, pero utilizando un diccionario para las reglas del juego.
El juego mostrará las victorias del jugador, los partidos empatados y las victorias del CPU. Se debe mostrar el siguiente menú:

  ***  Juego de piedra, papel o tijeras  ***
1) Piedra.
2) Papel.
3) Tijeras.
0) Salir.
Cualquier otro caso -> Opción no válida.
Para ello:
a) Muestre el menú en una función que pida al usuario una de las opciones: piedra, papel o tijeras.
b) Utilice un diccionario para las distintas combinaciones.
c) Realice la lógica adecuada para determinar al ganador. Se requiere que utilice al menos una función.
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
JUGADOR = "Gana el jugador."
EMPATE = "Empate."
CPU = "Gana la CPU."

# Función que muestra el menú de las opciones del jugador.
def Menu():
    print("  ***  Juego de piedra, papel o tijeras  ***")
    print(f"Victorias del jugador: {Victorias_jugador}, empates: {Empates} y victorias del CPU: {Victorias_CPU}  ")
    print("[0].-  Salir.")
    print("[1].-  Piedra.")
    print("[2].-  Papel.")
    print("[3].-  Tijera.")
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
    else:
        Jugador = None
    Lista.append(PIEDRA)
    Lista.append(PAPEL)
    Lista.append(TIJERA)
    # Elección de la CPU aleatoriamente entre las opciones.
    Opcion_CPU = choice(Lista)
    return Jugador,Opcion_CPU

# Diccionario que define las reglas del juego.
Piedra_papel_tijera = {(PIEDRA, TIJERA): JUGADOR,
                       (PIEDRA, PAPEL): CPU,
                       (TIJERA, PAPEL): JUGADOR,
                       (TIJERA, PIEDRA): CPU,
                       (PAPEL, PIEDRA): JUGADOR,
                       (PAPEL, TIJERA): CPU,
                       }

while Opcion != 0: # El juego continúa mientras el jugador no elija salir.
    Opcion = Menu()
    Opcion_Jugador, Opcion_CPU = Eleccion_jugador(Opcion)   # Obtiene la elección del jugador y del CPU.

    # Se obtiene el resultado del juego usando el diccionario.
    Resultado = Piedra_papel_tijera.get((Opcion_Jugador, Opcion_CPU), EMPATE)

    if Opcion == 0: # Salir del programa.
        print()
        print("Fin del programa.")
    elif Opcion >= 4: # Opcion incorrecta.
        print()
        print("Opción incorrecta.")
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
    print()