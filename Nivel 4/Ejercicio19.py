def crear_sistema_eventos():
    suscriptores = []

    def sistema(accion, fn=None, evento=None):
        nonlocal suscriptores
        if accion == "suscribir" and fn:
            suscriptores.append(fn)
        elif accion == "emitir" and evento:
            for sub in suscriptores:
                sub(evento)
    return sistema

pubsub = crear_sistema_eventos()
pubsub("suscribir", lambda e: print("Listener 1 recibió:", e))
pubsub("suscribir", lambda e: print("Listener 2 recibió:", e))

pubsub("emitir", evento="Evento de prueba")
