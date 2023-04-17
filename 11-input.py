nombre = input("Cual es tu nombre? \r\n")

print(f"Hola {nombre}")

#Leer datos que serán números
edad = input("Cual es tu edad?\r\n")
#Convertimos edad a entero, por que las entradas de datos en python siempre vienen como string
edad = int(edad)
if edad >= 18:
    print("Ya puedes votar")
else:
    print("Aún no puedes votar")

#Mezclarlo con operadores
numero= input("Agrega un número y te diré si es par o no\r\n")
numero = int(numero)
if numero % 2 ==0:
    print(f"El {numero} es Par")
else:
    print(f"El {numero} es Impar")
