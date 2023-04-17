#Función principal
playlist = {}
playlist["canciones"]=[]#Lista vacia
def app():
    #Agregar playlist
    agregar_playlist= True
    while agregar_playlist:
        nombre_playlist= input("¿Qué nombre quieres ponerle a la Playlist?\r\n")
        if nombre_playlist:
            playlist["nombre"]=nombre_playlist
            #Ya tenemos un nombre, desactivamos el true
            agregar_canciones()


def agregar_canciones():
    #Bandera para agregar canciones
    agregar_cancion= True

    while agregar_cancion:
        #Preguntar al usuario que canción agregar
        nombre_playlist =playlist["nombre"]
        pregunta=f"Agrega canciones para la playlist {nombre_playlist}:\r\n"
        pregunta+= "(Escribe Salir para dejar de agregar canciones)\r\n"

        cancion= input(pregunta)
        if cancion == "Salir":
            #Dejar de agregar canciones
            agregar_cancion=False

            #Mostramos el resumen de las canciones
            mostrar_resumen()
        else:
            playlist["canciones"].append(cancion)
            #Para que se vaya viendo las canciones
            print(playlist)

def mostrar_resumen():
    nombre_playlist = playlist["nombre"]
    print(f"Playlist: {nombre_playlist}\r\n")
    print("Canciones: \r\n")
    for cancion in playlist["canciones"]:
        print(cancion)
app()
