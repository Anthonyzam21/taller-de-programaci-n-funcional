def ejecutar_y_rastrear(fn_tarea, n):
    historial = []
    def ejecutor():
        nonlocal historial
        for _ in range(n):
            historial.append(fn_tarea())
        return historial
    return ejecutor

import random
ejecutor = ejecutar_y_rastrear(lambda: random.randint(1, 10), 3)
print(ejecutor())  
print(ejecutor())  