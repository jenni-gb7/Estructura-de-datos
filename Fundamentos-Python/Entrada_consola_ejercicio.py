'''
Jennifer Marlene Gutierrez Beteta
18 de octubre de 2024
Descripción:
Escribe un programa de nombre Entrada_consola_ejercicio.py que realice lo siguiente.
a) Pida 2 números decimales por consola al usuario utilizando la función input.

b) Muestre los resultados de las operaciones básicas con esos números: suma, resta, multiplicación y división.

Nota: Asuma que el usuario siempre va a ingresar números y que el segundo número es diferente de cero
'''

# En la funcion input se convierte el valor a un tipo de dato adecuado por eso se solicitan para hacer operaciones matemáticas con ellos.
#a)
num_uno = float(input("Introduce el primer número decimal: "))
num_dos = float(input(f"Introduce el segundo número decimal:"))

if num_dos != 0:    #Se declara la condición de que el número sea diferente de cero, para hacer las operaciones.

    #Operaciones matemáticas.
    suma = num_uno + num_dos
    resta = num_uno - num_dos
    multi = num_uno * num_dos
    division = num_uno / num_dos
    print()  # Se realiza un salto de línea.
    # Impresión de los resultados de las operaciones.
    # b)
    print(" ****  Resultados  ****")

    print(f"La suma de {num_uno: 2.f} y {num_uno: 2.f} es: {suma: 2.f}")
    print(f"La resta  de {num_uno: 2.f} y {num_uno: 2.f} es: {resta: 2.f}")
    print(f"La multiplicación de {num_uno: 2.f} y {num_uno: 2.f} es: {multi: 2.f}")
    print(f"La división de {num_uno: 2.f} y {num_uno: 2.f} es: {division: 2.f}")

else:
    print("El segundo número no puede ser 0. Intente nuevamente.")  #No se cumple la condición.





