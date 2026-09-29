def crear_formateador(prefijo, fn_transformacion):
    def formateador(texto):
        return f"{prefijo}{fn_transformacion(texto)}"
    return formateador

mayusculas = crear_formateador(">> ", lambda t: t.upper())
print(mayusculas("bienvenidos a la clase de programacion"))
 
