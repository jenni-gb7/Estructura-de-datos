'''
Jennifer Marlene Gutierrez Beteta
02 de diciembre de 2024.
Descripción:
Diccionario.
'''

# Los diccionarios son ordenados.

print("*** Ejemplo de uso ***")

# Para crear el diccionario se usan las llaves.
diccionario_profesor = {'nombre':"Alberto",
'primer apellido': "Martinez",
'edad':"31",
'correo':"albeto2@gmail.com"}
print(diccionario_profesor)
print("------------------------------------------------------")
# En los diccionarios se acceden por medio de una llave que seria la palabra clave para acceder.

Diccionario_jenni={}
Diccionario_jenni['Nombre']="Jenni"
Diccionario_jenni['Primer_apellido']="Gutiérrez"
Diccionario_jenni['Segundo apellido']="Beteta"
Diccionario_jenni['Grupo']="303"
Diccionario_jenni['Materia favorita']="Gutiérrez"
print(Diccionario_jenni)
print("------------------------------------------------------")
# Se accede de las 2 maneras.
Nombre_alumno = Diccionario_jenni.get('Nombre')
Apellido_alumno = Diccionario_jenni['Primer_apellido']
print(Nombre_alumno)
print(Apellido_alumno)
# Para acceder solo tienes que ingresar con la palabra clave.
print(Diccionario_jenni['Primer_apellido'])
print("------------------------------------------------------")
Diccionario_jenni['Nombre']="Mar"
Diccionario_jenni['Grupo']="303"
print(Diccionario_jenni)
print("------------------------------------------------------")
# Para eliminar.
del Diccionario_jenni['Segundo apellido']
print(Diccionario_jenni)
Diccionario_jenni.pop("Grupo")
print(Diccionario_jenni)
print("------------------------------------------------------")
# Imprime las palabras claves.
for clave in Diccionario_jenni.keys():
    print(f"clave:{clave}")
print("------------------------------------------------------")

# Combinación con tuplas.
Diccionario_egresado = {'Nombre': "J",'Primer apellido':"Ruiz","Segundo apellido":"Perez","Edad":"25"}
print(Diccionario_egresado)
print("------------------------------------------------------")
Diccionario_informatica = {
'Grupo_303':{'Num_alumnos':12,
    'Num_materias':5,
    'Promedio_gripal':7.9},
'Grupo_503':7.5,
'Grupo_703':7.5,
'Grupo_903':7.5,}
print(Diccionario_informatica )

print("------------------------------------------------------")
for Grupo in enumerate(Diccionario_informatica):
    print(f"Grupo: {Grupo}")
# Accede a los elementos.
prom_303= Diccionario_informatica['Grupo_303']
print(prom_303 )
