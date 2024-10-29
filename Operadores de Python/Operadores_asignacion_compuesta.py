'''
Jennifer Marlene Gutierrez Beteta
16 de octubre de 2024
Descripción:
Se utilizan para comparar 2 valores
'''
#Nota: pendiente modificar
num1= input("ingresa su número:")       #Se solicitan 2 números.
num2= input("ingresa su número:")

num1=int(num1)      #Se hace la conversión de cadena a entero.
num2=int(num2)

num1 +=3
print(num1)     #Imprime la suma de la variable num1 + 3.
num2 -=5
print(num2)     #Imprime la resta de la variable num2 - 5.
num1 *=2
print(num1)     #Imprime el resultado de la multiplicación de la suma anterior * 2.
num2 /=4
print(num2)     #Imprime el resultado de la división de la resta anterior / 4.


print(" ")
num1=8
num2=11

num1+=num2
num1*=num1
num1-=num2
num1 +=3
num1 /=2

print(f"el resultado es: {num1} {num2}")          #Imprime el resultado final de las operaciones anteriores.

