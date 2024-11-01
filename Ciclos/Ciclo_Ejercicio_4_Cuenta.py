'''
Jennifer Marlene Gutierrez Beteta
28 de octubre de 2024
Descripción:
Ciclo ejercicio 4 cuenta.
Este programa realizará diferentes acciones en una cuenta de banco.
'''
saldo = 0
opcion = 1
while opcion != 0:
    print(" ")
    print("*** Banco Azteca  ***")
    print(" ")
    print("[0].- Salir")
    print("[1].- Consulta saldo")
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

print(f"Saliendo del programa...")
