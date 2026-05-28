salud_jefe = 100
mana_jugador = 40

while salud_jefe > 0 and mana_jugador > 0:
    salud_jefe -= 30
    mana_jugador -= 15
    print(f"Atacas al jefe, tu mana es {mana_jugador} y el jefe tiene {salud_jefe} de vida.")

if salud_jefe < 0:
    print("Derrotaste al jefe!")
else:
    print(f"La vida del jefe es: {salud_jefe} y te quedaste sin mana, huyes.")