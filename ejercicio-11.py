opcion = ""
while opcion != "3":
    print("---MENU DE OPCIONES---")
    print("1. Saludar")
    print("2. Ver hora")
    print("3. Salir")
    opcion = input("Ingrese su opcion: ")
    match opcion:
        case "1":
            print("Hola")
        case "2":
            print("Son las 10:00 AM")
        case "3":
            print("Saliendo del programa...")
        case _:
            print("Opcion invalida")