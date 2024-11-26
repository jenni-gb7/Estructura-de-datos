'''
Jennifer Marlene Gutierrez Beteta
06 de noviembre de 2024.
Descripción:
Este programa calcula la suma acumulativa.
'''
'''
Escribe un programa de nombre Ciclos_ej1_suma_acumulativa.py que realice lo siguiente:

Este programa calculará la suma acumulativa del cero hasta un número ingresado por el usuario. Para ello:

a) Solicite al usuario un número mayor a cero que será el número hasta donde se realizará la suma.

b) Calcule la suma acumulativa.

c) Muestre el resultado de la suma.
'''

print()
print("*** Programa que calcula la suma acumulativa. ***")
print()
# Solicitar al usuario el número final.
Numero_Final = int(input("Ingrese el número final: "))

# Inicializar el contador.
Cont = 0
# Variable para acumular la suma.
Suma_Total = 0

# Ciclo que calcula la suma acumulativa desde 0 hasta el número ingresado.
while Cont <= Numero_Final :
    Suma_Total += Cont   #Sumar el contador al total.
    Cont += 1       # Se incrementar el contador.

print()
#Se muestra el resultado de la suma acumulativa.
print(f"La suma del 0 al {Numero_Final} son: {Suma_Total}.")

