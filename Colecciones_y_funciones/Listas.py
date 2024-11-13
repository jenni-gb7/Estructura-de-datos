'''
Jennifer Marlene Gutierrez Beteta
12 de noviembre de 2024.
Descripción:
Listas.
'''
from Ciclos.Ejercicio_3 import contador

# Crear lista.
'''
alumnos = ["Addi", "Jesus","Juan"]
alumnos.append("Hector")

print(alumnos)
print(alumnos[1])
alumnos.append("Tania")
print(alumnos)
for alumnos in alumnos:
    print(alumnos, end =",")'''


#//////////////////////////
alumnos = []
alumnos.append("Rosalinda")
alumnos.append("Juan")
alumnos.append("Lourdes")
alumnos.append("Tania")
alumnos.append("Bryan")
alumnos.append("Rebeca")
alumnos.append("Jennifer")
alumnos.append("Hector")
alumnos.append("Galilea")
alumnos.append("Patricia")
alumnos.append("Alberto")
alumnos.append("Addi")

#print(alumnos)

len(alumnos)
print(alumnos)
print()

print("-------------------------------------------------------")

alumnos.sort()
print(alumnos)
print()

print("-------------------------------------------------------")

alumnos.sort(reverse = True)
print(alumnos)
print()

print("-------------------------------------------------------")


alumnos.pop()
print(alumnos)
print()

