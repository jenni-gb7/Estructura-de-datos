'''
Jennifer Marlene Gutierrez Beteta
02 de diciembre de 2024.
Descripción:
Este programa dibuja una escalera, en donde el usuario ingresa el número de escalores. Y si será de manera ascendente o descendente.'''

'''
Escribe un programa de nombre Ej1_escalera.py que realice lo que se indica en la descripción del programa.
Este programa dibuja una escalera, en donde el usuario ingresa el número de escalores.

Si el número es positivo, la escalera será ascendente. Un ejemplo cuando se ingresa un valor de 4:

        _
      _|
    _|
  _|
_|

Si el número es negativo, la escalera será descendente. Un ejemplo cuando se ingresa un valor de -4:

_
 |_
   |_
     |_
       |_

Si el número es cero, se deberá salir del programa.


Se debe mostrar la siguiente pantalla:

  ***  Ejercicio 1. La escalera.  ***

Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir:

Cualquier otro caso -> Opción no válida.

Para ello:

a) Solicite el número de escalones utilizando un ciclo.

b) Muestre la escalera utilizando la lógica adecuada. Se requiere utilizar funciones para dibujar las escaleras para considerar el ejercicio como completo.
'''
# Función para la escalera de manera ascendente positiva.
def Ascendente(Num_de_escalones):
    # Se igualan las variables.
    Guion_bajo = "_"
    Barra_vertical = "|"
    Cont = Num_de_escalones
    Espacio = " "
    print(f"{Espacio * (Cont + 2)}{Guion_bajo}") # Se realiza la impresión del primer guión, antes del primer escalón.
    # Ciclo for para la impresión de la escalera.
    for j in range(1, Num_de_escalones + 1):
        Espacio = " " * Cont
        # Impresión de los escalones.
        print(f"{Espacio}{Guion_bajo}", end="")
        print(f"{Barra_vertical}")
        # El contador que es igual a los espacios decrementa, de acuerdo al número de escalones, de manera descendente.
        Cont += Espacio

# Función para la escalera de manera descendente negativa.
def Descendente(Num_de_escalones):
    # Se igualan las variables.
    Num_de_escalones =   Num_de_escalones + 1 * 1
    Guion_bajo = "_"
    Barra_vertical = "|"
    # Ciclo for para la impresión de la escalera.
    for j in range(1, Num_de_escalones + 1):
        Espacio = " " * j
        # Impresión de los escalones.
        print(f"{Guion_bajo}") # Se realiza la impresión del primer guión, antes del primer escalón.
        print(f"{Espacio}{Barra_vertical}",end="") # Los espacios decrementan de manera descendente.
    print(f"{Guion_bajo}")

Num_de_escalones = None
while Num_de_escalones != 0: # El juego continúa mientras el jugador no elija salir.
    print()
    print("***  Ejercicio 1. La escalera.  ***")
    # Se solicita el número de escalones al usuario.
    Num_de_escalones = int(input("Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir:"))

    if Num_de_escalones == 0: # Salir del programa.
        print()
        print("Fin del programa.")
    elif Num_de_escalones > 0: # El número de escalones es positivo.
        Descendente(Num_de_escalones)
    elif Num_de_escalones < 0: # El número de escalones es negativo.
        Ascendente(Num_de_escalones)
    else:
        print("Opcion no válida.") # Opción inválida.
    print("----------------------------------------------------------")
