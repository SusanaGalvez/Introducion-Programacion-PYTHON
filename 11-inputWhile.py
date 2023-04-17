pregunta="Agrega un número y te diré si es par o no\r\n"
pregunta+= "(Escribe 'cerrar' para sair de la aplicación)\r\n"


preguntar = True

while preguntar:
    numero= input(pregunta)
    if numero == 'cerrar' or 'Cerrar':
        preguntar = False
    else:
        numero = int(numero)
        if numero % 2 == 0:
            print(f"El {numero} es Par")
        else:
            print(f"El {numero} es Impar")
