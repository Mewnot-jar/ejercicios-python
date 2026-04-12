nota = float(input("Ingrese una nota entre un 1.0 y un 7.0: "))
while nota < 1.0 or nota > 7.0:
    print("Ingresa una nota valida")
    nota = float(input("Ingresa una nota entre un 1.0 y un 7.0: "))
print("Nota agregada exitosamente")