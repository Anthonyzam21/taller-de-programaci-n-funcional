def crear_pipeline(*funciones_transformacion):
    def ejecutar(dato_inicial):
        resultado = dato_inicial
        for fn in funciones_transformacion:
            resultado = fn(resultado)
        return resultado
    return ejecutar

pipeline = crear_pipeline(
    lambda x: x + 2,
    lambda x: x * 3,
    lambda x: f"Resultado: {x}"
)

print(pipeline(5)) 
