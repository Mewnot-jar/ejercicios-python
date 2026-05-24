inventario = [
    {"producto": "Teclado Mecánico", "stock": 15, "precio": 50},
    {"producto": "Mouse Gamer", "stock": 0, "precio": 25},
    {"producto": "Monitor 4K", "stock": 8, "precio": 300},
    {"producto": "Cables HDMI", "stock": 2, "precio": 10},
    {"producto": "Auriculares", "stock": 0, "precio": 45}
]
agotados = 0

for producto in inventario:
    if producto['stock'] > 0:
        print(f"El producto {producto['producto']} tiene unidades disponibles.")
    else:
        print(f"El producto {producto['producto']} no tiene unidades disponibles.")
        agotados +=1
print(f"En el inventario tienes {len(inventario)} tipos de productos.")
print(f"En el inventario tienes {agotados} productos agotados.")