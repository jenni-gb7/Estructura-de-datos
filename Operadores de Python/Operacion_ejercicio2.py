'''
Jennifer Marlene Gutierrez Beteta
17 de octubre de 2024
Descripción:
Ejercicio 2.
'''

var_uno = input("¿Es profesor de la UNSIJ?")
var_dos = input("¿Es estudiante de la UNSIJ?")

var_uno = var_uno.lower()=="si"


print(f"Forma parte de la cominudad estudiantil? {var_uno or var_uno}")