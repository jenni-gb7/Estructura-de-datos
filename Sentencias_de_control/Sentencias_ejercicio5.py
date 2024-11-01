'''
Jennifer Marlene Gutierrez Beteta
23 de octubre de 2024
Descripción:
Sentencia ejercicio 5.
Este programa determinará el promedio de una materia e indicará si el alumno aprobó o no la materia.
'''

print("*** Programa para calcular el promedio de una materia ***")
print(" ")

#Ingresa su calificaión, se hace la conversión de cadena a entero.
parcial_1 = int(input("Ingresa la calificación del parcial 1:"))
parcial_2 = int(input("Ingresa la calificación del parcial 2:"))
parcial_3 = int(input("Ingresa la calificación del parcial 3:"))
ordinario = int(input("Ingresa la calificación del ordinario:"))

#Se realiza la operación. para el promedio.
promedio = ((parcial_1 + parcial_2 + parcial_3)/3) * 0.5 + (ordinario * 0.5)

#Si el promedio es mayor a 6, aprobaron.
if promedio >=6:
    print(f"La calificación final es: {promedio:.1f}. ¡Felicidades¡ Aprobaste.")
#Si el promedio es menor a 6, reprobaron.
else:
    print(f"La calificación final es: {promedio:.1f}. Lo siento, no aprobaste")
