'''
Jennifer Marlene Gutierrez Beteta
12 de noviembre de 2024.
Descripción:
.
'''

print("*** Videos de You Tube  ***")
videos_yt = []


opcion = 1
while opcion != 0:
    
    print()
    print("[0].- Salir")
    print("[1].- Ver listas de videos por añadido")
    print("[2].- Ver listas de videos por orden A-Z")
    print("[3].- Ver listas de videos por orden Z-A")
    print("[4].- Añadir videos")
    print("[5].- Añadir varios videos")
    print("[6].- Eliminar videos")
    print()
    opcion = int(input("Ingresa una opción: "))
    if opcion  == 1:
        numero = 1
        for video_yt in videos_yt:
            print(f"{numero}._ {video_yt}")
            numero += 1
    elif opcion  == 2:
        videos_yt.sort()
        for video_yt in videos_yt:
            print(video_yt, end=",")
            print()
    elif opcion  == 3:
        print()
        videos_yt.sort(reverse = True)
        for video_yt in videos_yt:
            print(video_yt, end=",")
            print()
    elif opcion  == 4:
        print()
        video = input("Ingrese el nombre del video: ")
        videos_yt.append(video)
        print()
    elif opcion  == 5:
        print()
        anadir = int(input("Cantidad de  videos que desea añadir: "))
        contador = 1
        while contador <= anadir:
            video = input("Ingrese el nombre del video video:")
            videos_yt.append(video)
            contador += 1
        print()
    elif opcion  == 6:
        eliminar_video = input("Ingrese el video que desea eliminar: ")
        videos_yt.remove(eliminar_video)
    else:
        print()
        print("Opción incorrecta")
        print()
print()
print("Saliendo del programa...")



