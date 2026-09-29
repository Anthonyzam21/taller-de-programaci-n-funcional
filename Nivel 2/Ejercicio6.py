def crear_contador_paso(fn_paso):
    cuenta = 0
    def contador():
        nonlocal cuenta
        cuenta = fn_paso(cuenta)
        return cuenta
    return contador

contador_doble = crear_contador_paso(lambda c: c + 2)
print(contador_doble())  
print(contador_doble())  