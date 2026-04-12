fruta = input("Ingrese una fruta: ").lower()

match fruta:
    case "manzana":
        print("Rojo o verde")
    case "platano":
        print("Amarillo")
    case "uva":
        print("")
    case _:
        print("color desconocido")
