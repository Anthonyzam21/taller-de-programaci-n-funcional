def crear_consultor(campo):
    def consultor(fn_condicion):
        def filtro(lista):
            return [obj for obj in lista if fn_condicion(obj[campo])]
        return filtro
    return consultor

usuarios = [
    {"nombre": "Carlos", "edad": 25},
    {"nombre": "Luis", "edad": 17},
    {"nombre": "Marta", "edad": 30}
]

consultar_por_edad = crear_consultor("edad")
mayores_de_20 = consultar_por_edad(lambda e: e > 20)

print(mayores_de_20(usuarios))

