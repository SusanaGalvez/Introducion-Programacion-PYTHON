lenguajes=['Python','Kotlin','Java','Php']
print(lenguajes)
print(lenguajes[0])

#Ordenar los elementos
lenguajes.sort()
print(lenguajes)

#Acceder a un elemento dentro de un texto
aprendiendo= f'Estoy aprendiendo {lenguajes[2]}'
print(aprendiendo)


#Modficando el valor de un arreglo
lenguajes[2]= 'PHP'
print(lenguajes)

#Agregar elemento a un arreglo
lenguajes.append('Ruby')
print(lenguajes)

#Eliminando el último elemento
lenguajes.pop()
print(lenguajes)

#Eliminando con pop una posicion en específico
lenguajes.pop(0)
print(lenguajes)

#Elimiar por nombre
lenguajes.remove('Php')
print(lenguajes)

#Eliminar de un Arreglo
del lenguajes[1]
print(lenguajes)