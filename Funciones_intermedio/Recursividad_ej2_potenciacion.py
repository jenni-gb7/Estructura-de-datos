'''
Jennifer Marlene Gutierrez Beteta
21 de enero de 2025.
Descripción:
Ejercicio 2. Potenciación con funciones recursivas.

Este programa calcula la potencia de un número a otro número de manera recursiva. Ambos son números

enteros positivos ingresados por el usuario.

Notar que: a^b = a*(a^(b-1)).

Para ello:

    a) Solicite al usuario ambos números, validando que tengan el formato adecuado.

    b) Utilice una función recursiva para calcular la potencia, indicando el caso base y el caso recursivo.

    c) Muestre el resultado en consola.'''


def calcular_potencia(base: int, exponente: int) -> int:
    """
    Calcula la potencia de un número de forma recursiva.
    :param base: Número base.
    :param exponente: Número exponente.
    :return: Resultado de base elevado a exponente.
    """
    # Caso base: cualquier número elevado a la 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo
    return base * calcular_potencia(base, exponente - 1)


def pedir_numero(mensaje: str) -> int:
    """
    Solicita un número entero positivo al usuario, validando su formato.
    :param mensaje: Mensaje para el usuario.
    :return: Número entero positivo.
    """
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():   # Verifica si entrada está compuesta solo por dígitos positivos, sin signos ni espacios.
            return int(entrada)
        else:
            print("Formato no válido. Salir del programa.")
            exit()


def main():
    """
    Función principal.
    """
    print("*** Programa para Calcular la Potencia de un Número ***")
    base = pedir_numero("Ingresa la base (número entero positivo): ")
    exponente = pedir_numero("Ingresa el exponente (número entero positivo): ")

    resultado = calcular_potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")
    print("Fin del programa.")


if __name__ == "__main__":
    main()
