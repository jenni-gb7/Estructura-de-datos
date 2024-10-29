'''
Jennifer Marlene Gutierrez Beteta
23 de octubre de 2024
Descripción:
Sentencia ejercicio 3.
Este programa determinará un descuento en compras en "La cona".
'''

print("*** Descuento por ser miembro de la cona ***")
print(" ")
cantidad = float(input("Ingrese la cantidad comprada: $"))     #Ingresa la cantidad, se hace la conversión de cadena a flotante.
membresia = input("¿Cuenta con la memebresía si/no ?")         #Tiene menbresia, si/no.
membresia=membresia.lower()=="si"           #Se convierte la cadena a booleano.

#Se inicializan variables en 0.
total_pagar=0
descuento= 0

#Se declararan las condiciones.
if membresia and cantidad <1000:                #Si tiene membresía, obtiene un 5 % de descuento en todas sus compras.
    descuento = 0.05  #El descuento del 5%.
    print("Tu descuento es del 5%.")
    descuento= cantidad * descuento
    total_pagar = cantidad - descuento
    print((f"El total a pagar es: $ {total_pagar:.2f}"))
elif cantidad >=1000 :                      #Si tiene la membresía y su compra fue mayor o igual a $ 1000.00, entonces el descuento es del 8 %.
    descuento = 0.08  # El descuento del 8%.
    print("Tu descuento es del 8%.")
    descuento = cantidad * descuento
    total_pagar = cantidad - descuento
    print((f"El total a pagar es: $ {total_pagar:.2f}"))
else:                                           #Si no tiene la membresía, no obtiene ningún descuento y se invita a ser miembro.
    print("Se te invita a ser miembro para tener un descuento")
    print((f"El total a pagar es: $ {cantidad:.2f}"))
