def crear_promediador_filtrado(filtro_ruido_lambda):
    datos = []
    def promediador(valor):
        nonlocal datos
        if filtro_ruido_lambda(valor):
            datos.append(valor)
        return sum(datos) / len(datos) if datos else 0
    return promediador

promediador = crear_promediador_filtrado(lambda v: 0 <= v <= 100)
print(promediador(50))   
print(promediador(200))  
print(promediador(70))  