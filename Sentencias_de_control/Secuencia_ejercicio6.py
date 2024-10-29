'''
Jennifer Marlene Gutierrez Beteta
23 de octubre de 2024
Descripción:
Sentencia ejercicio 6.
Programa para calcular el costo de un tour turístico de acuerdo con el número de adultos, niños y el día de la visita
'''

print("*** Programa para calcular el promedio de una materia ***")
print(" ")


#si la visita son los lunes, martes y jueves, se tiene un descuento del 10 %.

#Ingresa sus datos, se hace la conversión de cadena a entero.
nombre = input("Ingresa el nombre del cliente: ")
adultos = int(input("Ingresa el número de adultos: "))
niños = int(input("Ingresa el número de niños: "))
dia = input("Ingresa el día de la semana: ")

dia = dia.lower()

#Precio de un adulto: $ 200.00
#Precio de un niño: $ 100.00
total = (adultos * 200) + (niños * 100)

print()
# si la visita son los lunes, martes y jueves, se tiene un descuento del 10 %.
if dia == "lunes"  or dia == "martes" or dia == "jueves":
    total = total - (total * 0.1)
    print(f"Gracias por su visita {nombre} este día {dia}. El costo total es de {total:.2f}.")
else:
    print(f"Gracias por su visita {nombre} este día {dia}.El costo total es de {total:.2f}.")