long_1 = float(input("Ingresa la primera longitud: "))
long_2 = float(input("Ingresa la segunda longitud: "))
long_3 = float(input("Ingresa la tercera longitud: "))

if long_1 == long_2 and long_1 == long_3:
    print("Equilatero")
elif long_1 == long_2 or long_2 == long_3 or long_1 == long_3:
    print("Isosceles")
else:
    print("Escaleno")
