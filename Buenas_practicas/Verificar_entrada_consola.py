'''
Jennifer Marlene Gutierrez Beteta
07 de enero de 2025.
Descripción:
Ejercicio 1, Parcial 3.
'''
'''
#prueba_numero = int(input("Ingresa un número:"))
print()

cadena = input("Ingresa cadena:").strip() # Recibe la cadena.
#
print(cadena.isnumeric())
print(cadena.isalpha())
print(cadena.isalnum())

numero = input("Ingresa un número:").strip() # Recibe la cadena, (strip) elimina los espacios.
while not numero.isnumeric(): # Sirven para números enteros positivos incluyendo al cero.
    print("Opción no válida")
    numero = input("Intenta nuevamente:").strip()
print()
numero = int(numero)
print(f"El número { numero} es de tipo {type(numero)}") # Función (type) para saber el tipo de dato.

def cadena_a_entero(cadena):
    No_guiones = cadena.count("-") # Recibe la cadena y cuenta los espacios o guiones.
    Revisar_cadena = cadena.lstrip("-") # Elimina los guiones de la izquierda (solo los de la izquierda y la derecha).
    if Revisar_cadena.isnumeric() and No_guiones in (0,1): # Que el número de guiones sea entre 0 o 1.
        return int(cadena) # Returna la cadena en entero.
    else:
        return None # No returna nada. 
'''
def cadena_a_flotante(cadena):
    No_guiones = cadena.count("-")  # Recibe la cadena y cuenta los espacios o guiones.
    No_puntos = cadena.count(".") # # Recibe la cadena y cuenta los puntos.
    Revisar_cadena = cadena.lstrip("-").replace(".","") # Elimina los guiones de la izquierda y los puntos.
    if Revisar_cadena.isnumeric() and No_puntos in (0,1) and No_guiones in (0,1) : # Que el número de puntos sea entre 0 o 1.
        return float(cadena) # Returna la cadena en entero.
    else:
        return None # No returna nada.

num_cadena = input("Ingresa un número:").strip()
numero = cadena_a_flotante(num_cadena)
while numero is None: # None, no regresa nada.
    print("Opción no válida")
    num_cadena = input("Ingresa otra vez:").strip()
    numero = cadena_a_flotante(num_cadena)
print(f"El número { num_cadena} es de tipo {type(num_cadena)}")

