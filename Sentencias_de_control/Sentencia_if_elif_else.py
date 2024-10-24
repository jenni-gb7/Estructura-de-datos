'''
Jennifer Marlene Gutierrez Beteta
23 de octubre de 2024
Descripción:
Sentencia if elsif else.
Programa que determina si un numero es par e impar.
'''

#If elif else condición:
#Tiene que buscar en que condición entrar.

num1= input("Ingresa tu edad:")
num1=float(num1)

if num1 <= 14:
    print("Pertenece a niños y adolescentes.")
elif num1 >= 15 and num1 <=25:
    print("Pertenece a jovenes.")
elif num1 >= 26 and num1 <=45:
    print("Pertenece a adultos jovenes.")
elif num1 >= 46 and num1 <= 60:
    print("Pertenece a adultos maduros.")
else:
    print("Pertenece a adultos mayores.")





