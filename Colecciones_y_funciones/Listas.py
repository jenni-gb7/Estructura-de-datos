'''
Jennifer Marlene Gutierrez Beteta
12 de noviembre de 2024.
Descripción:
Listas.
'''


#Ordenado: que cada cosa  tiene un orden especifico
#Mutable: es que cambia

# Crear lista.
'''
Alumnos = []
Alumnos.append("Hector")
Alumnos.append("Addi")
Alumnos.append("Alberto")
Alumnos.append("Juan")

print(Alumnos)
print(Alumnos[1])

print()
Alumnos.insert(1,"Tania")
print(Alumnos[1])
print()
for Alumno in Alumnos:
    print(Alumno,end = " ")

Alumnos.remove("Hector")
print(Alumnos)

Alumnos.pop(2)
print(Alumnos)

del Alumnos[2]
print(Alumnos)

'''


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

print(alumnos)

len(alumnos)
print(alumnos)
print()

print("-------------------------------------------------------")
# Ordena de la A-Z.
alumnos.sort()
print(alumnos)
print()

print("-------------------------------------------------------")
# Ordena de la Z-A.
alumnos.sort(reverse = True)
print(alumnos)
print()

print("-------------------------------------------------------")
# Elimina el ultimo de la lista.
alumnos.pop()
print(alumnos)
print()

'''
alumnos.insert(1, "Tania")
alumnos.remove("Héctor")
alumnos.pop(2)
del alumnos[2]

print(alumnos)
for alumno in alumnos:
    print(alumno, end= " ")
'''
