'''
Jennifer Marlene Gutierrez Beteta
16 de octubre de 2024
Descripción:
Operadores Lógicos.
Se pide una expresión y se debe convertir en True y False
'''

expresion1=input("Ingresa la expresión:")   #Se solicita una expresión.
expresion1=expresion1.lower()=="si"         #Condición para convertir de True y False
print(expresion1)

expresion2=input("Ingresa la expresión:")   #Se solicita una expresión.
expresion2=expresion2.lower()=="si"         #Condición para convertir de True y False
print(expresion2)

#NOTA:
#Si la expresión es "si", imprimirá True.
#Si la expresión es "no", imprimirá False.

#Se hacen las comparaciones logicas and, or y not.
print(f"¿Ambos fueron si?: {expresion1 and expresion2}")    #Comparación si las expresiones son iguales.
print(f"¿Ambos fueron si?: {expresion1 or expresion2}")     #Comparación si al menos una expresión es si.
print(f"¿Ambos fueron si?: {not expresion1}")   #Comparación que imprime lo contrario a lo que se ingresó.
#Si se ingresa "si" el resultado sera False y si se ingresa "no# el resultado sera True.
print(f"¿Ambos fueron si?: {not expresion2}")