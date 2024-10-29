'''
Jennifer Marlene Gutierrez Beteta
23 de octubre de 2024
Descripción:
Sentencia if else.
Programa que determina si un número es par e impar.
'''

#if condicion:
    #Condicion a ejecutar.
    #La condicion es verdadera.

#else:
    #Código que se ejecuta.
    #Con verdadero.

num1= input("Ingresa tu edad:")     #Se ingresa la edad.
num1=int(num1)                      #Conversión de cadena a entero.

if int(num1 %2 == 0):               #Condición si el módulo de el numero es igual a cero.
    print("El número es par")       #Se imprime que es par.
else:
    print("El número es impar")     #Sino se imprime que es impar.