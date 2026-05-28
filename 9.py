lecturas_boya = [(18.5, True), (19.1, True), (15.0, False), (18.8, True), (99.9, False)]
lecturas_validas = []
for lectura, conexion in lecturas_boya:
    if conexion:
        lecturas_validas.append(lectura)
promedio_lecturas =  sum(lecturas_validas) / len(lecturas_validas)
print(promedio_lecturas)