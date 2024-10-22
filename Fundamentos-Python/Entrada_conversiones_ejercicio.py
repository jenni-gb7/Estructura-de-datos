'''
Jennifer Marlene Gutierrez Beteta
18 de octubre de 2024
Descripción:
Escribe un programa de nombre Entrada_conversiones_ejercicio.py que realice lo siguiente:

a) Pida los datos de los profesores utilizando nombres de variables adecuadas, la función input y el casting:

Nombre (cadena).
No. de cubículo (int).
Horas de que imparte clase a la semana (float con 3 decimales).
¿Tiene más de 5 años en la unsij? (booleno).
b) Muestre los datos en consola de forma adecuada.

Nota: Asuma que el usuario siempre va a ingresar números cuando se requiera.
'''

# Pedir los datos del profesor
nombre = input("Ingrese el nombre del profesor: ")  #Se pide el nombre en una cadena.
cubiculo = int(input("Ingrese el número de cubículo: "))    #Se ingresa en una cadena y se convierte a entero.
horas_clase = float(input("Ingrese las horas que imparte clase a la semana (con 3 decimales): "))   ##Se ingresa en una cadena y se convierte a decimal.
anos_unsij = input("¿Tiene más de 5 años en la UNSIJ? (Sí/No): ")
anos_unsij = anos_unsij.lower() == "si" #Se convierte a booleano.


# Mostrar los datos ingresados en consola
# Imprime los datos de profesor.
print("\nDatos del Profesor:")
print(f"Nombre: {nombre}")
print(f"Número de cubículo: {cubiculo}")
print(f"Horas que imparte clase a la semana: {horas_clase:.3f}")    #Imprime las horas con los 3 primeros decimales.
print(f"Tiene más de 5 años en la UNSIJ: {anos_unsij}")     #imprime True o False.
