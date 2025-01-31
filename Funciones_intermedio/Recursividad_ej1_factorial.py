'''
Jennifer Marlene Gutierrez Beteta
21 de enero de 2025.
Descripción:
Ejercicio 1. Factorial mediante funciones recursivas.
Este programa calcula el factorial de un número entero positivo ingresado por el usuario, utilizando recursividad.

Notar que: n! = n*(n-1)!

Para ello:

    a) Solicite al usuario el número al que se requiere calcular el factorial, validando que tenga el formato adecuado.

    b) Utilice una función recursiva para calcular el factorial, indicando el caso base y el caso recursivo.

    c) Muestre el resultado en consola.
'''

def calcular_factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero positivo de forma recursiva.
    :param n: Número entero positivo.
    :return: Factorial de n.
    """
    # Caso base: el factorial de 0 o 1 es 1
    if n in (0, 1):
        return 1
    # Caso recursivo
    return n * calcular_factorial(n - 1)


def pedir_numero() -> int:
    """
    Solicita un número entero positivo al usuario y valida su formato.
    :return: Número entero positivo.
    """
    entrada = input("Ingresa un número entre 0 y entero positivo: ")
    if entrada.isdigit():   # # Verifica si entrada está compuesta solo por dígitos positivos, sin signos ni espacios.
        return int(entrada)
    else:
        print("Formato no válido. Salir del programa.")
        exit()


def main():
    """
    Función principal.
    """
    print("*** Programa para Calcular el Factorial de un Número ***")
    numero = pedir_numero()
    resultado = calcular_factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
    print("Fin del programa.")


if __name__ == "__main__":
    main()
