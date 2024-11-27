'''
Jennifer Marlene Gutierrez Beteta
24 de noviembre de 2024.
Descripción:
Ejercicio 1 Tuplas.
Este programa permite obtener la ecuacion de la recta.
.
'''

'''
Escribe un programa de nombre ej3_rol_de_juegos.py que realice lo siguiente:
Este programa almacena 8 jornadas en 2 equipos, los cuales compiten entre sí.
a) Se requiere realizar 7 grupos diferentes en donde las jornadas compiten sin repetir el enfrentamiento.

b) El movimiento de las jornadas será al contrario de las manecillas del reloj.

c) La jornada 1 no se moverá en ningún caso.
'''

# Declaración de equipos de las jornadas.
Equipo_1 = ["Jornada 1", "Jornada 2", "Jornada 3", "Jornada 4"]
Equipo_2 = ["Jornada 5", "Jornada 6", "Jornada 7", "Jornada 8"]

Auxiliar = None
Grupos = 1
# Mostrar los grupos de jornadas.
while Grupos <= 7:
    Cont = 0
    print(f"Grupo {Grupos}:")
    # Mostrar los enfrentamientos del grupo actual.
    while Cont < 4:
        print(Equipo_1[Cont], end=" ")
        print(Equipo_2[Cont])
        Cont += 1

    Grupos += 1

