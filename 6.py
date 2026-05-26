equipo = [("Gengar", 110, False), ("Venusaur", 80, True), ("Exeggutor", 55, True), ("Snorlax", 30, False)]
orden_de_turno = []
for pokemon, velocidad, habilidad in equipo:
    if habilidad:
        orden_de_turno.append((pokemon, velocidad * 2))
    else:
        orden_de_turno.append((pokemon, velocidad))

print(orden_de_turno)