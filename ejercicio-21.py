productos = ['Leche', 'Yogurth', 'Lechuga', 'Arroz', 'Galletas', 'Salchichas', 'Carne', 'Pollo']

for producto in productos:
    print(f"Producto: {producto}")
    vencido = input('Esta vencido?: ').lower()
    if vencido == 'si':
        print(f"Alerta! Debes retirar el producto: {producto}")
        break
else:
    print('Todo en orden!')