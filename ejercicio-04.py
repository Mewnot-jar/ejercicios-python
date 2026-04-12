cant_notas = int(input("Ingresa cantidad de notas: "))
notas = []
porc= []
promedio = 0
for i in range(cant_notas):
    notas.append(float(input(f"Ingrese la nota {i+1}: ")))
    porc.append(float(input("Ingrese el porcentaje de la nota: ")))
    promedio += notas[i] * (porc[i]*0.01)

print(round(promedio, 2))

    