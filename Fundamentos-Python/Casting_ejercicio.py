'''
Jennifer Marlene Gutierrez Beteta
14 de octubre de 2024
Descripción:
Realizar un programa poniendo en practica lo que vimos en Conversión de tipos de datos (casting) en Python.
'''

#NOTA:

'''La conversión de tipos de datos implica manipular datos que no están en el tipo de dato requerido. Ejemplos:
de cadena a entero, de cadena a número flotante, y viceversa.'''

#a) Convierta los siguientes números en cadenas: 3.14159265, 12, 0.
# *****   Conversión de número a cadena     *****

primer_num= 3.14159265                  #Declaramos nuestras variables.
segundo_num= 12
tercer_num= 0

print()
print("Conversión de número a cadena.")
print()
print(f"El número {primer_num} se convierte a cadena  str(primer_numero): {str(primer_num)}")
print(f"El número {segundo_num} se convierte a cadena  str(segundo_numero): {str(segundo_num)}")
print(f"El número {tercer_num} se convierte a cadena  str(tercer_numero): {str(tercer_num)}")

#b) De los números anteriores, indica su valor booleano.
# Valores anteriores convertidos a booleanos.
print()
print("Conversión a booleanos.")
print()

val_booleano = bool(primer_num)        #Se crean variables del valor booleano utilizando las variables anteriores.
print(f"¿El valor de {primer_num} es verdadero? {val_booleano}.")

val_booleano = bool(segundo_num)
print(f"¿El valor de {segundo_num} es verdadero? {val_booleano}.")

val_booleano = bool(tercer_num)
print(f"¿El valor de {tercer_num} es verdadero? {val_booleano}.")


#c) Convierta las siguientes cadenas a números: "10002", "100.02", "0".

primer_num = "10002"        # Reutilizamos nuestras variables anteriores.
primer_num_int = int(primer_num)      # Creamos una nueva variable.

segundo_num = "100.02"
segundo_num_float = float(segundo_num)

tercer_num = "0"
tercer_num_int = int(tercer_num)

# Imprimimos
print()
print("Conversión de cadena a numero.")
print()

print("Conversión de cadena a flotante.")
print(f"Número como cadena: {primer_num_int}.")

print("Conversión de cadena a entero.")
print(f"Número como cadena: {segundo_num_float}.")

print("Conversión de cadena a entero.")
print(f"Número como cadena: {tercer_num_int}.")

#d) De las cadenas anteriores, indica su valor booleano. Nota: especificar por qué el resultado de la cadena "0".

#valores anteriores indicando su valor booleano.
print()
print("Conversión a booleanos.")
print()

val_booleano = bool(primer_num_int)      #Se crean variables del valor booleano utilizando las variables anteriores.
print(f"¿El valor de {primer_num_int} es verdadero? {val_booleano}.")

val_booleano = bool(segundo_num_float)
print(f"¿El valor de {segundo_num_float} es verdadero? {val_booleano}.")

val_booleano = bool(tercer_num_int)
print(f"¿El valor de {tercer_num_int} es verdadero? {val_booleano}.")
print("Si el valor es 0, la función bool regresa False ya que las únicas condiciones para que sea False son que el valor sea 0, que el contenido de la variable este vacía o que el valor sea None.")
