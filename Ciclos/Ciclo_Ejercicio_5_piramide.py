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
# Se olicita al usuario el número de filas para las pirámides.
Numero_filas = int(input("Ingrese el número de filas: "))

print()
print("Pirámide 1:")
for j in range (1,Numero_filas + 1):
    asterisco = "*" * j
    print(f"{asterisco}")
print("/////////////////////////////////////////////")

print()
print("Pirámide 2:")
contador = Numero_filas
for i in range (1,Numero_filas+ 1):
    asterisco = "*" * contador
    print(f"{asterisco}")
    contador -= 1
print("/////////////////////////////////////////////////////////////")

print()
print("Pirámide 3:")
contador = Numero_filas
contador_2 = 0
for k in range (1,Numero_filas+ 1):
    espacio = " " * contador
    asterisco = "*" * (k + contador_2)
    print(f"{espacio}{asterisco}")
    contador -= 1
    contador_2 += 1
print("///////////////////////////////////////////////////////")


print()
print("Pirámide 4:")
contador = Numero_filas
contador_2 = 0
for l in range (1,Numero_filas + 1):
    espacio = " " * contador
    asterisco = "*" * l
    print(f"{espacio}{asterisco}")
    contador -= 1
    contador_2 += 1
print("//////////////////////////////////////////////////////////")
