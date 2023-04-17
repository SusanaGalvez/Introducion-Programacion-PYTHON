usuario_logueado = True
usuario_admin = False
#El and Revisa que se cumpla todas las condiciones y el or , al menos una de ellas
if usuario_logueado and usuario_admin:
    print("Administrador")
elif usuario_logueado:
    print("Acceso al sistema")
else:
    print("Debes iniciar sesión")
