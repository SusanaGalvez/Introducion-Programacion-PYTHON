class Restaurant:

    def __init__(self,nombre,categoria,precio):
        self.nombre = nombre#Atributos
        self.categoria=categoria
        #Con un solo _ está PROTEGIDO.., pero se puede cambiar aún y con 2 __ está de forma PRIVADA, daría error
        self.__precio=precio


    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre }, Categoría: {self.categoria}, Precio: {self.__precio}")


    #GETTERS Y SETTERS, GET OBTIENE UN VALOR Y SET AGREGA UN VALOR
    #Hacemos una nueva función llamada get_precio()

    def get_precio(self):
        #print(self.__precio)
        #Normalmente se pone lo de abajo
        return self.__precio

    def set_precio(self,precio):
        self.__precio= precio

#Intanciamos la primera Clase
restaurant= Restaurant("Pizzeria Acapulco","Comida Italiana",50)
#En este print me sale 50
#print(restaurant.__precio)#No me deja, me da error, por que yo lo he puesto PRIVADO
#Aqui le cambio el precio y se llama ENCAPSULAMIENTO
#restaurant.__precio= 500

#Aquí le cambio el precio ya estando privado, mediente la funcion def get_precio()
restaurant.mostrar_informacion()
restaurant.set_precio(200)
precio = restaurant.get_precio()
print(precio)



#Yo puedo instanciar todas las clases que quiera
restaurant2= Restaurant("Pizzeria Méjico","Comida Picante",20)
restaurant2.mostrar_informacion()