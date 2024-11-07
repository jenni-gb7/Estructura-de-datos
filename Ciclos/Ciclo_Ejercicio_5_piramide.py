'''
Jennifer Marlene Gutierrez Beteta
06 de noviembre de 2024.
Descripción:
Ciclo for.
'''
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

for j in range(1,n_fila+1):
    contador = "*" * n_fila
    n_fila = n_fila - 1
    print(f" {contador}")
print()
'''
#Ejercicio 3
n_fila = int(input("Ingrese un número de fila: "))

contador= n_fila

for k in range(1,n_fila+1):
    espacio = " " * k
    contador = "*" * contador
    print(f"{espacio} {contador}")
    contador -= 1
print()