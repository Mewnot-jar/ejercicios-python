billetes = [50000, 20000, 10000, 5000, 2000, 1000]
monto = int(input("Ingresa un monto: "))
resultado = {}

for billete in billetes:
    if monto >= billete:
        resultado[billete] = monto // billete
        monto = monto % billete
print(resultado)