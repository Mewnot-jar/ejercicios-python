cola_tareas = [
    ("crear", "Base de datos"), 
    ("actualizar", "Servidor Web"), 
    ("eliminar", "Archivos temporales"), 
    ("magia", "Hacer algo raro")
]
while len(cola_tareas) > 0:
    accion, objetivo = cola_tareas.pop(0)
    match accion:
        case "crear":
            print(f"Creando: {objetivo}")
        case "actualizar":
            print(f"Actualizando: {objetivo}")
        case "eliminar":
            print(f"Eliminando: {objetivo}")
        case "magia":
            print(objetivo)
        case _:
            print(f"Error: La accion {accion} no es valida.")
print("Todas las tareas han sido correctamente procesadas.")