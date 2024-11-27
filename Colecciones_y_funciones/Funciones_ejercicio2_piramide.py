'''
Jennifer Marlene Gutierrez Beteta
07 de noviembre de 2024.
Descripción:
#Este programa imprime una pirámide de caracteres '*' en cuatro formas diferentes según la cantidad de filas.
'''

'''Escribe un programa de nombre Ciclos_ej5_piramide.py que realice lo siguiente:
Este programa imprime una pirámide de caracteres '*' de cuatro formas:
1)
*
**
***

2)
***
**
*

3)
  *
 ***
*****

4)
  *
 **
***

En donde el usuario ingresa el número de filas. Para ello:
a) Solicite el número de filas de la pirámide.
b) Muestre los tres tipos de pirámides utilizando la lógica adecuada.
'''


def Piramide_1(Numero_filas):
    print()
    print("Pirámide 1:")
    for j in range(1, Numero_filas + 1):
        asterisco = "*" * j
        print(f"{asterisco}")
    print("________________________________________________________________")

def Piramide_2(Numero_filas):
    print()
    print("Pirámide 2:")
    contador = Numero_filas
    for i in range(1, Numero_filas + 1):
        asterisco = "*" * contador
        print(f"{asterisco}")
        contador -= 1
    print("________________________________________________________________")

def Piramide_3(Numero_filas):
    print()
    print("Pirámide 3:")
    contador = Numero_filas
    contador_2 = 0
    for m in range(1, Numero_filas + 1):
        espacio = " " * contador
        asterisco = "*" * (m + contador_2)
        print(f"{espacio}{asterisco}")
        contador -= 1
        contador_2 += 1
    print("________________________________________________________________")

def Piramide_4(Numero_filas):
    print()
    print("Pirámide 4:")
    contador = Numero_filas
    contador_2 = 0
    for m in range(1, Numero_filas + 1):
        espacio = " " * contador
        asterisco = "*" * m
        print(f"{espacio}{asterisco}")
        contador -= 1
        contador_2 += 1
    print("________________________________________________________________")


Numero_filas = int(input("Ingrese el número de filas: "))
Piramide_1(Numero_filas)
Piramide_2(Numero_filas)
Piramide_3(Numero_filas)
Piramide_4(Numero_filas)
