'''
Jennifer Marlene Gutierrez Beteta
14 de octubre de 2024
Descripción:
Usos de los tipos básico de datos en Python.
'''

# Notas:
"""
En Python, no se requiere indicar el tipo de la variable en su declaración.
Los valores básicos que pueden almacenar las variables son:
- Int.
- Float.
- String (str).
- Boolean. True o False (con inicial mayúscula).
- None. Tipo especial que representa una ausencia de valor.
"""
# Ejemplos de tipos de datos.

# Número entero
mi_variable_entera = -100                           #Se declara la variable entero.
print("Tipo de dato entero:",mi_variable_entera)    #Se imprime la variable entero.

# Número decimal
mi_variable_decimal = 12.12                         #Se declara la variable decimal.
print("Tipo de dato decimal:", mi_variable_decimal) #Se imprime la variable decimal.

# Cadena de texto
mi_variable_texto_nombre = "Jennifer"                #Se declara la cadena nombre.
mi_variable_texto_apellido = 'Gutierrez'             #Se declara la cadena apellido.
print("Cadena de texto:", mi_variable_texto_nombre, mi_variable_texto_apellido)     #Se imprime la cadena de nombre y adelante se imprime la cadena apellido.

# Booleno
mi_variable_booleana = True                     #Se declara la variable Booleno.
print('Tipo booleano:', mi_variable_booleana)   #Se imprime  la variable Booleno.

# None
mi_variable_none = None                     #Se declara la variable None.
print("Tipo none:",mi_variable_none)        #Se imprime  la variable None.

# Uso de constantes.
'''
En Python, a diferencia de otros lenguajes de programación, no existe un tipo específico para definir constantes.
Se utiliza una convención de colocar las variables en mayúsculas y no modificarlas.
'''
VARIABLE_CONSTANTE = 3.1416                                                #Se declara la variable constante.
print("Ejemplo de convención de una constante:", VARIABLE_CONSTANTE)       #Se imprime  la variable constante.

#Notas :
"""En este caso el programa te muestra:
- Un tipo de dato entero.
- Un tipo de dato decimal.
- Una cadena de texto, en este caso imprime el nombre junto al apellido.
- Un tipo de dato none.
- Un ejemplo de constante.
"""
