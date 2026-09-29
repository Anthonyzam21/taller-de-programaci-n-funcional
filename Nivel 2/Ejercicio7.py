def crear_acumulador_validado(criterio_lambda):
    total = 0
    def acumulador(valor):
        nonlocal total
        if criterio_lambda(valor):
            total += valor
        return total
    return acumulador

acum_positivos = crear_acumulador_validado(lambda v: v > 0)
print(acum_positivos(5))   
print(acum_positivos(-3))  
print(acum_positivos(10))  