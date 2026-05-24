paquetes = [150, 148, 155, 30, 152, 149, 45, 151]
clave_user = input("Ingresa tu clave: ")
desc_contador = 0

while clave_user != "1234":
    clave_user = input("Clave incorrecta. Intentalo de nuevo. Ingresa tu clave: ")
for i in range(len(paquetes)):
    if paquetes[i] < 100:
        print(f"Paquete de {paquetes[i]}g descartado.")
        desc_contador += 1
    else:
        print(f"Paquete de {paquetes[i]}g aprobado.")
print(f"Se revisaron {len(paquetes)} paquetes.")
print(f"{desc_contador} paquetes fueron descartados.")