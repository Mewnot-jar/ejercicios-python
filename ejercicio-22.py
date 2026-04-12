mayor_edad = False
while not mayor_edad:
    edad_usuario = int(input("Ingresa tu edad: "))
    if edad_usuario < 18:
        print("Acceso denegado. Debes ser mayor de edad, vuelve a intentarlo!")
    else:
        mayor_edad = True


print("Bienvenido al sistema!")