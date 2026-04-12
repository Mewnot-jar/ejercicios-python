saldo = 5000

while True:
    print("1. Ver saldo")
    print("2. Salir")
    opcion = input("Ingrese una opcion del menu: ")
    if opcion == "1":
        print(f"Tu saldo es: {saldo}")
    elif opcion == "2":
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion no valida")