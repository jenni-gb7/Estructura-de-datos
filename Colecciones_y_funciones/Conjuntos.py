'''
Jennifer Marlene Gutierrez Beteta
25 de noviembre de 2024.
Descripción:
Conjuntos.
'''

# Desordenado.
# Mutables.

print()
print("*** Ejemplos de uso de los conjuntos ***")
print(" ")

Conjuntos_nombres = set()
print(f"Conjunto_vacio: {Conjuntos_nombres}")
# Palabra reservada "Set" para crear un conjunto vacio.
print("-------------------------------------------------")
# Se añaden valores al conjunto.

Conjuntos_nombres.add("Rebeca")
Conjuntos_nombres.add("Juan")
Conjuntos_nombres.add("Yami")
Conjuntos_nombres.add("Bryan")
Conjuntos_nombres.add("Galilea")
Conjuntos_nombres.add("Rosalinda")
Conjuntos_nombres.add("Jenni")
Conjuntos_nombres.add("Tania")
Conjuntos_nombres.add("Hector")
Conjuntos_nombres.add("Paty")
Conjuntos_nombres.add("Addi")
Conjuntos_nombres.add("Alberto")

print(f"Conjunto 303: {Conjuntos_nombres}")
print("-------------------------------------------------")
# Añadiendo elementos repetidos.

Conjuntos_nombres.add("Rebeca")
Conjuntos_nombres.add("Juan")
Conjuntos_nombres.add("Yami")
Conjuntos_nombres.add("Bryan")
Conjuntos_nombres.add("Galilea")
Conjuntos_nombres.add("Rosalinda")
Conjuntos_nombres.add("Jenni")
Conjuntos_nombres.add("Tania")
Conjuntos_nombres.add("Hector")
Conjuntos_nombres.add("Paty")
Conjuntos_nombres.add("Addi")
Conjuntos_nombres.add("Alberto")

print(f"Conjunto 303: {Conjuntos_nombres}")
print("-------------------------------------------------")
# Se eliminan elementos del conjunto.
Conjuntos_nombres.remove("Rebeca")
print(f"Conjunto 303: {Conjuntos_nombres}")
print("-------------------------------------------------")
# Mostrar todos los elementos
for nombre in Conjuntos_nombres:
    print(nombre, end=",")
print("-------------------------------------------------")
# Pertenece a un conjunto o a una lista.
print()
print(f"¿El elemento pertenece al conjunto?{"Rebeca" in Conjuntos_nombres}")
print(f"¿El elemento  pertenece al conjunto? {"Jenni" in Conjuntos_nombres}")
print("-------------------------------------------------")
# Nuevo conjunto de números.
Conjuntos_numeros = {12.1,12,3.2,-2.3,4.1}

# Funciones básicas:
print(f"Tamaño del conjunto : {len(Conjuntos_numeros)}")
print(f"suma de conjuntos:{sum(Conjuntos_numeros)}")
