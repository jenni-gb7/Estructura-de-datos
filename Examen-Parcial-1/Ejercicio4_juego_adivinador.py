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

# Módulo random.
import random

# Inicializar contadores
num_intento = 0

# Generar la opción de la CPU aleatoriamente (1 al 100)
num_secreto = random.randint(1, 100)

# Se declara la condición para el ciclo while.
# Mientras el número de intentos sean <= 4, es decir tiene 5 intentos.
while num_intento <= 4:

    # Se acomulan en la variable el número de intentos.
    num_intento += 1

    print(" ")
    print(f"Número de intento: {num_intento}.", end=" ")
    num_1 = int(input(f"Ingresa un número (1-100): "))

    # Revisar que el número ingresado este en el rango de 1 a 100.
    if num_1 <= 1 or num_1 >= 100:
        print("Número fuera de rango. Ingresa un número entre 1-100")
        # Salta al siguiente intento sin contar el actual.
        num_intento = 0

    # Comparar el número ingresado con el número secreto.
    # Condición: Si la varible número es menor igual al número de intentos.
    elif num_1 <= num_secreto:
        # Se imprime el mensaje con una pista.
        print("El número a adivinar es mayor ")
    # Condición: Si la varible número es mayor igual al número secreto.
    elif num_1 >= num_secreto:
        # Se imprime el mensaje con una pista.
        print("El número a adivinar es menor ")
        # Si la varible número es igual al número secreto.
    else:
        print(f"¡Felicitaciones!. Adivinaste el número {num_secreto} en {num_intento} intentos.")

# Si no se cumple en 5 intentos, se termina y se imprime el siguiente mensaje.
print(" ")
print(f"Perdiste. El número secreto era: {num_secreto}.")







