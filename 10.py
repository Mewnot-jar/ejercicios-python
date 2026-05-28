registro_ventas = [("One Piece", 20), ("Berserk", 5), ("Naruto", 15), ("One Piece", 12), ("Berserk", 3), ("Bleach", 8)]
ventas_totales = {}
for manga, ventas in registro_ventas:
    if not manga in ventas_totales:
        ventas_totales[manga] = ventas
    else:
        ventas_totales[manga] +=  ventas
print(ventas_totales)


