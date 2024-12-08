'''
Jennifer Marlene Gutierrez Beteta
02 de diciembre de 2024.
Descripción:
Este programa convierte números entre las bases decimal, binaria y hexadecimal.'''


'''
Escribe un programa de nombre Ej2_conversiones_decimal_binario_hexadecimal.py que realice lo que se indica en la descripción del programa.

 ***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***

1) Convertir de decimal a binario y hexadecimal.

2) Convertir de binario a decimal y hexadecimal.

3) Convertir de hexadecimal a decimal y binario.

0) Salir.

Cualquier otro caso -> Opción no válida.

Para ello:

a) Utilice la lógica adecuada para mostrar las conversiones. No utilice funciones como bin() o hex().

b) Asuma que el usuario siempre va a ingresar números en el formato adecuado. Por ejemplo: 1001 como número binario o 1F como hexadecimal, no 120 como número binario o 1Z como hexadecimal.

c) Para considerar el ejercicio como completo, utilice funciones para mostrar el menú y para las conversiones entre bases, considerando que cada función devuelve una tupla. Por ejemplo, la función que recibe el número decimal debe devolver el valor en binario y en hexadecimal como una tupla.
'''

'''def Menu_1():
    print("***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***")
    print("[0].- Salir.")
    print("[1].- Convertir de decimal a binario y hexadecimal.")
    print("[2].- Convertir de binario a decimal y hexadecimal.")
    print("[3].- Convertir de hexadecimal a decimal y binario.")
    print()
    Opcion = int(input("Ingresa una opción: "))
    return Opcion'''

Numero_1 = int(input("Ingresa un numero:"))

def Decimal_a_binario(Numero_1):
    Binario = " "
    while Numero_1 > 0:
        if Numero_1 % 2 == 0:
            Binario = "0" + Binario
        else:
            Binario = "1" + Binario
            Numero_1 = Numero_1 // 2
    return  Binario

Binario = Decimal_a_binario(Numero_1)
print(Binario)
