def app():
    archivo = open('archivo.txt','w')
    #Generamos los numeros en el archivo

    for i in range(0, 20):
        archivo.write('Esta es la línea' + str(i) + "\r\n")

    archivo.close()

app()
