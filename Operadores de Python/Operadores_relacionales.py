'''
Jennifer Marlene Gutierrez Beteta
16 de octubre de 2024
Descripción:
Operadores relacionales
'''

#Se solicitan dos numeros
num1= input("ingresa su número:")       #Se solicitan 2 números.
num2= input("ingresa su número:")

num1=int(num1)      #Se hace la conversión de cadena a entero.
num2=int(num2)

#se toman los 2 primeros decimales con .2f.
#Se hacen las comparaciones y como resultado True o False depende el caso, si es verdadero o falso.

print(f"¿El {num1: .2f} es mayor  {num2: .2f}? {num1>num2}")
print(f"¿El {num1: .2f} es mayor igual a {num2: .2f}? {num1>=num2}")
print(f"¿El {num1: .2f} es igual {num2: .2f}? {num1==num2}")
print(f"¿El {num1: .2f} es menor {num2: .2f}? {num1<num2}")
print(f"¿El {num1: .2f} es menor igual {num2: .2f}? {num1<=num2}")
print(f"¿El {num1: .2f} es diferente {num2: .2f}? {num1!=num2}")
