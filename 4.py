jugada = [("ficha", 50), ("ficha", 20), ("trampa", 100), ("ficha", 40), ("multiplicador", 3)]
puntaje_total = 0


for carta, valor in jugada:
    match carta:
            case "ficha":
                puntaje_total += valor
            case "trampa":
                puntaje_total -= valor
            case "multiplicador":
                puntaje_total *= valor
    if puntaje_total < 0:
        puntaje_total = 0    
    print(f"Carta: {carta} - Valor: {valor} = {puntaje_total}")
print(f"El puntaje total del combo es: {puntaje_total}")