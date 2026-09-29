def crear_operador(factor, operacion_lambda):
    def operador(lista):
        return list(map(lambda x: operacion_lambda(x, factor), lista))
    return operador

multiplicar = crear_operador(3, lambda x, f: x * f)
print(multiplicar([1, 2, 3]))  
