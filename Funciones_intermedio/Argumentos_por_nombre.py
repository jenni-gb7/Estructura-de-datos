'''
Jennifer Marlene Gutierrez Beteta
15 de enero de 2025.
Descripción:
Ejercicio 2, Parcial 3.
'''


def Imprimir_alumno(Nombre: str,Matricula: int,Grupo: int,Semestre: int)-> None:    # Definición de la función y tipo de datos.
    print("***DATOS PERSONALES***")
    print(f"Nombre: {Nombre} \nMatricula: {Matricula} \nGrupo: {Grupo} \nSemestre: {Semestre} ")


def main() -> None:
    Nombre = "Jennifer"
    Matricula = 11233456
    Grupo = 303
    Semestre = 3

    Imprimir_alumno(Nombre,Matricula,Grupo,Semestre) # Llamada a la función imprimir_alumno.


if __name__ == '__main__':  # indica si el código es el que se ejecuta.
    main()  # Llamada de la función a nivel de módulo.
