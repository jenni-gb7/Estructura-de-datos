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

# Función del menú.
def Menu_1():
    print()
    print("***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***")
    print("[1].- Convertir de decimal a binario y hexadecimal.")
    print("[2].- Convertir de binario a decimal y hexadecimal.")
    print("[3].- Convertir de hexadecimal a decimal y binario.")
    print("[4].- Mostrar Ob y Ox.")
    print("[5].- Suma de binarios.")
    print("[0].- Salir.")
    print()
    Opcion = int(input("Ingresa una de las opciones: "))
    return Opcion

# Función de decimal a binario.
def Decimal_a_binario(Decimal):
    Binario = [] # Se declara la lista.
    while Decimal > 0:
        Residuo_b = Decimal % 2 # Se calcula el residuo de dividir el número decimal entre 2 para obtener el bit.
        Binario.append(Residuo_b) # Los residuos se almacenan en una lista.
        Decimal = Decimal // 2
    Binario.reverse()   # Invertimos la lista para que el orden sea correcto.
    return tuple(Binario) # El resultado final se convierte en una tupla.

# Función de decimal a hexadecimal.
def Decimal_a_hexadecimal(Decimal):
    Hexadecimal = [] # Se declara la lista.
    Hex_digitos = "0123456789ABCDEF"  # Dígitos hexadecimales.
    while Decimal > 0:
        Residuo_H = Decimal % 16 # Se calcula el residuo de dividir el número decimal entre 16.
        Hexadecimal.append(Hex_digitos[Residuo_H]) # Los residuos se almacenan en una lista junto a los dígitos hexadecimales.
        Decimal = Decimal // 16
    Hexadecimal.reverse() # Invertimos la lista para que el orden sea correcto.
    return tuple(Hexadecimal) # El resultado final se convierte en una tupla.

# Función de binario decimal.
def Binario_a_decimal(Binario):
    # Convertir binario a decimal manualmente usando una tupla para los bits.
    Decimal = 0
    Potencia = 0
    for bit in reversed(Binario):  # Se recorre el binario desde el último bit hacia el primero usando reversed.
        Decimal += bit * (2 ** Potencia) # Se suma bit x2.
        Potencia += 1 # La potencia aumenta en cada iteración.
    return Decimal # El resultado.

# Función de binario a hexadecimal.
def Binario_a_hexadecimal(Binario):
    # Convertir binario a decimal
    Decimal = 0
    Potencia = 0
    for bit in reversed(Binario): # Se recorre el binario desde el último bit hacia el primero usando reversed.
        Decimal += bit * (2 ** Potencia) # Se suma bit x2.
        Potencia += 1 # La potencia aumenta en cada iteración.

    # Convertir el decimal a hexadecimal
    Hex_digitos = "0123456789ABCDEF"  # Dígitos hexadecimales.
    Hexadecimal = [] # Se declara la lista.

    if Decimal == 0:
        Hexadecimal.append('0')  # Para el caso de 0

    while Decimal > 0:
        Residuo_H = Decimal % 16 # Se calcula el residuo de dividir el número decimal entre 16.
        Hexadecimal.append(Hex_digitos[Residuo_H]) # Los residuos se almacenan en una lista junto a los dígitos hexadecimales.
        Decimal = Decimal // 16

    # Invertimos la lista para obtener el orden correcto
    Hexadecimal.reverse()
    return tuple(Hexadecimal) # Convertimos a tupla.

# Función de hexadecimal a decimal.
def Hexadecimal_a_decimal(Hexadecimal):
    # Diccionario para convertir cada dígito hexadecimal a su valor decimal
    Hex_a_decimal = {
        '0': 0, '1': 1, '2': 2, '3': 3,
        '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11,
        'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    # Convertir el número hexadecimal a decimal
    Decimal = 0
    Potencia = 0
    for digito in reversed(Hexadecimal.upper()):
        Decimal += Hex_a_decimal[digito] * (16 ** Potencia)
        Potencia += 1
    # Convertir el número decimal a una tupla de dígitos
    Decimal_tupla = tuple(int(d) for d in str(Decimal))
    return Decimal_tupla

# Función de hexadecimal a binariol.
def Hexadecimal_a_binario(Hexadecimal):
    # Diccionario de los valores hexadecimales a binarios
    Hex_a_bin = {
        '0': (0, 0, 0, 0), '1': (0, 0, 0, 1), '2': (0, 0, 1, 0), '3': (0, 0, 1, 1),
        '4': (0, 1, 0, 0), '5': (0, 1, 0, 1), '6': (0, 1, 1, 0), '7': (0, 1, 1, 1),
        '8': (1, 0, 0, 0), '9': (1, 0, 0, 1), 'A': (1, 0, 1, 0), 'B': (1, 0, 1, 1),
        'C': (1, 1, 0, 0), 'D': (1, 1, 0, 1), 'E': (1, 1, 1, 0), 'F': (1, 1, 1, 1)
    }
    # Convertir cada carácter hexadecimal a su equivalente binario
    Binario = []
    for digito in Hexadecimal.upper():  # Asegurarnos de que sea mayúscula
        Binario.extend(Hex_a_bin[digito]) # Nos genera el número en binario pero con 3 ceros de más en la izquierda.
    # Eliminar los primeros 3 bits de más.
    Binario = Binario[3:]
    return tuple(Binario)

def Suma_de_binarios(Num1_binario,Num2_binario):
    Suma = []
    Suma = Num1_binario + Num2_binario
    return tuple(Suma)

Opcion = None
while Opcion != 0:  # El juego continúa mientras el jugador no elija salir.
    Opcion = Menu_1()
    if Opcion == 0:
        print()
        print("Fin del programa.") # Salir del programa.
    elif Opcion == 1:
        print()
        # Se le solicita un número al usuario.
        Decimal = int(input("Ingresa el número en base decimal:"))
        # Llamar a la función para convertir decimal a binario.
        Resultado_B = Decimal_a_binario(Decimal)
        # Llamar a la función para convertir decimal a hexadecimal.
        Resultado_H = Decimal_a_hexadecimal(Decimal)
        # Mostrar el resultado.
        print("El número decimal", Decimal, "es", *Resultado_B,  "en binario y", *Resultado_H, "en hexadecimal.")
        print("-----------------------------------------------------------------------")
    elif Opcion == 2:
        print()
        # Se le solicita un número al usuario.
        Binario = input("Ingresa el número en base binaria (como una secuencia de 0s y 1s): ")
        # Convertir la entrada en una tupla de números binarios (0s y 1s)
        Binario = tuple(int(b) for b in Binario)  # Convierte cada carácter a entero y crea la tupla.
        # Llamar a la función para convertir binario a decimal.
        Resultado_D = Binario_a_decimal(Binario)
        # Llamar a la función para convertir binario a hexadecimal.
        Resultado_BH = Binario_a_hexadecimal(Binario)
        # Mostrar el resultado
        print("El número binario",*Binario,"es",Resultado_D,"en decimal y",*Resultado_BH,"en hexadecimal.")
        print("-----------------------------------------------------------------------")
    elif Opcion == 3:
        print()
        # Se le solicita un número al usuario.
        Num_hexadecimal = input("Ingresa el número en base hexadecimal: ")
        # Llamar a la función para convertir hexadecimal a binario.
        Resultado_HB = Hexadecimal_a_binario(Num_hexadecimal)
        # Llamar a la función para convertir hexadecimal a decimal.
        Resultado_HD = Hexadecimal_a_decimal(Num_hexadecimal)
        # Mostrar el resultado
        print(f"El número hexadecimal",Num_hexadecimal, "es",*Resultado_HD," en decimal Y",*Resultado_HB, "en binario.")
        print("-----------------------------------------------------------------------")
    elif Opcion == 4:
        print()
        print("El número decimal", Decimal, "es Ob", *Resultado_B, "y","Ox",*Resultado_H, ".")
    elif Opcion == 5:
        print()
        Num1_binario = input("Ingresa el número en base binaria (como una secuencia de 0s y 1s): ")
        # Convertir la entrada en una tupla de números binarios (0s y 1s)
        Num1_binario = tuple(int(b) for b in Num1_binario)  # Convierte cada carácter a entero y crea la tupla.
        Num2_binario = input("Ingresa el número en base binaria (como una secuencia de 0s y 1s): ")
        # Convertir la entrada en una tupla de números binarios (0s y 1s)
        Num2_binario = tuple(int(b) for b in Num2_binario)  # Convierte cada carácter a entero y crea la tupla.
        # Llamar a la función para suma.
        Suma = Suma_de_binarios(Num1_binario,Num2_binario)
        # Mostrar el resultado.
        print("La suma de binarios es:",*Suma)
    else:
        print("Opción no válida.")
print("-----------------------------------------------------------------------")

