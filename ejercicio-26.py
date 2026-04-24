pedidos = ["pocion_vida", "pocion_mana", "pocion_fuerza", "pocion_invisible"]
inventario = {
    "vida": 3,
    "mana": 2,
    "fuerza": 0,
    "invisible": 2,
}
print(f"Que pocion quieres comprar?")
opcion_pocion = input(f"Esta es la lista de pociones: {pedidos}")

match opcion_pocion:
    case "pocion_vida":
        inventario["vida"] -= 1
    case "pocion_mana":
        inventario["mana"] -= 1
    case "pocion_fuerza":
        inventario["fuerza"] -= 1
    case "pocion_invisible":
        inventario["invisible"] -= 1
    case _:
        print("Esa opcion no es valida!")
print(f"Asi quedo el stock: {inventario}")