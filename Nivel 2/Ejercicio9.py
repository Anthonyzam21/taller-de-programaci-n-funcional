def crear_limitador_avanzado(max_intentos, fn_alerta):
    intentos = 0
    def limitador():
        nonlocal intentos
        intentos += 1
        if intentos > max_intentos:
            fn_alerta(intentos)
            intentos = 0  
        return intentos
    return limitador

alerta = lambda i: print(f"Límite superado en intento {i}")
limiter = crear_limitador_avanzado(3, alerta)
for _ in range(7):
    print("Intento:", limiter())