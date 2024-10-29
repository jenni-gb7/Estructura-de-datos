'''
Jennifer Marlene Gutierrez Beteta
23 de octubre de 2024
Descripción:
Sentencia ejercicio 1.
Este programa determinará cuál de dos números ingresados por el usuario es menor o si son iguales..
'''


#Se solicitan dos numeros.
num_1 =input("Ingresa un número decimal:")
num_2 = input("Ingresa otro número decimal:")

num_1 =float(num_1)     #Conversión de cadena a decimal.
num_2 =float(num_2)

if num_1<=num_2:                                        #Condición si, se imprime el letrero.
    print(f"El {num_1: .2f} es menor {num_2: .2f} ")

