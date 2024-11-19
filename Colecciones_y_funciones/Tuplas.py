'''
Jennifer Marlene Gutierrez Beteta
19 de noviembre de 2024.
Descripción:
Ejericio Tuplas .
'''
'''
Los elementos se caracterizan entre parentesís y es ordenado e inmutable'''
print()
print("*** Fechas de cumpleaños ***")
print()
Fechas_cumpleaños = ('12-19','12-27','10-18','11-01','09-30','08-25','01-06','10-21','04-11','03-06')
print("Fechas de cumpleaños:", Fechas_cumpleaños)
for Fecha in Fechas_cumpleaños:
    print(Fecha,end =", ")
print()
# Serie de pi de leibniz.
print()
print("*** Serie de pi de leibniz ***")
print()
pi_serie = (4, -4/3, 4/5, -4/7, 4/9, -4/11, 4/13, -4/15, 4/17, -4/19, 4/21, -4/23)
print(pi_serie, end=", ")
print()
print(f"Valor de pi considerando 3 elementos: {sum(pi_serie[0:2])}")
print(f"Valor de pi considerando 5 elementos: {sum(pi_serie[0:4])}")
print(f"Valor de pi considerando 8 elementos: {sum(pi_serie[0:7])}")
print(f"Valor de pi considerando 10 elementos: {sum(pi_serie[0:9])}")
print(f"Valor de pi considerando todos los  elementos: {sum(pi_serie)}")

# Coordenadas.
print()
print("*** Coordenadas ***")
print()
Punto_1 = (1,0)
Punto_2 = (5,3)

print(f"Coordenadas en tuplas: {Punto_1}, {Punto_2}")

#Desempaquetado de tuplas.
# Con asignación múltiple.

# Obtener una ecuación de la recta.
# Ecuación de la recta: y= mx + b.
x1,y1 = Punto_1
x2,y2 = Punto_2

# Pendiente de la recta (m).
# Formúla m= (y2-y1)/(x2-x1)
m = (y2-y1)/(x2-x1)
print("m=",m)

# Ordenada al origen (b).
# Formúla b=y1-mx1
b= y1-m*x1
print("b=",b)


y = m*x1+b
print(f"Ecuación de la recta: {m} x {b}")