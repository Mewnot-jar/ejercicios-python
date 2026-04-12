nombre_producto = input("Nombre del producto: ")
cantidad_producto = int(input("Cantidad del producto: "))
precio_producto = float(input("Valor unitario del producto: "))

precio_neto = cantidad_producto * precio_producto
precio_iva_inc = precio_neto * 1.21
iva = precio_iva_inc - precio_neto

print(f"El valor total SIN IVA incluido: {precio_neto} ")
print(f"El valor total CON IVA incluido: {precio_iva_inc} ")
print(f"Estas pagando {iva} de IVA")