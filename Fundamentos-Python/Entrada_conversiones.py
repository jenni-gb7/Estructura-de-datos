'''
Jennifer Marlene Gutierrez Beteta
18 de octubre de 2024
Descripción:
Conversión de cadenas a int, float y boolean mediante la interacción con consola.
'''

# Comentar sobre las funciones anidadas.
print("****   Datos de los alumnos    *****")
nombre = input("Ingresa el nombre: ")
semestre = int(input("Ingresa el no. de semestre: "))   #Se solicita un valor y se convierte la cadena a entero.
promedio = float(input("Ingresa el promedio: "))        #Se solicita un valor y se convierte la cadena a flotante.
es_mujer = input("¿Es mujer (Si/No)?: ")

# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si" #Se convierte a booleano y imprime True o False.

# Se imprimen los datos del alumno.
# Comentar  qué es lo que realiza {promedio:.2f} probando con números diferentes.
# Te imprime el número con 2 de sus decimales.
print()
print(f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")  #Se imprimen todos l0s valores en la misma línea.