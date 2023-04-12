nombre=input('Escribe tu nombre')
puesto=input('Escribe tu puesto')
def informacion(nombre,puesto):
    print(f'Soy {nombre} y soy {puesto}')
informacion('Susana','Programadora')
informacion('Virginia','Ama de casa')
informacion('Rodrigo','Pintor')

#Este ejemplo de arriba está completo , pero el de abajo le quité el Argumento Pintor y así tiene que quedar:

def informacion(nombre,puesto='Pintor'):
    print(f'Soy {nombre} y soy {puesto}')
informacion(nombre,puesto)
#informacion('Virginia','Ama de casa')
#informacion('Rodrigo')
#pero si le pasas algo al lado de Rodrigo, cojerá lo que está al lado y lo otro lo obviará