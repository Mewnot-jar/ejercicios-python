vida_maxima = 1000
vida_actual = int(input("Tu vida maxima es 1000, cuanta vida te queda?: "))
vida_faltante = 1000 - vida_actual
pociones = (50, 20, 10)


for pocion in pociones:
    cantidad = vida_faltante // pocion
    if cantidad > 0:
        print(f"Necesitas {cantidad} pociones de {pocion}")
    vida_faltante %= pocion



