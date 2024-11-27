'''
Jennifer Marlene Gutierrez Beteta
21 de noviembre de 2024.
Descripción:
Ejercicio 1 Tuplas.
Este programa muestra el valor máximo y mínimo de una lista de números. En este caso, la tupla se utiliza para devolver los valores máximo y mínimo de la función.
.
'''


'''
Se debe mostrar el siguiente menú:

  ***  Valor máximo y mínimo de una lista de números del usuario  ***

1) Ver lista de números.

2) Añadir número a la lista.

3) Determinar el valor máximo y mínimo de la lista de números.

0) Salir.

Cualquier otro caso -> Opción no válida.'''

#Galilea Peralta Contreras.
#19 de noviembre del 2024.
#Descripción:
#Este programa muestra el valor máximo y mínimo de una lista de números proporcionada por el usuario.

"""
Este programa muestra el valor máximo y mínimo de una lista de números. En este caso, la tupla se utiliza para devolver los valores máximo y mínimo de la función.
Se debe mostrar el siguiente menú:
  ***  Valor máximo y mínimo de una lista de números del usuario  ***
1) Ver lista de números.
2) Añadir número a la lista.
3) Determinar el valor máximo y mínimo de la lista de números.
0) Salir.
Cualquier otro caso -> Opción no válida.
Para ello:
a) Se sugiere utilizar una función para mostrar el menú.
b) Se debe utilizar una única función para devolver el valor máximo y mínimo en una tupla.
"""
#Función que muestra el menú.
def Menu():
    print("*** Listas de compras**+")
    print()
    print("[0].- Salir")
    print("[1].- Ver lista de números")
    print("[2].- Añadir un número a la lista")
    print("[3].- Determinar el valor máximo y mínimo de la lista de números")
    print()

    Opcion = int(input("Ingrese la opcion: "))
    return Opcion

#Función que recibe una lista de números y devuelve el máximo y mínimo en una tupla.
def Maximos_Minimos(Tupla_Numeros):
    cont = 1
    Numero_Elementos = len(Tupla_Numeros)
    Tupla_Maximo_Minimo = ()
    Maximo,Minimo = Tupla_Numeros[0],Tupla_Numeros[0]
    while cont < Numero_Elementos:
        if Tupla_Numeros[cont] > Maximo: # Se modifica el  máximo si se encuentra un valor mayor.
            Maximo = Tupla_Numeros[cont]
        else:
            if Tupla_Numeros[cont] < Minimo:  #Actualiza el mínimo si se encuentra un valor menor.
                Minimo = Tupla_Numeros[cont]
        cont += 1
    Tupla_Maximo_Minimo = Maximo,Minimo
    return Tupla_Maximo_Minimo # Retorna una tupla con el máximo y mínimo.


Opcion = None
Tupla_Numeros = ()
Numero_Guardado = []
while Opcion != 0:
    Opcion = Menu()
    if Opcion == 0:
        print("Fin del programa")
    elif Opcion == 1: # Mostrar la lista de números.
        if len(Tupla_Numeros) != 0:
            print(f"La lista de número es: {Tupla_Numeros},")
        else:
            print("No hay números para mostrar")
        print()
    elif Opcion  == 2:  # Añadir un número a la lista.
        print()
        Numero_añadido = float(input("Ingrese el número a la lista: "))
        Numero_Guardado.append(Numero_añadido)
        Tupla_Numeros = (Numero_Guardado)
        print(f"¡El número {Numero_añadido} se agrego con exito!")
        print()

    elif Opcion  == 3:  #Determinar el valor máximo y mínimo de la lista.
        print()
        if len(Tupla_Numeros) != 0:
            Numero_maximo,Numero_minimo = Maximos_Minimos(Tupla_Numeros)
            print("El número maximo de la lista es: ", Numero_maximo)
            print("El número minimo de la lista es: ", Numero_minimo)
        else:
            print("No hay números")
        print()
    else:
        print()
        print("Opción incorrecta")
        print()
print()
print("Salio del programa")