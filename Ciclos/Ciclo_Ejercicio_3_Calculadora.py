'''
Jennifer Marlene Gutierrez Beteta
28 de octubre de 2024
Descripción:
Ciclo ejercicio 3 Calculadora .
Este programa que realizará las operaciones basicas.
'''
opcion=1

while opcion != 0:
    print(" ")
    print("*** Ménu  ***")
    print(" ")
    print("[0].- Salir")
    print("[1].- Suma")
    print("[2].- Resta")
    print("[3].- Multiplicación")
    print("[4].- División")
    print("[5].- División entera")
    print("[6].- Exponenciación")
    print(" ")

    opcion = int(input("Ingresa una opción: "))
    if opcion == 1:
        numero_1 = int(input("Ingresa el primer número: "))
        numero_2 = int(input("Ingresa el segundo número: "))
        suma = numero_1 + numero_2
        print(f"La suma {numero_1} + {numero_2} de  es:",suma)

    elif opcion == 2:
        numero_1 = int(input("Ingresa el primer número: "))
        numero_2 = int(input("Ingresa el segundo número: "))
        resta = numero_1 - numero_2
        print(f"La resta de {numero_1} - {numero_2} es:", resta)
    elif opcion == 3:
        numero_1 = int(input("Ingresa el primer número: "))
        numero_2 = int(input("Ingresa el segundo número: "))
        multiplicacion = numero_1 * numero_2
        print(f"La multiplicación de {numero_1} * {numero_2} es:", multiplicacion)
    elif opcion == 4:
        numero_1 = int(input("Ingresa el primer número: "))
        numero_2 = int(input("Ingresa el segundo número: "))
        division = numero_1 / numero_2
        print(f"La división de {numero_1} / {numero_2} es:{division: .2f}")
    elif opcion == 5:
        numero_1 = int(input("Ingresa el primer número: "))
        numero_2 = int(input("Ingresa el segundo número: "))
        división_entera =numero_1 / numero_2
        print(f"La división entera de {numero_1} / {numero_2} es:", división_entera)
    elif opcion == 6:
        numero_1 = int(input("Ingresa el primer número: "))
        numero_2 = int(input("Ingresa el segundo número: "))
        exponienciacion = numero_1 ** numero_2
        print(f"La exponienciación de {numero_1} ** {numero_2} es:",  exponienciacion)
    else:
        print(f"La opción no es válida")


print(f"Saliendo del programa...")