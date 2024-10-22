'''
Jennifer Marlene Gutierrez Beteta
18 de octubre de 2024
Descripción:
Entrada de datos por consola para interacturar con el usuario con valores dinámicos.
'''

# Comentar sobre la función input.
# En la funcion input se convierte el valor a un tipo de dato adecuado por eso se solicitan para hacer operaciones matemáticas con ellos
numero1_cadena = input("Introduce un número decimal: ") #Se solicitan números para hacer operaciones matemáticas.
numero2_cadena = input("Introduce otro número decimal: ")
resultado_cadena = numero1_cadena + numero2_cadena # Verificar qué es lo que realiza esta instrucción (ver el print).
print()     #Se realiza un salto de linea.
print(" ****  Recibir número sin un casting de varibles  ****")
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}")    #Se imprimen los 2 números concatenados

# Comentar por qué se realiza el casting de variables.
# Es necesario hacer la conversión de los datos, que no son del tipo de dato requerido,
numero1_float = float(numero1_cadena)   #Se hace la conversión de la cadena a un número flotante.
numero2_float = float(numero2_cadena)
resultado_float = numero1_float + numero2_float # Verificar qué es lo que realiza de esta manera y compáralo.
print()
print(" ****  Casting de varibles  ****")
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}")   #Se imprimen la suma de los 2 números.



