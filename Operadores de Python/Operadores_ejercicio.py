'''
Jennifer Marlene Gutierrez Beteta
17 de octubre de 2024
Descripción:
Ejercicio 1.
'''

print("Compras mayores a $5000.00")
print()

cantidad=input("Ingresa la cantidad:")      #Se ingresa una cantidad.
interes=input("¿Compra a meses sin en intereses?")  #Se ingresa si o no.

cantidad=int(cantidad)              #Se hace la conversión de cadena a entero.
interes =interes.lower()=="si"      #Se hace la conversión de cadena a booleano.

print(f"¿Aplica bonificación? {cantidad > 5000 and interes }")   #Si la cantidad es menor a 5000 y si compra a meses sin interés.
#Se imprime False, sino aplica a la bonificación y aplica si imprime True.

