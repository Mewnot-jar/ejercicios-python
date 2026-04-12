horas = int(input("Ingresa cuantas horas estuviste en el estacionamiento: "))

if horas <= 0:
    print("Error: Horas no validas")
else:
    vehiculo = (input("Tipo de vehiculo (Moto - Auto - Camion): ")).capitalize()
    match vehiculo:
        case "Moto":
            valor_vehiculo = 2
        case "Auto":
            valor_vehiculo = 5
        case "Camion":
            valor_vehiculo = 10
        case _:
            valor_vehiculo = 0

    if valor_vehiculo != 0:
        if horas >= 8:
            precio = (horas * valor_vehiculo) - ((horas * valor_vehiculo) * 0.10) 
            print(f"Tienes el 10% de descuento! - Tu {vehiculo} debe pagar: ${precio}")
        else:
            precio = horas * valor_vehiculo
            print(f"Tu {vehiculo} debe pagar: ${precio}")
    else:
        print("Vehiculo no encontrado")