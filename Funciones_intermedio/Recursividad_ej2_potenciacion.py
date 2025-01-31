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
    '''
    Calcula la potencia de un número de forma recursiva.
    '''
    # Caso base: cualquier número elevado a la 0 es 1
    if exponente == 0:
        return 1
    # Caso especial: 0 elevado a cualquier número mayor que 0 es 0.
    elif exponente == 0:
        return 0
    # Caso recursivo
    return base * calcular_potencia(base, exponente - 1)

def num_valido(cadena: str,cadena_2: str) -> bool:
    '''
    Función que determina si las cadenas ingresadas representan números enteros positivos válidos.'''

    # Se verifica si la cadena contiene solo caracteres numéricos.
    if cadena.isnumeric() and cadena_2.isnumeric():
        # Se maneja el caso especial 0^0 que es una indeterminación.
        if cadena == "0" and cadena_2 == "0":
            print("0 ^ 0 = Indeterminado.")
            return False
        else:
            return True
    else:
        print("Formato no válido.")
        return False

def main() -> None:
    '''
    Función principal.
    '''

    print("********  Programa que imprime la potenciación de un número de manera recursiva.  ********")
    # Se solicita al usuario la base y el exponente.
    base = input("Ingresa la base: ")
    exponente = input("Ingresa el exponente: ")
    print()

    # Se revisa que el número sea válido.
    if num_valido(base,exponente):
        base = int(base)
        exponente = int(exponente)
        # Se muestra el resultado de la potenciación calculada recursivamente.
        print(f"{base} ^ {exponente} = ",end=" ")
        print(calcular_potencia(base,exponente))
    print()
    print("Fin del programa.")

if __name__ == '__main__':
    main()

