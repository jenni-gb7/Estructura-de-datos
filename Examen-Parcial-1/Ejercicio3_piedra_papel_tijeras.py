'''
Jennifer Marlene Gutierrez Beteta
31 de octubre de 2024
Descripción:
Ejercicio 3, Examen Parcial 1.

Este programa es el famoso juego de "piedra, papel o tijera", en donde el contrincante es la CPU. La opción de la CPU se escogerá de forma aleatorio con la función randint().

El juego mostrará las victorias del jugador, los partidos empatados y las victorias del CPU. Además, mostrará el siguiente menú:

1) Piedra.
2) Papel.
3) Tijera.
0) Salir.
Cualquier otro caso -> Mostrar un mensaje de "opción no válida".

Para ello:

a) Muestre la cantidad de victorias, empates y derrotas.

b) Pida al usuario una opción del menú.

c) Realice la lógica adecuada para calcular al ganador.

d) Muestre en la consola la elección del jugador, del CPU y el resultado.

e) Repita nuevamente el menú hasta salir.
'''

# Módulo random.
import random

# Inicializar contadores
opcion_jugador = 1
victorias_del_jugador = 0
empates_e = 0
victorias_del_cpu = 0


# Se declara la condición para el ciclo while, y asi poder entrar al menú.
# Mientras la variable opción sea diferente de cero (0).
while opcion_jugador != 0:
    # Generar la opción de la CPU aleatoriamente (1 al 3)
    opcion_cpu = random.randint(1, 3)

    # Se declaran los marcadores del juego.
    print(" ")
    print("*** Juego de piedra, papel o tijera ***")
    print(" ")
    print(f"Victorias del jugador: {victorias_del_jugador},",end=" ")
    print(f"Empates: {empates_e} y",end=" ")
    print(f"Victorias del CPU: {victorias_del_cpu}.",end=" ")
    # Se declara el menú.
    print("")
    print("[1].- Piedra.")
    print("[2].- Papel.")
    print("[3].- Tijera.")
    print("[0].- Salir")
    print(" ")

    opcion_jugador = int(input("Ingresa una opción: "))

    # La secuencia if-elif-else es la forma de "si las condiciones anteriores no son verdaderas, entonces prueba esta condición", es decir los número entrará en la condición que se adapte mejor a ellos.

    # Condición: Si la opcion del jugador == opcion del cpu.
    if opcion_jugador == opcion_cpu:
            opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}
            print(f"Jugador: {opciones[opcion_jugador]}.", end=" ")
            print(f"CPU: {opciones[opcion_cpu]}.", end=" ")
            # Entonces es un empate y se acomula en la variable.
            print("Empate.")
            empates_e += 1
    # Condición: Si se cumplen que piedra y tijera o papel y piedra o tijera y papel, el que sea superior gana ya sea el jugador o la CPU..
    elif (opcion_jugador == 1 and opcion_cpu == 3) or (opcion_jugador == 2 and opcion_cpu == 1) or (opcion_jugador == 3 and opcion_cpu == 2):
        opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}
        print(f"Jugador: {opciones[opcion_jugador]}.", end=" ")
        print(f"CPU: {opciones[opcion_cpu]}.", end=" ")
        print("El ganador es el jugador.")
        # Entonces es victoria del jugador y se acomula en la variable.
        victorias_del_jugador += 1
    # Condición: Si se cumplen que piedra y tijera o papel y piedra o tijera y papel, el que sea superior gana, ya sea el jugador o la CPU.
    elif (opcion_cpu == 1 and opcion_jugador == 3) or (opcion_cpu == 2 and opcion_jugador == 1) or (opcion_cpu == 3 and opcion_jugador == 2):
        opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}
        print(f"Jugador: {opciones[opcion_jugador]}.", end=" ")
        print(f"CPU: {opciones[opcion_cpu]}.", end=" ")
        print("El ganador es el CPU.")
        # Entonces es  victoria del cpu y se acomula en la variable.
        victorias_del_cpu += 1
        # Si la opcion es == cero, el juego termina.
    elif opcion_jugador == 0:
        print(f"Fin del juego...")
    # Si opcion <4, tiene que intentarlo de nuevo.
    else:
        print("La opción no es válida")

