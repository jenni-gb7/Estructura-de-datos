'''
Jennifer Marlene Gutierrez Beteta
15 de octubre de 2024
Descripción:
Ejercicio 4.
Este programa determinará True o False de acuerdo a las expresiones.
'''
# Declarar variables.
VALOR1= "False"
VALOR2= "True"
VALOR3= "True"
VALOR4= "False"

print("*** Expresión booleana  ***")
print(" ")
valor1 = input("Ingresa un valor booleano V/F:")           #Pedir usuario un valor booleano.
valor2 = input("Ingresa un valor booleano V/F:")
valor3 = input("Ingresa un valor booleano V/F:")
valor4 = input("Ingresa un valor booleano V/F:")

res=(valor1 or valor2) and (valor3 or valor4)       #Hacer la comparación de los valores.
print(f"El resultado de la expresion booleana es:{res}")

