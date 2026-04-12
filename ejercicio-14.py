total_galletas = 0
total_paquetes = 0
meta = 3

while total_paquetes < meta:
    while total_galletas < 4:
        total_galletas +=1
        print(f"Galleta horneada - Llevas {total_galletas}")
        if total_galletas % 4 == 0:
            total_paquetes +=1
            print(f"Paquete listo - Llevas {total_paquetes}")
print("Produccion terminada")
print(f"Hiciste {total_paquetes} paquetes y {total_galletas} galletas")








