'''
Jennifer Marlene Gutierrez Beteta
31 de octubre de 2024
Descripción:
Ejercicio 1, Examen Parcial 1.

Este programa imprime en consola los números, separados por comas, del 1 hasta un número ingresado por el usuario.

Sin embargo, se deben sustituir los siguientes valores:

3 o sus múltiplos por la palabra "Licenciatura".
5 y sus múltiplos por la palabra "Informática".
Múltiplos de 3 y 5 por la frase "Licenciatura en Informática" y se imprima un salto de línea en lugar de la coma.

a) Solicite un número en consola.

b) Realizar la lógica adecuada para imprimir los números o mensajes adecuados.

c) Mostrar los resultados en consola.

'''

print(" ")
print("***  Licenciatura en Informática ***")
print(" ")

# a) Solicite un número en consola.
num1 = int(input("Ingresa el número final de la cuenta :"))
print(f"Los números del 1 al {num1} son:")
contador = 1

while contador <= num1:

    if contador %3 == 0 and contador %5 == 0:
        print("Licenciatura en Informática,",end=" ")
        print()
    elif contador %3 == 0:
        print("Licenciatura,",end=" ")
    elif contador %5 == 0:
        print("Informática,",end=" ")
    else:
        print(contador, end=", ")
    contador += 1
