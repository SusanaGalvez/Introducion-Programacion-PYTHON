class Restaurant:
    def agregar_restaurante(self,nombre):
        self.nombre= nombre
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre }")

#Intanciamos una clase
restaurant= Restaurant()
restaurant.agregar_restaurante("Pizzeria Metro")
restaurant.mostrar_informacion()

#Yo puedo instanciar todas las clases que quiera
restaurant2= Restaurant()
restaurant2.agregar_restaurante("Pizzeria Papa luigi")
restaurant2.mostrar_informacion()
