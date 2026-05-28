historial_chat = ["!ping", "!estado", "!reproducir", "!salir", "!ban"]

for comando in historial_chat:
    match comando:
        case "!ping":
            print("Pong!")
        case "!estado":
            print("El servidor esta Online")
        case "!reproducir":
            print("Reproduciendo playlist")
        case "!salir":
            print("Apagando el bot")
            break
        case "!ban":
            print("Un usuario a sido baneado")
        case _:
            print("Comando no encontrado :c")
    