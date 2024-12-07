'''
Jennifer Marlene Gutierrez Beteta
21 de noviembre de 2024.
Descripción:
Ejercicio 1 Tuplas.
Este programa permite obtener la ecuacion de la recta.
.
'''
'''
Escribe un programa de nombre Tuplas_ej2_coordenadas.py que realice lo siguiente:
Este programa almacena diversos puntos como coordenadas y permite obtener la ecuación de la recta entre dos de los puntos.
Se debe mostrar el siguiente menú:
  ***  Rectas a partir de puntos (coordenadas) en el plano cartesiano  ***
1) Ver coordenadas almacenadas.
2) Agregar coordenada (x,y)
3) Calcular la pendiente y la ecuación de la recta entre dos coordenadas.
4) Eliminar coordenada (x,y).
0) Salir.

Cualquier otro caso -> Opción no válida.
Para ello:
a) Utilice funciones para modular el código.
b) Utilice una tupla para almacenar las coordenadas (x,y) del punto.
c) Utilice una lista para almacenar las tuplas de las coordenadas.
'''
#Función para mostrar el menú.
def Menu():
    print("***  Rectas a partir de puntos (coordenadas) en el plano cartesiano  ***")
    print()
    print("[0].- Salir.")
    print("[1].- Ver coordenadas almacenadas.")
    print("[2].- Agregar coordenada (x,y).")
    print("[3].- Calcular la pendiente y la ecuación de la recta entre dos coordenadas.")
    print("[4].- Eliminar coordenada (x,y).")
    print()

    Opcion = int(input("Ingrese la opción: "))
    return Opcion

# Lista para las coordenadas como tuplas (x, y)
Lista_cordenadas = []
Opcion = None

while Opcion != 0:
    Opcion = Menu()
    if Opcion == 0:
        print()
        print("Fin del programa.")
    elif Opcion == 1:  # Ver las coordenadas.
        print()
        if len(Lista_cordenadas) != 0:
            Numero = 1
            for Lista_cordenada in Lista_cordenadas:
                print(f"Cordenada {Numero} es: {Lista_cordenada}.")
                Numero += 1
        else:
            print("No hay coordenadas.")
        print()
    elif Opcion  == 2:  # Agregar una nueva coordenada.
        print()
        X = float(input("Ingrese la coordenada x: "))
        Y = float(input("Ingrese la coordenada y: "))
        Tupla_coordenadas = (X,Y)
        Lista_cordenadas.append(Tupla_coordenadas)
        print(F"Se agrego con exito las cordenadas {X:.1f} y {Y:.1f}.")
        print()
    elif Opcion == 3:  # Calcular la pendiente y la ecuación de la recta entre dos coordenadas.
        if len(Lista_cordenadas) != 0:
            Numero = 1
            for Lista_cordenada in Lista_cordenadas:
                print(f"Cordenada {Numero} es: {Lista_cordenada}")
                Numero += 1
            print()
            Indice_1 = int(input("Ingrese el indice de la primera coordenada: "))
            Indice_2 = int(input("Ingrese el indice de la segunda coordenada: "))
            x1, y1 = (Lista_cordenadas[Indice_1-1])
            x2, y2 = (Lista_cordenadas[Indice_2-1])

            # Pendiente: y = mx + b

            m = (y2 - y1) / (x2 - x1)
            b = y1 - m * x1
            print("La pendiente es: ",m)
            print(f"Expresión de la recta es: y = {m}x + ({b}).")
        else:
            print("No hay coordenadas.")

    elif Opcion  == 4:
        if len(Lista_cordenadas) != 0:
            Eliminar_coordenada = int(input("Ingrese el indice de la coordenada que quiera eliminar: "))
            del Lista_cordenadas[Eliminar_coordenada-1]
        else:
            print("No hay coordenadas por eliminar.")
            print()

    else:
        print()
        print("Opción incorrecta.")
        print()