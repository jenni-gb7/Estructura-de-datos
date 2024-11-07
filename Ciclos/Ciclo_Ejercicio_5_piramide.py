'''
Jennifer Marlene Gutierrez Beteta
06 de noviembre de 2024.
Descripción:
Ciclo for.
'''

#Ejercicio 1
n_fila = int(input("Ingrese un número de fila: "))
contador= "*"

for i in range(1,n_fila+1):
    contador = "*" * i
    print(f" {contador}")
print()

#Ejercicio 2
n_fila = int(input("Ingrese un número de fila: "))
contador= "*"

for i in range(1,n_fila+1):
    contador = "*" * n_fila
    print(f" {contador}")
print()