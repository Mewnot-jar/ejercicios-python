for i in range(3):
    print(f"Bomba Nro: {i+1}")
    respuesta = input("Desea cargar combustible?: ").lower()
    if respuesta == "si":
        monto = int(input("Ingresa el monto a cargar: "))
        while monto <= 0:
            monto = input("Error, ingrese un monto valido: ")
        print(f"Bomba {i+1} cargada con ${monto}")
    else:
        continue
