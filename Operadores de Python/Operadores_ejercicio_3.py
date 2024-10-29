'''
Jennifer Marlene Gutierrez Beteta
15 de octubre de 2024
Descripción:
Ejercicio 3.
Este programa determinará si un usuario se autentifica correctamente con su usuario y contraseña.
'''

#Declarar las variables de usuario y contraseña-
USUARIO_1= "alumno"
CONTRASEÑA_1 = "tercero"

print("*** Sistema de auteuntificación ***")
print(" ")
usuario = input("Ingresa tu usuario:")            #Pedir usuario.
contraseña = input("Ingresa tu contraseña:")    #Pedir contraseña.


print(f"¿El acceso es correcto? {usuario == USUARIO_1 and contraseña == CONTRASEÑA_1}")     #Hacer la comparación si el usuario y la contraseña son iguales.

