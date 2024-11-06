'''
Jennifer Marlene Gutierrez Beteta
06 de noviembre de 2024.
Descripción:
Ciclo for.
'''

# Ciclo for.
# Sintaxis for variable in secuencia.
# En este ejemplo se imprime caracter a caracter de la cadena ingresada y se cuenta el total de caracteres.

cadena_usuario = input("Ingresa una cadena: ")
#cadena_usuario = cadena_usuario.lower()
contador_caracter= 0
for caracter in cadena_usuario:
   contador_caracter +=1
   print(f" {caracter}", end=" ")
print()
print(contador_caracter)
print()

# Se declara un arreglo de nombres.
# Se imprimirá un mensaje de "Hola", con el nombre de cada uno.
alumnos = ["Rosalinda","Juan", "Lourdes", "Tania","Bryan", "Rebeca", "Jennifer", "Hector", "Galilea", "Patricia", "Alberto", "Addi"]
for alumno in alumnos:
    print(f"Hola {alumno}")
print()

# Función range (rango), imprimirá los números del 1 al 10 separados por una coma (,).
for i in range(1,11):
    print(i,end=", ")