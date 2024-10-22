'''
Jennifer Marlene Gutierrez Beteta
16 de octubre de 2024
Descripción:
Se pide una expresion y se debe convertir en True y False
'''

expresion1=input("Ingresa la expresion:")
expresion1=expresion1.lower()=="si"         #condicion para convertir de True y False
print(expresion1)

expresion2=input("Ingresa la expresion:")
expresion2=expresion2.lower()=="si"
print(expresion2)

print(f"¿Ambos fueron si?: {expresion1 and expresion2}")
print(f"¿Ambos fueron si?: {expresion1 or expresion2}")
print(f"¿Ambos fueron si?: {not expresion1}")
print(f"¿Ambos fueron si?: {not expresion2}")