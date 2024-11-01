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

opcion = 1
while opcion != 4:
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
    if opcion == 1:
        base_b = float(input("Ingresa la base: "))
        altura_h = float(input("Ingresa la altura: "))
        area_r = base_b * altura_h
        print(f"El área del rectángulo es: {area_r: .3f} cm")
    elif opcion == 2 :
        base_b = float(input("Ingresa la base: "))
        altura_h = float(input("Ingresa la altura: "))
        perimetro_r = 2 * (base_b + altura_h)
        print(f"El perímetro del rectángulo es: {perimetro_r: .3f} cm")
    elif opcion == 3:
        radio_c = float(input("Ingresa el radio: "))
        area_c = 3.1416 * (radio_c ** 2)
        print(f"El área del círculo es: {area_c: .3f} cm")
    elif opcion == 4:
        radio_c = float(input("Ingresa el radio: "))
        perimetro_c = 2 * 3.1416 * radio_c
        print(f"El área del círculo es: {perimetro_c: .3f} cm")
    elif opcion == 0:
        print(f"Saliendo del programa...")
    else:
        print("La opción no es válida")


