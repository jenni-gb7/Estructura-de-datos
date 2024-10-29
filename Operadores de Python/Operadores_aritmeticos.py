'''
Jennifer Marlene Gutierrez Beteta
15 de octubre de 2024
Descripción:
Operadores aritmeticos

'''
#NOTAS:
#Se solicitan 2 números:

usuario1= input("ingresa su número:")   #Se se solicita un número.
usuario2= input("ingresa su número:")

usuario1=int(usuario1)                  #Se hace la conversión de cadena a entero.
usuario2=int(usuario2)


print(usuario1 + usuario2)             #Imprime la suma de los 2 números.
print(usuario1 - usuario2)             #Imprime la resta de los 2 números.
print(usuario1 * usuario2)             #Imprime la multiplicación de los 2 números.
print(usuario1 / usuario2)             #Imprime la división de los 2 números con un solo decimal.
print(usuario1 ** usuario2)            #Se eleva la variable usuario1, las veces que sea la variable usuario2.
print(usuario1 // usuario2)            #Imprime la división de los 2 números, sin decimales.
divi= usuario1 / usuario2
print(f"El resultado : {divi: .2f}")   #Imprime la division con 2 decimales
