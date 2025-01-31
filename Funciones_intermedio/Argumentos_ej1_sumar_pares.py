'''
Jennifer Marlene Gutierrez Beteta
21 de enero de 2025.
Descripción:
Ejercicio 1. Sumar números pares con argumentos variables.

Este programa realiza la suma de todos los números pares ingresados por el usuario.

Para ello:

    a) Solicite al usuario los números enteros. Nota: Hay que validar que tengan el formato adecuado.

    b) Utilice una función con argumentos variables que devuelva la suma de los números pares.

    c) Muestre el resultado en consola.'''

def suma_pares(*numeros)-> None:
    """
    Calcula y muestra la suma de los números pares dados.
    """
    suma_total = sum(num for num in numeros if num % 2 == 0)
    print(f"La suma de los números pares es: {suma_total}")


def pedir_numeros()-> None:
    """
    Solicita números enteros al usuario hasta que presione enter.
    Retorna una lista de números.
    """
    numeros = []
    contador = 1

    while True:
        # Se solicitan números.
        entrada = input(f"Ingresa un número entero [{contador}](o presiona enter para terminar): ")
        # El bucle se detiene si el usuario presiona Enter sin escribir nada
        if entrada == "":
            break
        # Para verificar si es un número válido.
        if entrada.isdigit() or entrada.startswith('-'):   # Verifica si entrada está compuesta solo por dígitos positivos, sin signos ni espacios.
            numero = int(entrada)
        # Si el número es par lo agrega a la lista.
            if numero % 2 == 0:
                numeros.append(numero)
            contador += 1
        else:
            print("Formato no válido, intenta de nuevo.")

    return numeros


def main()-> None:
    """
    Función principal.
    """
    print("*** Programa para Sumar Números Pares ***")
    # Llama a las funciones anteriores
    numeros = pedir_numeros()
    suma_pares(*numeros)


if __name__ == '__main__':
    main()
