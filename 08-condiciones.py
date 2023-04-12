balance = 500
if balance > 0:
    print('Puedes Pagar')
else:
    print('No tienes saldo')

#If de igualacion pero con negación
lenguaje = 'PHP'
if not lenguaje =='Python':
    print('Excelente decisión')

#Evaluar un booleano
usuario_autenticado = True

if usuario_autenticado:
    print('Acesso al sistema')
else:
    print('Debes iniciar sesión')

#Evaluar un elemento de una lista
lenguajes=['Python','Kotlin','Java','Php']

if 'Kotlin' in lenguajes:
    print('Si está en la lista')
else:
    print('No está en la lista')

#if anidados
usuario_autenticado=True
usuario_admin=False

if usuario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciasr sesión')


