import os


CARPETA = 'contactos/'  # Esta en mayúscula por que es una constante
EXTENSION = '.txt'  # Extensión del archivo


class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def app():
    #Muestra el directorio
    crear_directorio()

    # Muestra el menú de opciones
    mostrar_menu()

    # Pregunat al usuario la acción a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        # Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            # print('Ver contacto')
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            # print('Eliminar contacto')
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no válida, intentelo de nuevo')
def crear_directorio():
    if not os.path.exists('contactos/'):
        # crear la carpeta
        os.makedirs('contactos/')

def mostrar_menu():
    print('Seleccione del Menú lo que desea hacer:')
    print('1)Agregar nuevo contacto')
    print('2)Editar contacto')
    print('3)Mostrar contacto/s')
    print('4)Buscar contacto')
    print('5)Eliminar contacto')

def agregar_contacto():
    print('Escriba los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del Nuevo Contacto:\r\n')

    # Revisar si el archivo ya existe antes de crearlo, y existe_contacto()es una funcion que hemos hecho para utilizarla aquí y en modificar contacto

    existe = existe_contacto(nombre_contacto + EXTENSION)
    # en el video pone dentro de los parentesis nombre_anterior,pero me lo pone en rojo
    if not existe:
        # la W es permiso de escritura
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            # Resto de los campos
            telefono_contacto = input('Agrega el Telefono:\r\n')
            categoria_contacto = input('Categoría Contacto:\r\n')

            # Instanciamos la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el Archivo
            archivo.write('Nombre: ' + contacto.nombre + "\r\n")
            archivo.write('Telefono: ' + contacto.telefono + "\r\n")
            archivo.write('Categoria: ' + contacto.categoria + "\r\n")

            # Mostrar un mensaje exitoso
            print('\r\n CONTACTO CREADO CORRECTAMENTE \r\n')

    else:
        print('Ese contacto ya existe')

    # Para que vuelva a salir las preguntas
    app()

def editar_contacto():
    print('Escribe el nombre del contacto a editar:')
    nombre_anterior = input('Nombre del contacto que desea editar \r\n')
    # Revisamos si el archivo ya existe antes de editarlo, existe_contacto() es una función que hemos creado anteriormente
    existe = existe_contacto(nombre_anterior)

    if existe:
        # print('Puedes editarlo')
        # Tenemos que abrir el archivo, reescribirlo y guardarlo
        with open(CARPETA + nombre_anterior + EXTENSION,'w') as archivo:
            # en vez de nombre_anterior , ponía nombre contacto
            nombre_contacto = input('Agrega el nuevo Nombre:\r\n')
            telefono_contacto = input('Agrega el nuevo Telefono:\r\n')
            categoria_contacto = input('Agrega la nueva Categoria:\r\n')

            # Instanciamos
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribimos en el archivo
            archivo.write('Nombre: ' + contacto.nombre + "\r\n")
            archivo.write('Telefono: ' + contacto.telefono + "\r\n")
            archivo.write('Categoria: ' + contacto.categoria + "\r\n")

        # Renombramos el Archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
        # Mostrar mensaje de Éxito
        print('\r\nCONTACTO EDITADO CORRECTAMENTE\r\n')

    else:
        print('ESE CONTACTO NO EXISTE')
    # Reiniciar la aplicación
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                # imprime los contenidos
                print(linea.rstrip())
            # Imprime un separador entre contactos
            print('\r\n')
    app()
def buscar_contacto():
    nombre = input('Selecciona el contacto a buscar: \r\n')
    try:

        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n INFORMACIÓN DEL CONTACTO: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print("EL CONTACTO NO EXISTE")
        print(IOError)
    # Reiniciar la app
    app()

def eliminar_contacto(expression=None):
    nombre = input('Seleccione el Contacto a eliminar:\r\n')
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\n CONTACTO ELIMINADO CORRECTAMENTE')
    except Exception as ex:
        print(ex)
        print('No existe ese contacto')
# Reinicio la App
    app()


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)
app()
