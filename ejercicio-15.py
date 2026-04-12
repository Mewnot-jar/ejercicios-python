energia = 0
while energia < 100:
    energia_ingresada = int(input("Ingresa la cantidad de energia que vas a agregar: "))
    if energia_ingresada >= 0:
        energia += energia_ingresada
    else:
        print("No puedes quitar energia!")
print("Felicidades llegaste a 100 de energia - Despegando...")
