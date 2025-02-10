'''
Jennifer Marlene Gutierrez Beteta
22 de enero de 2025.
Descripción:
Examen Parcial 3: Juego 4 en raya.
'''

import  Juego_ahorcado
import  Juego_de_gato
import Juego_4_en_raya
import Ej4_batalla_naval
import Carrera_de_caballos_modulo

def mostrar_menu() -> None:
    '''
    Muestra un menú con diferentes opciones de juegos.
    El usuario debe ingresar una opción válida y el juego correspondiente se ejecutará.
    Una vez terminado el juego, se regresa al menú principal.
    '''
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
                Juego_ahorcado.Jugar_ahorcado()
            elif eleccion == 2:
                Juego_de_gato.juego_del_gato()
            elif eleccion == 3:
                Juego_4_en_raya.Juego_4raya()
            elif eleccion == 4:
                Ej4_batalla_naval.main()
            elif eleccion == 5:
                Carrera_de_caballos_modulo.main()
            elif eleccion == 0:
                print("¡Hasta luego!")
                break
            else:
                print("Selección no válida, por favor elige una opción entre 0 y 5")
        else:
            print("Por favor, ingresa un número válido")

if __name__ == "__main__":
    mostrar_menu()
