almacen = []

cantidad_productos = int(input("Cuantos productos quieres agregar?: "))
while cantidad_productos <= 0:
    print("Cantidad incorrecta. Intentalo de nuevo")
    cantidad_productos = int(input("Cuantos productos quieres agregar?: "))
for i in range(cantidad_productos):
    producto = input(f"Agregando producto Nro {i+1}: ").capitalize()
    almacen.append(producto)

print(f"Agregaste {len(almacen)} productos.")
print(f"Tu carrito: {almacen}")

respuesta = input("Quieres eliminar algo de tu lista?: ").lower()
while respuesta == "si":
    print(f"Tu carrito: {almacen}")
    producto_eliminado = input("Escribe el producto que quieras eliminar: ").capitalize()
    if producto_eliminado in almacen:
        almacen.remove(producto_eliminado)
    else:
        print("Ese producto no esta en tu carrito.")
    print(f"Tu carrito: {almacen}")
    respuesta = input("Quieres eliminar algo de tu lista?: ").lower()

print("Esta es tu compra!")
print(almacen)
