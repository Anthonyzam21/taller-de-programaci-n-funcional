def crear_conmutador(lista_estados):
    indice = 0
    def conmutador():
        nonlocal indice
        estado = lista_estados[indice]
        indice = (indice + 1) % len(lista_estados)
        return estado
    return conmutador

switch = crear_conmutador(["rojo", "verde", "azul"])
print(switch())  
print(switch())  
print(switch())  
print(switch())  