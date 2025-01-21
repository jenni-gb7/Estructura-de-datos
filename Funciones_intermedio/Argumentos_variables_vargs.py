'''
Jennifer Marlene Gutierrez Beteta
21 de enero de 2025.
Descripción:
Ejercicio 2, Parcial 3.
'''

# Vargs: argumentos de variables.
def Colores_Favoritos(Persona: str,* vargs):
    print(f"{Persona} : {vargs}")

def Sumar(* vargs):
    Res = 0
    for i in vargs:
        Res += i
    return Res


# Código a nivel de módulo.
if __name__ == '__main__':
    Colores_Favoritos("Jennifer","Morado","Negro","Blanco","Rosa")
    Colores_Favoritos("Addi","Azul","Blanco","Negro")
    Colores_Favoritos("Rosa","Blanco")
    Cadena = "Hola"
    Tupla = "Hola",
    Res = Sumar(5, 3, 4)


print(Cadena)
print(Tupla)
print(f"{Res}")