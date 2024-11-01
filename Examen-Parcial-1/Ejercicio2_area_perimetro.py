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
while opcion != 0:
    print(" ")
    print("*** Programa que calcula el área y el perímetro ***")
    print(" ")
    print("[0].- Salir")
    print("[1].- Calcular el área de un rectángulo.")
    print("[2].- Ingresa saldo")
    print("[3].- Retirar saldo")
    print(" ")

    opcion = int(input("Ingresa una opción: "))
    if opcion == 1:
        print(f"Su saldo es de: $ {saldo :.2f}")
    elif opcion == 2 :
        saldo_1= float(input("Ingrese su saldo: $"))
        saldo = saldo + saldo_1
    elif opcion == 3:
        saldo_retirar= float(input(f"Saldo a retirar: $"))
        saldo_retirado= saldo - saldo_retirar
        print(f"Saldo retirado: $ {saldo_retirado:.2f}")
    else:
        print(f"La opción no es válida")