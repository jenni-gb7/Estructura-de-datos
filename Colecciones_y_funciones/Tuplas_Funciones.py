'''
Jennifer Marlene Gutierrez Beteta
20 de noviembre de 2024.
Descripción:
Ejercicio Tuplas Funciones .
'''

print()
print("*** Calificaciones del semestre ***")
print(" ")

# Se crea la función.

def Promedios(calificaciones):
    Promedio_parcial = sum(calificaciones[0:3])/3
    Promedio_final = (Promedio_parcial + calificaciones[3])/2
    return Promedio_parcial, Promedio_final

parcial1 = float(input("Ingresa la calificación del Parcial 1: "))
parcial2 = float(input("Ingresa la calificación del Parcial 2: "))
parcial3 = float(input("Ingresa la calificación del Parcial 3: "))
ordinario = float(input("Ingresa la calificación del Ordinario: "))
print()

calificaciones = (parcial1, parcial2, parcial3, ordinario)
print(calificaciones)

Promedio_parcial, Promedio_final= Promedios(calificaciones)

print(f"(El promedio de los parciales es  : {Promedio_parcial: .1f} y el promedio final es: {Promedio_final: .1f}")