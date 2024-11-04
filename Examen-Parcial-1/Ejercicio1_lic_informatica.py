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

# Solicita un número en consola.
num1 = int(input("Ingresa el número final de la cuenta :"))
print(f"Los números del 1 al {num1} son:")

# Se inicializa el contador.
contador = 1

# Se declara la condición del ciclo while.
# Mientras el contador sea menor igual al número ingresado, si se cumple esta condición entra en el ciclo.
while contador <= num1:

# La secuencia if-elif-else es la forma de "si las condiciones anteriores no son verdaderas, entonces prueba esta condición", es decir los número entrará en la condición que se adapte mejor a ellos.

    # Condición: Si el contador es últiplo de 3 y 5.
    if contador %3 == 0 and contador %5 == 0:
        #Se sustituyen estos números por la frase "Licenciatura en Informática" y se imprima un salto de línea en lugar de la coma.
        print("Licenciatura en Informática",end=" ")
        print()
    # Condición: Si el contador es 3 o sus múltiplos.
    elif contador %3 == 0:
        #Se sustituyen estos números por la palabra "Licenciatura", separado por una coma.
        print("Licenciatura,",end=" ")
    # Condición: Si el contador es 3 o sus múltiplos.
    elif contador %5 == 0:
        # Se sustituyen estos números por la palabra "Informática", separado por una coma.
        print("Informática,",end=" ")
        # Si no cumple ninguna de estas conciciones.
    else:
        # Solo imprime el número de manera normal, separado por una coma.
        print(contador, end=", ")
    contador += 1
