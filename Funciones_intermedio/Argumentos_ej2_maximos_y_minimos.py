'''
Jennifer Marlene Gutierrez Beteta
21 de enero de 2025.
Descripción:
Ejercicio 2. Encontrar máximos y mínimos con argumentos variables.

Este programa encuentra el valor máximo y mínimo de todos los números ingresados por el usuario.

Para ello:

    a) Solicite los números con decimales, validando que tengan el formato adecuado.

    b) Utilice una función con argumentos variables que devuelva el valor máximo y mínimo.


    c) Muestre el resultado en consola.'''


def encontrar_max_min(*vargs)-> None:
    """
    Encuentra y muestra el valor máximo y mínimo de una lista de números.
    """
    # Se inicializan las variables en primer valor de la tupla.
    maximo = vargs[0]
    minimo = vargs[0]

    # Determinar el mínimo y máximo.
    for i in vargs:
        if i > maximo:
            maximo = i  # Se actualiza el valor máximo si se encuentra un número mayor.
        else:
            if i < minimo:  # Se actualiza el valor mínimo si se encuentra un número menor.
                minimo = i

    # Se muestra el mínimo y máximo.
    print(f"El número mínimo es: {minimo}")
    print(f"El número máximo es: {maximo}")

def pedir_numeros()-> None:
    """
    Solicita números con decimales al usuario, validando su formato.
    """
    numeros = []
    contador = 1
    while True:
        entrada = input(f"Ingresa un número con decimales [{contador}](o presiona enter para terminar): ")
        if entrada == "":
            break
        if entrada.startswith('-'): # Verifica si comienza con un signo.
            numero = float(entrada)
            numeros.append(numero)
            contador += 1
        else:
            print("Formato inválido. Ingresa un número válido.")

    return numeros


def main()-> None:
    """
    Función principal.
    """
    print("*** Programa para Encontrar el Valor Máximo y Mínimo ***")

    numeros = pedir_numeros()
    encontrar_max_min(*numeros)


if __name__ == "__main__":
    main()
