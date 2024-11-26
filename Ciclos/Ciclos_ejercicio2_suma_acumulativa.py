'''
Jennifer Marlene Gutierrez Beteta
06 de noviembre de 2024.
Descripción:
Este programa calcula la suma acumulativa entre dos números ingresados por el usuario.
'''

'''
Escribe un programa de nombre Ciclos_ej2_suma_acumulativa_v2.py que realice lo siguiente:

Este programa calculará la suma acumulativa de dos números ingresados por el usuario.

A diferencia del programa anterior, ahora el usuario también definirá el número inicial. Para ello:
a) Solicite al usuario los números inicial y final de la suma acumulativa.
b) Calcule la suma acumulativa entre ambos números.
c) Muestre el resultado de la suma.
'''
print()
print("*** Programa que calcula la suma acumulativa entre dos números. ***")
print()
# Solicitar el número inicial y final.
Numero_Inicial = int(input("Ingrese el número inicial de la cuenta: "))
Numero_Final = int(input("Ingrese el número final de la cuenta: "))


# Inicializar el contador.
# Se iguala para que inicie en el número definido por el usuario.
Cont_1 = Numero_Inicial
# Se inicializa la variable para almacenar la suma acumulativa.
Suma_Total1 = 0

# Ciclo que calcula la suma acumulativa entre los números ingresados.
while Cont_1 <= Numero_Final:
    Suma_Total1 += Cont_1  #Sumar el contador al total.
    Cont_1 += 1      # Se incrementar el contador.

# Mostrar el resultado de la suma acumulativa
print()
print(f"La suma del {Numero_Inicial} al {Numero_Final} es: {Suma_Total1}.")


