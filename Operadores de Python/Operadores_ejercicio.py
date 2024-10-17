'''
Jennifer Marlene Gutierrez Beteta
17 de octubre de 2024
Descripción:
Ejercicio 1.
'''

print("Compras mayores a $5000.00")
print()

cantidad=input("Ingresa la cantidad:")
interes=input("¿Compra a meses sin en intereses?")

cantidad=int(cantidad)
interes =interes.lower()=="si"

print(f"¿Aplica bonificacion? {cantidad > 5000 and interes}")

