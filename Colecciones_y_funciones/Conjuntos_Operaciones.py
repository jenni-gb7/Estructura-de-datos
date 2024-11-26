'''
Jennifer Marlene Gutierrez Beteta
26 de noviembre de 2024.
Descripción:
Conjuntos: Operaciones básicas.
'''
# Se crean 2 conjuntos, A y B.

Conjunto_A = {11,7,10,9,5,1,15,7}
Conjunto_B = {55,70,11,77,66,9,5}
print(f"Conjunto A: {Conjunto_A}")
print(f"Conjunto B: {Conjunto_B}")

print(" ")
print("*** Operaciones básicas  ***")
print(" ")
# Unión de conjuntos.
union = Conjunto_A|Conjunto_B
print(f"Unión: {union}")
# Intersección de conjuntos.
interseccion = Conjunto_A&Conjunto_B
print(f"intersección: {interseccion}")
# Diferencia de conjuntos.
diferencia = Conjunto_A-Conjunto_B
print(f"diferencia: {diferencia}")

print("--------------------------------------------------------------")
# Convertir de listas a conjuntos.
# Viceversa.
Lista_Original = ["leon", "lepardo","aguila","gato","capibara","chapulin","venado","leopardo"]
print(f"Lista Original: {Lista_Original}")
# Convertir de lista a conjuntos.
Conjunto_Animales = set(Lista_Original)
print(f"Conjunto Animales: {Conjunto_Animales}")
Lista_Modificada = list(Conjunto_Animales)
print(f"Lista Modificada: {Lista_Modificada}")
Tupla_animales = tuple(Lista_Modificada)
print(f"Tupla animales: {Tupla_animales}")

