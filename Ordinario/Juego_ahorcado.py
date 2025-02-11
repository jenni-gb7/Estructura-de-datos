'''
Jennifer Marlene Gutierrez Beteta
22 de enero de 2025.
Descripción:
Examen Parcial 3: Juego del ahorcado.
'''

# Colores
ROJO = "\033[91m"
RESET = "\033[0m"

import random

def Mostrar_monito(intentos: int)-> None:
    """
    Dibuja el monito del ahorcado según el número de intentos restantes.
    :param intentos: Número de intentos restantes.
    """
    monito = [
        """
           ------
           |    |
           |    
           |   
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """
    ]
    print(monito[6 - intentos])

def Jugar_ahorcado()-> int:
    """
    Ejecuta la lógica del juego del ahorcado.
    El jugador debe adivinar letras de una palabra secreta seleccionada aleatoriamente.
    Se muestra el monigote del ahorcado según los intentos restantes.
    """


    palabras = ["python","computadora","ahorcado","juego","palabras"]
    palabra = random.choice(palabras)   # Función que selecciona un elemento de la lista al azar.
    intentos = 6
    adivinadas = []

    AHORCADO = """
           AAAAA  H   H  OOOOO  RRRRR   CCCCC  AAAAA  DDDDD   OOOOO
           A   A  H   H  O   O  R    R C       A   A  D    D  O   O
           AAAAA  HHHHH  O   O  RRRRR  C       AAAAA  D    D  O   O
           A   A  H   H  O   O  R  R   C       A   A  D    D  O   O
           A   A  H   H  OOOOO  R   RR  CCCCC  A   A  DDDDD   OOOOO
           """
    # Imprimir el texto con colores
    print(ROJO + AHORCADO + RESET)

    print("¡Bienvenido al juego del Ahorcado!")
    while intentos > 0:
        Mostrar_monito(intentos)
        print(f"Intentos restantes: {intentos}")
        # Mostrar la palabra oculta.
        palabra_oculta = [letra if letra in adivinadas else "_" for letra in palabra]
        print()
        print("Palabra:", " ".join(palabra_oculta))   # Función que combina una lista en una cadena con espacios.

        # Verificar si se ha ganado.
        if "_" not in palabra_oculta:   # Comprueba si el subrayado no está  en la cadena.
            print("¡Felicidades! Adivinaste la palabra:", palabra)
            break
        # Pedir una letra al usuario.
        letra = input("Adivina una letra: ").lower()    # Convierte todos los caracteres de una cadena a minúsculas.
        if len(letra) != 1 or not letra.isalpha():  # Comprueba si una cadena está formada solo por letras.
            print("Por favor,ingrese una letra.")
            intentos += 1
        if letra in adivinadas:
            print("Ya usaste esa letra,intenta de nuevo.")
        elif letra in palabra:
            print("¡Correcto!")
            adivinadas.append(letra)    # Permite agregar elementos a una lista.
        else:
            print("Incorrecto.")
            intentos -= 1
    # Si pierde.
    if intentos == 0:
        print()
        print("Perdiste. La palabra era:", palabra)
        Mostrar_monito(0)


if __name__ == "__main__":
    Jugar_ahorcado()

