archivos = ["A", "B", "C", "X", "E", "F"]

for archivo in archivos:
    print(f"Procesando archivo {archivo}...")
    if archivo == "X":
        print("Peligro, virus encontrado")
        print("Deteniendo el sistema...")
        break
    print("OK!")
