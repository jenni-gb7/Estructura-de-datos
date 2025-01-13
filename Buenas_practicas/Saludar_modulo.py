'''
Jennifer Marlene Gutierrez Beteta
13 de enero de 2025.
Descripción:
Ejercicio 2, Parcial 3.
'''

def Saludar(nombre: str ) -> int | None:
    print(f" Hola {nombre}")

if __name__ == '__main__':
    Nombre = input("Ingresa un nombre: ")
    Saludar(Nombre)