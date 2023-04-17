#Iniciar un diccionario vacio
jugador={}
print(jugador)

#Se une un jugador
jugador["nombre"]="Rodrigo"
jugador["puntaje"]=0
print(jugador)

#Incrementa el puntaje
jugador["puntaje"]=100
print(jugador)

#Acceder a un valor
print(jugador.get("lolaila", "No existe claro ese valor"))

#Iterar en el diccionario
for llave, valor in jugador.items():
    print(llave)
    print(valor)

#Eliminar jugador y puntaje
del jugador["nombre"]
del jugador["puntaje"]
print(jugador)