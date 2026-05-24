inventario = {
    'laptops': 5,
    'ratones': 15,
    'teclados': 10,
    'monitores': 3
}
operaciones = {
    'inventario_final':{},
    'pedidos_aprobados': [],
    'pedidos_rechazados': [],
}

ordenes = [
    {
        'cliente': 'Ana', 
        'articulos': [('laptops', 2), ('ratones', 2)]
    },
    {
        'cliente': 'Juan', 
        'articulos': [('monitores', 4), ('teclados', 1)]
    }, 
    {
        'cliente': 'Pedro', 
        'articulos': [('laptops', 1), ('ratones', 10), ('teclados', 5)]
    },
    {
        'cliente': 'Laura', 
        'articulos': [('monitores', 2), ('teclados', 2)]
    }
]
print(inventario)
for orden in ordenes:
    estado = "Aprobado"
    for producto, cantidad in orden['articulos']:
        if cantidad <= inventario[producto]:
            estado = "Aprobado"
        else:
            estado = "Rechazado"
            operaciones['pedidos_rechazados'].append(orden['cliente'])
            break
    if estado == "Aprobado":
        operaciones['pedidos_aprobados'].append(orden['cliente'])
        for producto, cantidad in orden['articulos']:
            operaciones['inventario_final'][producto] = inventario[producto] - cantidad
            print(operaciones['inventario_final'][producto])

print(operaciones)
            
            