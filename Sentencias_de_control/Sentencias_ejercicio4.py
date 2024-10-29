'''
Jennifer Marlene Gutierrez Beteta
23 de octubre de 2024
Descripción:
Sentencia ejercicio 4.
Este programa determinará si te permiten el acceso al bar "La Negra".
'''

print("*** Acceso al bar 'La negra' ***")
print(" ")
edad = int(input("Ingresa tu edad: "))      #Ingresa su edad, se hace la conversión de cadena a entero.
presupuesto = float(input("Ingresa tu presupuesto: $"))   #Ingresa su presupuesto, se hace la conversión de cadena a flotante.

if edad >=18 and presupuesto > 250:     #Conciciones tener al menos 18 años y tener al menos $ 250.00 para gastar
    print("¡Bienvenido a tu mejor bar!")
else:
    print("Lo sentimos, estamos por cerrar.")
