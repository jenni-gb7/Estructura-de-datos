'''
Jennifer Marlene Gutierrez Beteta
21 de enero de 2025.
Descripción:
Ejercicio 2, Parcial 3.
'''
# Kwargs: Funciona como
def Preferencias(tema: str, ** kwargs):
    print(f"El tema es {tema}")
    for key,value in kwargs.items():
        print(f"Nombre: {key} prefiere {value}")


if __name__ == '__main__':
    Preferencias("comida", Rebeca = "Mole", Juan = "Tacos", Bryan = "Tlayudas", Yamileth = "Tamales")