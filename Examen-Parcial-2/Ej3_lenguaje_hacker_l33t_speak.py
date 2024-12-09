'''
Jennifer Marlene Gutierrez Beteta
02 de diciembre de 2024.
Descripción:
Este programa convierte un texto al lenguaje hacker (lenguaje leet o 1337). Esta escritura se caracteriza por reemplazar las letras por números y símbolos.'''

'''
Escribe un programa de nombre Ej3_lenguaje_hacker_l33t_speak.py que realice lo que se indica en la descripción del programa.
Este programa convierte un texto al lenguaje hacker (lenguaje leet o 1337). Esta escritura se caracteriza por reemplazar las letras por números y símbolos.
Lenguaje básico:

En el lenguaje básico se sustituye cada vocal por un número.
La A se convierte en un 4, la E en un 3, la I en un 1 y la O en un cero.
La letra U es una excepción, ya que no hay un número obvio, por lo que se sustituye por (_).


Lenguaje intermedio:

En el lenguaje intermedio también se sustituyen las consonantes por números o signos de puntuación.
Por ejemplo, la B se convierte en I3, la C en [, la D en ), la L en 1.
Revisa la "Leet speak alphabet" de la página anterior y toma la primera de las opciones para el lenguaje.
Nota que no hay caracteres acentuados, por lo no se deben de convertir.


Se debe mostrar el siguiente menú:

  ***  Ejercicio 3. Lenguaje hacker (l33t sp34k).  ***

1) Convertir un texto a lenguaje básico.

2) Convertir un texto a lenguaje intermedio.

0) Salir.

Cualquier otro caso -> Opción no válida.

Para ello:

a) Utilice la lógica adecuada para mostrar las conversiones. No utilice funciones como bin() o hex().

a) Utilice la lógica adecuada para convertir el texto al lenguaje hacker básico o intermedio, según sea el caso.

b) Se debe convertir los caracteres sin importar si son mayúsculas o minúsculas, sin modificar los caracteres que no se convirtieron. Ejemplos con el lenguaje básico: hola -> h0l4, Hola -> H0l4, HOLA -> H0L4.
'''
# Función para el ménu.
def Menu_2():
    print()
    print("****  Ejercicio 3. Lenguaje hacker (l33t sp34k).  ***")
    print("[1].- Convertir un texto a lenguaje básico.")
    print("[2].- Convertir un texto a lenguaje intermedio.")
    print("[0].- Salir.")
    print()
    # Se le solicita al usuario una opción.
    Opcion = int(input("Ingresa una de las opciones: "))
    return Opcion

# Función para el lenguaje básico.
def Lenguaje_basico_vocales(Texto_usuario):
    Texto_convertido = ""  # Cadena vacía para almacenar el resultado
    for Letra in Texto_usuario:
         # Reemplazar vocales minúsculas y mayúsculas.
        if Letra == 'a' or Letra == 'A':
            Texto_convertido += '4'
        elif Letra == 'e' or Letra == 'E':
            Texto_convertido += '3'
        elif Letra == 'i' or Letra == 'I':
            Texto_convertido += '1'
        elif Letra == 'o' or Letra == 'O':
            Texto_convertido += '0'
        elif Letra == 'u' or Letra == 'U':
            Texto_convertido += '(_)'
        else:
            Texto_convertido += Letra  # Dejar el carácter sin cambios.
    return Texto_convertido

# Función para el lenguaje intermedio.
def Lenguaje_intermedio_consonantes(Texto_usuario):
    Texto_convertido = ""  # Cadena vacía para almacenar el resultado
    for Letra in Texto_usuario:
        # Reemplazar vocales minúsculas y mayúsculas.
        if Letra == 'a' or Letra == 'A':
            Texto_convertido += '4'
        elif Letra == 'e' or Letra == 'E':
            Texto_convertido += '3'
        elif Letra == 'i' or Letra == 'I':
            Texto_convertido += '1'
        elif Letra == 'o' or Letra == 'O':
            Texto_convertido += '0'
        elif Letra == 'u' or Letra == 'U':
            Texto_convertido += '(_)'
        # Reemplazar consonantes minúsculas y mayúsculas.
        elif Letra == 'b' or Letra == 'B':
            Texto_convertido += 'I3'
        elif Letra == 'c' or Letra == 'C':
            Texto_convertido += '['
        elif Letra == 'd' or Letra == 'D':
            Texto_convertido += ')'
        elif Letra == 'f' or Letra == 'F':
            Texto_convertido += '|='
        elif Letra == 'g' or Letra == 'G':
            Texto_convertido += '&'
        elif Letra == 'h' or Letra == 'H':
            Texto_convertido += '#'
        elif Letra == 'j' or Letra == 'J':
            Texto_convertido += ',_|'
        elif Letra == 'k' or Letra == 'K':
            Texto_convertido += '>|'
        elif Letra == 'l' or Letra == 'L':
            Texto_convertido += '1'
        elif Letra == 'm' or Letra == 'M':
            Texto_convertido += '/\\/\\'
        elif Letra == 'n' or Letra == 'N':
            Texto_convertido += '|\\|'
        elif Letra == 'p' or Letra == 'P':
            Texto_convertido += '|*'
        elif Letra == 'q' or Letra == 'Q':
            Texto_convertido += '(_,)'
        elif Letra == 'r' or Letra == 'R':
            Texto_convertido += 'I2'
        elif Letra == 's' or Letra == 'S':
            Texto_convertido += '5'
        elif Letra== 't' or Letra == 'T':
            Texto_convertido += '7'
        elif Letra == 'v' or Letra == 'V':
            Texto_convertido += '\\/'
        elif Letra == 'w' or Letra == 'W':
            Texto_convertido += '\\/\\/'
        elif Letra == 'x' or Letra == 'X':
            Texto_convertido += '><'
        elif Letra== 'y' or Letra == 'Y':
            Texto_convertido += 'j'
        elif Letra == 'z' or Letra == 'Z':
            Texto_convertido += '2'
        else:
            Texto_convertido += Letra # Dejar el carácter sin cambios.
    return Texto_convertido

Opcion = None
while Opcion != 0:  # El juego continúa mientras el jugador no elija salir.
    Opcion = Menu_2()
    if Opcion == 0:
        print()
        print("Fin del programa.") # Salir del programa.
    elif Opcion == 1:
        print()
        # Solicitar al usuario que ingrese el texto
        Texto_usuario = input("Ingresa el texto a convertir a lenguaje l33t básico: ")
        # Convertir el texto usando la función
        Texto_convertido = Lenguaje_basico_vocales(Texto_usuario)
        # Mostrar el resultado
        print()
        print("El texto convertido es:")
        print(Texto_convertido)
        print("---------------------------------------------------------")
    elif Opcion == 2:
        print()
        # Solicitar al usuario que ingrese el texto
        Texto_usuario = input("Ingresa el texto a convertir a lenguaje l33t intermedio: ")
        # Convertir el texto usando la función
        Texto_convertido = Lenguaje_intermedio_consonantes(Texto_usuario)
        # Mostrar el resultado
        print()
        print("El texto convertido es:")
        print(Texto_convertido)
        print("---------------------------------------------------------")
    else:
        print()
        print("Opción no válida.")
print("-----------------------------------------------------------------------")
    

