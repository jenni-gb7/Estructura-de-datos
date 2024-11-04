'''
Jennifer Marlene Gutierrez Beteta
31 de octubre de 2024
Descripción:
Ejercicio 2, Examen Parcial 1.

Este programa determina el área y el perímetro de un rectángulo o de un círculo.
Muestre el siguiente menú:

1) Calcular el área de un rectángulo.
2) Calcular el perímetro de un rectángulo.
3) Calcular el área de un círculo.
4) Calcular el perímetro de un círculo.
0) Salir.
Cualquier otro caso -> Mostrar un mensaje de "opción no válida".

Para ello:

a) Muestre el menú anterior en consola.

b) En caso de calcular un área o perímetro, solicite al usuario los valores requeridos (flotantes).

c) Utilice la lógica adecuada para calcular lo solicitado. Asuma pi = 3.1416.

d) Imprima el resultado en la consola. Nota: muestre únicamente 3 decimales en todos los casos.

e) Repita el menú hasta salir.
'''

# Se inicializa la variable.
opcion = 1

# Se declara la condición para el ciclo while, y asi poder entrar al menú.
# Mientras la variable opción sea diferente de cero (0).
while opcion != 0:
    print(" ")
    print("*** Programa que calcula el área y el perímetro ***")
    print(" ")
    print("[1].- Calcular el área de un rectángulo.")
    print("[2].- Calcular el perímetro de un rectángulo.")
    print("[3].- Calcular el área de un círculo.")
    print("[4].- Calcular el perímetro de un círculo.")
    print("[0].- Salir")
    print(" ")


    opcion = float(input("Ingresa una opción: "))

    # La secuencia if-elif-else es la forma de "si las condiciones anteriores no son verdaderas, entonces prueba esta condición", es decir los número entrará en la condición que se adapte mejor a ellos.
    # Condición: Si opcion == 1 calcular el área de un rectángulo.
    if opcion == 1:
        # Se solicita la base y la altura.
        base_b = float(input("Ingresa la base: "))
        altura_h = float(input("Ingresa la altura: "))
        # La fórmula para calcular el área de un rectángulo es área= base * altura.
        area_r = base_b * altura_h
        print(f"El área del rectángulo es: {area_r: .3f} cm")
    # Condición: Si opcion == 2 calcular el perímetro  de un rectángulo.
    elif opcion == 2 :
        # Se solicita la base y la altura.
        base_b = float(input("Ingresa la base: "))
        altura_h = float(input("Ingresa la altura: "))
        # La fórmula para calcular el perímetro de un rectángulo es perímetro= 2 * (base + altura).
        perimetro_r = 2 * (base_b + altura_h)
        print(f"El perímetro del rectángulo es: {perimetro_r: .3f} cm")
    # Condición: Si opcion == 3 calcular el área de un  círculo.
    elif opcion == 3:
        # Se solicita el radio.
        radio_c = float(input("Ingresa el radio: "))
        # La fórmula para calcular el área del círculo es area= 3.1416 * (radio ** 2).
        area_c = 3.1416 * (radio_c ** 2)
        print(f"El área del círculo es: {area_c: .3f} cm")
    # Condición: Si opcion == 4 calcular el perímetro de un  círculo.
    elif opcion == 4:
        # Se solicita el radio.
        radio_c = float(input("Ingresa el radio: "))
        # La fórmula para calcular el perímetro del círculo es perímetro= 2 * 3.1416 * radio.
        perimetro_c = 2 * 3.1416 * radio_c
        print(f"El perímetro del círculo es: {perimetro_c: .3f} cm")
        # Si no cumple ninguna de estas condiciones y opcion == 0.
    elif opcion == 0:
        # El programa termina.
        print(f"Saliendo del programa...")
    else:
        # Si opcion ¡= 4, tiene que intentarlo de nuevo.
        print("La opción no es válida")


