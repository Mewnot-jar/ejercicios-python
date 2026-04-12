estudiantes = [
    {"nombre": "Carlos", "nota": 3.5},
    {"nombre": "Maria", "nota": 6.2},
    {"nombre": "Jose", "nota": 4.0},
    {"nombre": "Ana", "nota": 2.8},
]
for estudiante in estudiantes:
    if estudiante["nota"] >= 4.0:
        print(f"Estudiante {estudiante["nombre"]}: Aprobado")
    elif estudiante["nota"] < 4.0:
        print(f"Estudiante {estudiante["nombre"]}: Reprobado")
print(f"Se evaluaron {len(estudiantes)} estudiantes")