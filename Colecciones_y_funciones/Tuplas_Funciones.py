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

def calificacion(calificaciones):
    promedio_parcial = sum(calificaciones[0.2])/3
    promedio_final = promedio_parcial + (calificaciones[3])/2
    return (promedio_parcial, promedio_final)

primer_parcial = float(input("Ingresa la calificación del 1 parcial:"))
segundo_parcial = float(input("Ingresa la calificación del 2 parcial:"))
tercer_parcial = float(input("Ingresa la calificación del 3 parcial:"))
ordinario = float(input("Ingresa la calificación del ordinario:"))
# Se crea una tupla.

calificaciones = (primer_parcial, segundo_parcial, tercer_parcial, ordinario)
print(calificaciones)
promedio_parcial, promedio_final = calificacion(calificaciones)

if esta_aprobado:
    print("¡Felicidades aprobaste!")
else:
    print("Lo siento, no aprobaste...")

print(f"(El promedio de los parciales es  : {promedio_parcial: 1.f} y el promedio final es: {promedio_final: 1.f}")