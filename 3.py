tarifas = [(5, 1000), (10, 800), (20, 500)]
peso_total = 12
precio_total = 0
for limite, precio in tarifas:
    if peso_total > 0:
        if peso_total >= limite:
            precio_total += limite * precio
            peso_total -= limite
        else:
            precio_total += peso_total * precio
            peso_total = 0
        print(f"Tramo hasta {limite}kg = {precio_total}")
print(f"Debe pagar: ${precio_total}")