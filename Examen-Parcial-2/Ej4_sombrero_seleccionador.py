'''
Jennifer Marlene Gutierrez Beteta
02 de diciembre de 2024.
Descripción:
Este programa es un test de la elección del sombrero seleccionador de Harry Potter para alguna de las casas: Gryffindor, Slytherin, Hufflepuff y Ravenclaw.'''

'''
Escribe un programa de nombre Ej4_sombrero_seleccionador.py que realice lo que se indica en la descripción del programa.
Este programa es un test de la elección del sombrero seleccionador de Harry Potter para alguna de las casas: Gryffindor, Slytherin, Hufflepuff y Ravenclaw.

Ejemplos de preguntas:

¿Cuál de las siguientes opciones odiarías más que la gente te llamara?
Gryffindor - Ordinario.
Slytherin - Ignorante.
Hufflepuff - Cobarde.
Ravenclaw - Egoísta.

Después de tu muerte ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre?
Gryffindor - Te extraña, pero sonríe.
Slytherin - Pide más historias sobre tus aventuras.
Hufflepuff - Piensa con admiración tus logros.
Ravenclaw - No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta.


Dada la opción, preferirías inventar una poción que garantizara:
Gryffindor - Gloria.
Slytherin - Sabiduría.
Hufflepuff - Amor.
Ravenclaw - Poder.


¿Cómo te definirías en una sola palabra?
Gryffindor - Valiente.
Slytherin - Ambicioso.
Hufflepuff - Leal.
Ravenclaw - Curioso.


¿Qué cualidad te describe mejor?
Gryffindor - La fuerza.
Slytherin - La astucia.
Hufflepuff - La paciencia.
Ravenclaw - La inteligencia.


¿Cuál es tu clase favorita?
Gryffindor - Vuelo.
Slytherin - Defensa contra las artes oscuras.
Hufflepuff - Animales fantásticos.
Ravenclaw - Pociones.


¿Cuál es tu lenguaje de programación favorito?
Gryffindor - C.
Slytherin - Python.
Hufflepuff - C++.
Ravenclaw - JavaScript.

Se debe mostrar la siguiente pantalla inicial:

  ***  Ejercicio 4. Test del sombrero seleccionador de Harry Potter.  ***

Este programa determina la casa (Gryffindor, Slytherin, Hufflepuff y Ravenclaw) a la que perteneces, de acuerdo a tus respuestas.

1) Iniciar test.

0) Salir.

Cualquier otro caso -> Opción no válida.

Para ello:

a) Realice al menos 5 preguntas al usuario. Puede utilizar las 7 aquí presentadas.

b) El orden de las respuestas presentadas no debe ser el mismo al repetir el test. Se recomienda combinar conjuntos, listas y diccionarios para este fin.

c) Utilice la lógica adecuada para determinar la casa con base en las respuestas.

d) Muestre la casa al final del test y finalice el programa.
'''
import random

# Diccionario de preguntas y opciones.
preguntas = [
    ("¿Cuál de las siguientes opciones odiarías más que la gente te llamara?",
     ["Ordinario", "Ignorante", "Cobarde", "Egoísta"]),
    ("Después de tu muerte, ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre?",
     ["Te extraña, pero sonríe.", "Pide más historias sobre tus aventuras.", "Piensa con admiración tus logros.",
      "No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta."]),
    ("Dada la opción, preferirías inventar una poción que garantizara:", ["Gloria.", "Sabiduría.", "Amor.", "Poder."]),
    ("¿Cómo te definirías en una sola palabra?", ["Valiente.", "Ambicioso.", "Leal.", "Curioso."]),
    ("¿Qué cualidad te describe mejor?", ["La fuerza.", "La astucia.", "La paciencia.", "La inteligencia."])
]

# Diccionario de respuestas asociadas con cada casa.
casas = {
    "Gryffindor": ["Valiente.", "Te extraña, pero sonríe.", "Gloria.", "La fuerza."],
    "Slytherin": ["Ambicioso.", "Pide más historias sobre tus aventuras.", "Sabiduría.", "La astucia."],
    "Hufflepuff": ["Leal.", "Piensa con admiración tus logros.", "Amor.", "La paciencia."],
    "Ravenclaw": ["Curioso.",
                  "No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta.",
                  "Poder.", "La inteligencia."]
}


# Función para determinar la casa basada en las respuestas.
def determinar_casa(respuestas):
    puntajes = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    # Sumamos los puntos para cada casa según las respuestas.
    for respuesta in respuestas:
        for casa, opciones in casas.items():
            if respuesta in opciones:
                puntajes[casa] += 1
    # Determinamos la casa con más puntos.
    casa_final = max(puntajes, key=puntajes.get) # Key función para determinar cómo se evalúan los elementos y para cada clave llamará al valor máximo.
    return casa_final


# Función para hacer las preguntas.
def hacer_preguntas():
    respuestas = [] # Se declar la lista.
    random.shuffle(preguntas)  # Mezclamos las preguntas.

    # Hacemos las 5 preguntas
    for pregunta, opciones in preguntas:
        print("" + pregunta)
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}) {opcion}")

        # Pedimos la respuesta del usuario.
        while True:
            try:   # Si el número no es válido, vuelve a seleccionar su respuesta.
                respuesta = int(input("Seleccione su respuesta (1-4): "))
                if 1 <= respuesta <= 4:
                    respuestas.append(opciones[respuesta - 1])
                    break
                else:
                    print("Por favor, elige una opción entre 1 y 4.")
            except ValueError: # Por si escoge un número inválido.
                print("Entrada no válida. Debes elegir un número entre 1 y 4.")

    # Determinamos la casa final.
    casa = determinar_casa(respuestas)
    print(f"¡El sombrero seleccionador te ha asignado a la casa: {casa}")


# Función del menú.
def Menu():
    print()
    print("*** Test del Sombrero Seleccionador de Harry Potter ***")
    print("[0].-Salir")
    print("[1].- Iniciar test")
    print()
    # Se le solicita al usuario una opción.
    opcion = int(input("Ingresa una de las opciones: "))
    return opcion

opcion = None
while opcion != 0:
    opcion = Menu()
    if opcion == 0:
        print()
        print("Fin del programa.") # Salir del programa.
    elif opcion == 1: # Iniciar con el test.
        hacer_preguntas()
        break
    else:
        print()
        print("Opción no válida.")
print("-----------------------------------------------------------------------")


