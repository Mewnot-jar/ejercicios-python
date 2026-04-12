palabra = input("Ingresa la palabra que quieres analizar: ").lower()
letra_user = input("Ingresa la letra que quieres encontrar: ").lower()
encontrada = False
for letra in palabra:
    if letra == letra_user:
        encontrada = True
        break


if encontrada:
    print(f"Letra encontrada!, la letra '{letra_user.capitalize()}' se encuentra en la palabra {palabra.capitalize()}")
else:
    print("Letra no encontrada...")