def menu() -> int:
    """
    Muestra el menú del programa
    :return: La selección del usuario
    """
    seguir = True
    while seguir:
        print("1. Sumar")
        print("2. Restar")
        print("0. Salir")
        seleccion = input("Elige una opción: ")
        if seleccion.isnumeric():  # verificar si la entrada es un número
            seleccion = int(seleccion)
            if seleccion == 0 or seleccion == 1 or seleccion == 2:
                seguir = False  # salir
                return seleccion
        print("Por favor, ingresa una opción válida")
#
def sumar(uno, dos) -> int:
    total = uno + dos
    print(total)
    print()
    return total

def resta(tres, cuatro) -> int:
    resultado = tres - cuatro
    print(resultado)
    print()
    return resultado


def ingresar_numero() -> float:
    """
    Solicita al usuario un número y verifica que sea válido
    Acepta tanto enteros como flotantes
    :return: El número válido ingresado
    """
    continuar = True
    while continuar:
        numero = input("Ingresa un número: ")
        no_puntos = numero.count(".")
        no_guiones = numero.count("-")
        # Elimino el signo negativo y los puntos para verificar que lo que quede son solo números
        revisar_cadena = numero.lstrip("-").replace(".", "")


        if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
            continuar = False  # salir del bucle
            return float(numero)  # devuelve flotante
        else:
            print("Entrada no válida. Por favor ingrese un número válido (entero o decimal)")


def main() -> None:
    opcion = None  #  Apliqué lo de la variable None
    while opcion != 0:
        opcion = menu()

        if opcion == 1:
            num1 = ingresar_numero()  # Se piden los números después de seleccionar la opción
            num2 = ingresar_numero()
            sumar(num1, num2)
        elif opcion == 2:
            num1 = ingresar_numero()  # Se piden los números después de seleccionar la opción
            num2 = ingresar_numero()
            resta(num1, num2)


if __name__ == '__main__':
    main()
    #print(__main__)
