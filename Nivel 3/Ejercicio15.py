import time

def auditar_ejecucion(fn_objetivo, fn_logger):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = fn_objetivo(*args, **kwargs)
        fin = time.time()
        duracion = fin - inicio
        fn_logger(f"Función {fn_objetivo.__name__} ejecutada en {duracion:.4f}s")
        return resultado
    return wrapper

logger = lambda msg: print("LOG:", msg)

def tarea_pesada(n):
    suma = 0
    for i in range(n):
        suma += i
    return suma

tarea_auditada = auditar_ejecucion(tarea_pesada, logger)
print(tarea_auditada(1000000))
