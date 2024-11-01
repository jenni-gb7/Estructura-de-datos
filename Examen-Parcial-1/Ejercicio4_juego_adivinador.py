'''
Jennifer Marlene Gutierrez Beteta
31 de octubre de 2024
Descripción:
Ejercicio 4, Examen Parcial 1.
Este programa es un juego en donde el usuario intente adivinar un número secreto.


Para ello:

a) El número a adivinar es un número aleatorio entre 1 y 100.

b) El jugador tendrá 5 intentos para encontrar el número.

c) Como pista, el juego indicará si el número a adivinar es menor o mayor al número ingresado, si el número no es el correcto.

d) Si el jugador adivina el número, el juego muestra un mensaje de felicitación y el número de intentos.

e) Si el jugador no adivina el número, el juego muestra un mensaje con el número.
'''

print(" ")
print("*** Juego del adivinador ***")
print(" ")

import random

# Inicializar contadores
num_intento = 0

# Generar la opción de la CPU aleatoriamente (1, 2 o 3)
num_secreto = random.randint(1, 100)

while num_intento <= 4:

    num_intento += 1

    print(" ")
    print(f"Número de intento: {num_intento}.", end=" ")
    num_1 = int(input(f"Ingresa un número (1-100): "))
    if num_1 <= num_secreto:
        print("El número a adivinar es mayor ")
    elif num_1 >= num_secreto:
        print("El número a adivinar es menor ")
    else:
        print(f"¡Felicitaciones!. Adivinaste el número {num_secreto} en {num_intento} intentos.")

print(" ")
print(f"Perdiste. El número secreto era: {num_secreto}.")







