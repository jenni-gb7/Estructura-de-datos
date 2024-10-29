'''
Jennifer Marlene Gutierrez Beteta
23 de octubre de 2024
Descripción:
Sentencia ejercicio 2.
Este programa determinará la estación del año de acuerdo al número de mes ingresado por el usuario.
'''

print("*** Estaciones del año ***")
num1 = input("Ingresa el número del mes:")
num1 = int(num1)

if num1 >= 3 and num1 <=5:                                      #Condición si el número es mayor a 3 y menor a 5.
    print("La estación es: Primavera.")
elif num1 >= 6 and num1 <=8:                      #Condición si el número es mayor igual a 6 y menor igual 8.
    print("La estación es: Verano.")
elif num1 >= 9 and num1 <=11:                       #Condición si el número es mayor igual a 9 y menor igual 11.
    print("La estación es: Otoño.")
elif num1 ==12 or num1 >= 1 and num1 <= 2:                 #Condición si el número es igual a 12 o el número mayor igual a 1 y menor igual 2.
    print("La estación es: Invierno.")
else:
    print("Mensaje de mes incorrecto..")           #Condición sino pertenece a ninguno de los anteriores.
