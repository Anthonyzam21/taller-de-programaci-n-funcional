def agrupar_por(lista, fn_clave):
    agrupado = {}
    for item in lista:
        clave = fn_clave(item)
        if clave not in agrupado:
            agrupado[clave] = []
        agrupado[clave].append(item)
    return agrupado

personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Marta", "edad": 25}
]

agrupado = agrupar_por(personas, lambda p: p["edad"])
print(agrupado)
