'''
Jennifer Marlene Gutierrez Beteta
23 de octubre de 2024
Descripción:
Sentencia if elif else.
Programa que determina si un numero es par e impar.
'''

#If elif else condición:
#Tiene que buscar en que condición entrar, sino se cumple la primera, se va con la segunda y así sucesivamente hasta llegar al else.

num1= input("Ingresa tu edad:")     #Se ingresa la edad.
num1=int(num1)                      #Conversión de cadena a entero.

if num1 <= 14:                                      #Condición si el número es menor a 14.
    print("Pertenece a niños y adolescentes.")
elif num1 >= 15 and num1 <=25:                      #Condición si el número es mayor igual a 15 y menor igual 25.
    print("Pertenece a jovenes.")
elif num1 >= 26 and num1 <=45:                       #Condición si el número es mayor igual a 26 y menor igual 45.
    print("Pertenece a adultos jovenes.")
elif num1 >= 46 and num1 <= 60:                      #Condición si el número es mayor igual a 46 y menor igual 60.
    print("Pertenece a adultos maduros.")
else:
    print("Pertenece a adultos mayores.")           #Condición sino pertenece a ninguno de los anteriores.





