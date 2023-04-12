import os


CARPETA = 'contactos/'  # Esta en mayúscula por que es una constante
EXTENSION = '.txt'  # Extensión del archivo


class Contacto:
    def _init_(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def app():
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
            print('Intente de nuevo')


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


def agregar_contacto():
    print('Escriba los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del Nuevo Contacto:\r\n')

    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(
        nombre_contacto)  # en el video pone dentro de los parentesis nombre_anterior,pero me lo pone en rojo

    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            # Resto de los campos
            telefono_contacto = input('Agrega el Telefono:\r\n')
            categoria_contacto = input('Categoría Contacto:\r\n')

            # Intanciamos la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el Archivo
            archivo.write('Nombre: ' + contacto.nombre + "\r\n")
            archivo.write('Telefono: ' + contacto.telefono + "\r\n")
            archivo.write('Categoria: ' + contacto.categoria + "\r\n")

            # Mostrar un mensaje exitoso
            print('\r\n Contacto creado correctamente \r\n')

    else:
        print('Ese contacto ya existe')

    # Para que vuelva a salir las preguntas
    # app()


def editar_contacto():
    print('Escribe el nombre a editar:')
    nombre_anterior = input('Nombre del contacto que desea editar \r\n')

    # Revisamos si el archivo ya existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        # print('Puedes editarlo')
        with open(CARPETA + nombre_anterior + EXTENSION,
                  'w') as archivo:  # en vez de nombre_anterior , ponía nombre contacto
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
            print('\r\nContacto editado correctamente\r\n')

    else:
        print('Ese contacto no existe')
    # Reiniciar la aplicación
    app()


def eliminar_contacto(expression=None):
    nombre = input('Seleccione el Contacto a eliminar:\r\n')
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\nEliminado Correctamente')
    except Exception as ex:
        print(ex)
        print('No existe ese contacto')
    # Reinicio la App
    app()


def mostrar_menu():
    print('Seleccione del Menú lo que desea hacer:')
    print('1)Agregar nuevo contacto')
    print('2)Editar contacto')
    print('3)Ver contacto')
    print('4)Buscar contacto')
    print('5)Eliminar contacto')


def buscar_contacto():
    nombre = input('Selecciones el contacto a buscar')

    try:

        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Información del Contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)
    # Reiniciar la app
    app()


def crear_directorio():
    if not os.path.exists('contactos/'):
        # crear la carpeta
        os.makedirs('contactos/')


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)


app()
