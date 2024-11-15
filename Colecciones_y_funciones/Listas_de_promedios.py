'''
Jennifer Marlene Gutierrez Beteta
13 de noviembre de 2024.
Descripción:
Ejericio 3, Listas de promedio.
'''

alumnos = []
calificaciones = []
promedios = []
opcion= 1
contador = 0

while opcion != 0:
    print(" ")
    print("*** Promedios del parcial 1  ***")
    print(" ")
    print("[0].- Salir")
    print("[1].- Ver calificación de alumno")
    print("[2].- Ver promedio de alumno")
    print("[3].- Añadir alumno")
    print("[4].- Eliminar alumno")
    print("[5].- Ver promedio grupal")
    print(" ")
    opcion = int(input("Ingresa una opción: "))
    if opcion  == 1:
        numero_1 = 0
        for calificacion in calificaciones:
            print(f"Calificaciones: {calificaciones}")
            numero_1+= 1
            print(" ")
    elif opcion == 2:
        numero_2 = 0
        for promedio in promedios:
            print(f" {promedios[numero_2]} {promedios}")
            numero_2 += 1
    elif opcion == 3:
        print()
        calificacion_electronica = float(input("Ingrese la calificación electrónica: "))
        calificaciones.append(calificacion_electronica)
        calificacion_derecho = float(input("Ingrese la calificación derecho: "))
        calificaciones.append(calificacion_derecho)
        calificacion_algebra = float(input("Ingrese la calificación algébra: "))
        calificaciones.append(calificacion_algebra)
        calificacion_contabilidad = float(input("Ingrese la calificación contabilidad: "))
        calificaciones.append(calificacion_contabilidad)
        calificacion_estructura = float(input("Ingrese la calificación estructura: "))
        calificaciones.append( calificacion_estructura)

        contador += 1
        print()
    elif opcion == 4:
        eliminar_alumno = input("Ingrese el producto que desea eliminar: ")
        numero_alumno = 0

        while alumnos[numero_alumno] !=  eliminar_alumno:
            numero_alumno += 1

        alumnos.remove(eliminar_alumno)
        del calificaciones[numero_alumno]

    else:
        print()
        print("Opción incorrecta")
        print()
print()
print("Saliendo del programa...")