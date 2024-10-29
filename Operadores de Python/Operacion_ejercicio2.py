'''
Jennifer Marlene Gutierrez Beteta
17 de octubre de 2024
Descripción:
Ejercicio 2.
Este programa revisa si la persona forma parte de la comunidad estudiantil.
'''

# Se debe responder con si/no.
var_uno = input("¿Es profesor de la UNSIJ?")
var_dos = input("¿Es estudiante de la UNSIJ?")

var_uno = var_uno.lower()=="si"     #Se hace la conversión de cadena a booleano.
var_dos = var_dos.lower()=="si"

print(f"Forma parte de la comunidad estudiantil? {var_uno or var_dos}") #Se utiliza la condición "or" (o).
#NOTA:
#Con al menos uno que sea si, ya sea la var_uno o var_dos se imprime que es True, es decir que al menos alguno de ellos pertenece a la comunidad estudiantil.