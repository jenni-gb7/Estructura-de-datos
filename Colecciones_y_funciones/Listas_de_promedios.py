'''
Jennifer Marlene Gutierrez Beteta
13 de noviembre de 2024.
Descripción:
Ejericio 3, Listas de promedio.
'''

'''
Escribe un programa de nombre Listas_ej3_calificaciones.py que realice lo siguiente:
Este programa es una lista de las calificaciones de los alumnos del Parcial 1. La lista está conformada por el nombre del alumno y sus calificaciones.
Cada alumno tiene 5 calificaciones: estructuras de datos, derecho, contabilidad, álgebra y electrónica.
Se debe mostrar el siguiente menú:

  ***  Calificaciones del Parcial 1  ***
1) Ver calificaciones de todos los alumnos.
2) Ver calificaciones detalladas de un alumno.
3) Ver promedios del Parcial 1 de todos los alumnos.
4) Ver promedio grupal del Parcial 1.
5) Agregar alumno y sus calificaciones.
6) Eliminar alumno y sus calificaciones.
0) Salir.

Cualquier otro caso -> Opción no válida.
Para ello:
a) Se sugiere utilizar funciones para modular el código.
b) Se sugiere utilizar listas para las cinco calificaciones, los nombres y las calificaciones de los alumnos.
c) Todas las calificaciones y promedios se deben mostrar únicamente con un decimal.'''

# Función para el menú.
def Menu():
    print("*** Promedios del parcial 1. **+")
    print()
    print("0) Salir.")
    print("1) Ver calificaciones de alumno.")
    print("2) Ver calificaciones de los alumnos.")
    print("3) Ver promedios del Parcial 1 de todos los alumnos.")
    print("4) Añadir alumno.")
    print("5) Eliminar alumno.")
    print("6) Ver promedio grupal.")
    print()
    Opcion = int(input("Ingresa una opción: "))
    return Opcion

Estructura_datos = []
Derecho = []
Contabilidad = []
Algebra = []
Electronica = []
Ingles = []
# Se agrupan las materias en una lista.
Calificaciones = [Estructura_datos, Derecho, Contabilidad, Algebra, Electronica,Ingles]
indice = 0
# Declara la varible.
Opcion = None

while Opcion != 0:
    Opcion = Menu()
    if Opcion  == 0: # Salir del programa.
        print("Fin de programa.")
    elif Opcion  == 1: #Ver calificaciones de un alumno.
        print()
        if len(Estructura_datos) != 0: #Verifica si hay alumnos registrados.
             Numero_alumno = int(input("Ingrese el numero del alumno que deseas ver: "))
             print("Calificacion del alumno ",Numero_alumno)
             print(f" Estructura de datos: {Estructura_datos[Numero_alumno]: .1f}.")
             print(f" Derecho: {Derecho[Numero_alumno]: .1f}.")
             print(f" Contabilidad: {Contabilidad[Numero_alumno]: .1f}.")
             print(f" Electronica: {Electronica[Numero_alumno]: .1f}.")
             print(f" Ingles: {Ingles[Numero_alumno]: .1f}.")
             print()
        else:
            print("No hay alumnos por ver.")
            print()
    elif Opcion == 2: # Ver calificaciones de todos los alumnos.
        print()
        if len(Estructura_datos) != 0:
            for Calificacion in Calificaciones:
                print(f" {Calificacion}")
        else:
            print("No hay alumnos por ver.")
        print()
    elif Opcion == 3:  # Ver promedios de todos los alumnos.
        if len(Estructura_datos) != 0:
            Numero_alumnos = len(Estructura_datos)
            Contador = 0
            Promedio_alumno = 0
            Total_p = 0
            while Contador < Numero_alumnos:
                Promedio_de_un_alumno = (Estructura_datos[Contador] + Derecho[Contador] + Contabilidad[Contador] +
                                         Algebra[Contador] + Electronica[Contador] + Ingles[Contador]) / 6
                print(f"El promedio del alumno {Contador} es: {Promedio_alumno:.1f}.")
                Contador += 1
        else:
            print("No hay alumnos.")


    elif Opcion  == 4: # Agregar alumno y sus calificaciones.
        print()
        print("Ingrese las calificaciones del alumno")
        Estructura_agregado = float(input("Estructuras de datos: "))
        Derecho_agregado = float(input("Derecho: "))
        Contabilidad_agregado = float(input("Contabilidad: "))
        Algebra_agregado = float(input("Algebra: "))
        Electronica_agregado = float(input("Electronica: "))
        Ingles_agregado = float(input("Ingles: "))

        Calificaciones[0].append(Estructura_agregado)
        Calificaciones[1].append(Derecho_agregado)
        Calificaciones[2].append(Contabilidad_agregado)
        Calificaciones[3].append(Algebra_agregado)
        Calificaciones[4].append(Electronica_agregado)
        Calificaciones[5].append(Ingles_agregado)

        print()
    elif Opcion  == 5:  # Eliminar un alumno.
        Eliminar_alumno = int(input("Ingrese el numero del alumno que deseas eliminar: "))
        del Estructura_datos[Eliminar_alumno]
        del Derecho[Eliminar_alumno]
        del Contabilidad[Eliminar_alumno]
        del Algebra[Eliminar_alumno]
        del Electronica [Eliminar_alumno]
        del Ingles[Eliminar_alumno]

    elif Opcion == 6:  # Ver promedio grupal.
        if len(Estructura_datos) != 0:
            Numero_alumnos = len(Estructura_datos)
            Contador = 0
            Promedio_alumno = 0
            Total_p  = 0
            while Contador < Numero_alumnos:
                #Si fuera la otra forma de lista , se podria utilizar la funcion sum
                Promedio_de_un_alumno = (Estructura_datos[Contador] + Derecho[Contador] + Contabilidad[Contador] + Algebra[Contador] + Electronica[Contador] + Ingles[Contador])/6
                Total_p  = Total_p  + Promedio_alumno
                Contador += 1
            Total_p  = Total_p  / Numero_alumnos
            print(f"El promedio grupal es: {Total_p : .1f}.")
        else :
            print()
            print("No hay alumnos que promediar.")
        print()
    else: # Opción no válida.
        print()
        print("Opción incorrecta.")
        print()