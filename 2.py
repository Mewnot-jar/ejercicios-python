billetes = (20000, 10000, 5000, 2000, 1000)
monto = int(input("Monto a retirar: "))

for billete in billetes:
    cantidad = monto // billete
    if cantidad > 0:
        print(f"Necesitas {cantidad} billete de {billete}")
    monto %= billete