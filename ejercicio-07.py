clima = input("Como esta el clima?: ").capitalize()

match clima:
    case "Soleado":
        print("Recuerda usar protector solar y lentes de sol! :D")
    case "Lluvioso":
        print("Saca tu paraguas! D:")
    case "Nevado":
        print("Mejor no salgas, te vas a congelar xd")
    case "Nublado":
        print("Esta piola, pero no te confies, puede salir el sol!")
    case _:
        print("No se brother, estas en otro planeta?")