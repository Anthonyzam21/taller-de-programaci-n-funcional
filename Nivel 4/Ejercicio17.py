def memoizar_avanzado(fn_costosa, max_items):
    cache = {}
    orden = []

    def wrapper(*args):
        if args in cache:
            return cache[args]
        resultado = fn_costosa(*args)
        cache[args] = resultado
        orden.append(args)
        if len(orden) > max_items:
            viejo = orden.pop(0)
            del cache[viejo]
        return resultado
    return wrapper

import time
def funcion_lenta(x):
    time.sleep(1)
    return x * 2

memo = memoizar_avanzado(funcion_lenta, 3)
print(memo(5))  
print(memo(5))  
