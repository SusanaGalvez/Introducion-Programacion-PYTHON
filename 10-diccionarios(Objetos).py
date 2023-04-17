#Creando un diccionaria simple

cancion={
    "artista":"Camela",
    "cancion":"Hablale de mí",
    "lanzamiento":1990,
    "likes":3000
}
#Acceder a los elemntos del diccionario
print(cancion["artista"])

#Mezclar con un String, lo primero es pasar la información a una variable
artista= cancion["artista"]
print(f"Estoy escuchando a {artista}")


#Agregar más valores
cancion["playlist"]="Rumba Flamenca"
print(cancion)

#Reemplazar valor existente
cancion["cancion"]="Rumba Flamenca"
print(cancion)

#Borrar valor
del cancion["lanzamiento"]
print(cancion)
