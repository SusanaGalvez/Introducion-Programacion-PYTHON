class Restaurant:

    def __init__(self,nombre,categoría,precio):
        self.nombre = nombre#Atributos
        self.categoria=categoría
        self.precio=precio


    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre }, Categoría: {self.categoria}, Precio: {self.precio}")

#Intanciamos una clase
restaurant= Restaurant("Pizzeria Acapulco","Comida Italiana",50)
#En este print me sale 50
print(restaurant.precio)
#Aqui le cambio el precio y se llama ENCAPSULAMIENTO
restaurant.precio=100
restaurant.mostrar_informacion()

#Yo puedo instanciar todas las clases que quiera
restaurant2= Restaurant("Pizzeria Méjico","Comida Picante",20)
restaurant2.mostrar_informacion()