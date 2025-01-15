'''
Jennifer Marlene Gutierrez Beteta
13 de enero de 2025.
Descripción:
Ejercicio 2, Parcial 3.
'''
from tkinter.font import names


def Menu() :
    '''
    Esta función muestra el menú del programa.
    :return: Devuelve la opción seleccionada.
    '''
    print("[1].- Suma")
    print("[2].- Resta")
    print("[0].-Salir")

    opcion = int(input("Ingresa una de las opciones: "))
    return opcion

def Suma(cadena: str) -> float | None:
    no_puntos = cadena.count(".")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_puntos in(0,1) :
        return  float(cadena)
    else:
        return None

def Resta(cadena: str) -> float | None:
    no_puntos = cadena.count(".")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None

opcion = Menu()

def main() -> None:
    while opcion != 0:
        if opcion == 1:
            Num1_Suma = input("Ingresa el primer número a sumar: ")
            Num1_Suma = Suma(Num1_Suma)
            Num2_Suma = input("Ingresa el segundo número a sumar:")
            Num2_Suma = Suma(Num2_Suma)
            Resultado_Suma = Num1_Suma + Num2_Suma
            print(f"el resultado de la suma de {Num1_Suma} y {Num2_Suma} es {Resultado_Suma}")
        elif opcion == 2:
            Num1_Resta = input("Ingresa el primer número a sumar: ")
            Num1_Resta = Resta(Num1_Resta)
            Num2_Resta = input("Ingresa el segundo número a sumar:")
            Num2_Resta = Resta(Num2_Resta)
            Resultado_Resta = Num1_Resta - Num2_Resta
            print(f"el resultado de la resta de {Num1_Resta} y {Num2_Resta} es {Resultado_Resta}")
        else:
            print("Opción no valida")
    print("Salio del programa")


if __name__ == '__main__':  # indica si el código es el que se ejecuta.
    main()
