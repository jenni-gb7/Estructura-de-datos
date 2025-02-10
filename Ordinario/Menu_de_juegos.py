'''
Jennifer Marlene Gutierrez Beteta
22 de enero de 2025.
Descripción:
Examen Parcial 3: Juego 4 en raya.
'''

import Juego_Ahorcado
import Juego4enraya


def mostrar_menu() -> int:
    while True:
        print("*** Elige uno de los juegos ***")
        print("1. Ahorcado")
        print("2. Juego del Gato")
        print("3. 4 en Raya")
        print("4. Batalla naval")
        print("5. Carrera de caballos")
        print("0. Salir")

        eleccion = input("Ingresa tu selección: ")

        if eleccion.isnumeric():
            eleccion = int(eleccion)

            if eleccion == 1:
                Juego_Ahorcado.Jugar_ahorcado()
                break
            elif eleccion == 2:
                Juego_Gato.jugar_gato()
                break
            elif eleccion == 3:
                Juego4enraya.Juego_4raya()
                break
            elif eleccion == 4:
                Juego4enraya.Juego_4raya()
                break
            elif eleccion == 5:
                Juego4enraya.Juego_4raya()
                break
            elif eleccion == 0:
                print("¡Hasta luego!")
                break
            else:
                print("Seleccion no válida, por favor elige una opción entre 0 y 3")
        else:
            print("Por favor, ingresa un número válido")


if __name__ == "__main__":
    mostrar_menu()