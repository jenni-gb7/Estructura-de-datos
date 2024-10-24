'''
Jennifer Marlene Gutierrez Beteta
23 de octubre de 2024
Descripción:
Sentencia if else.
Programa que determina si un numero es par e impar.
'''

#if condicion:
    #Condicion a ejecutar.
    #La condicion es verdadera.

#else:
    #Codigo que se ejecuta.
    #Con verdadero.

num1= input("Ingresa tu edad:")
num1=int(num1)

if int(num1 %2 == 0):
    print("El número es par")
else:
    print("El número es impar")