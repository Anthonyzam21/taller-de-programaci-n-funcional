def crear_generador_sufijos(patron_lambda):
    contador = {"n": 0}
    def generador(nombre):
        contador["n"] += 1
        return patron_lambda(nombre, contador["n"])
    return generador

sufijo_archivos = crear_generador_sufijos(lambda n, i: f"{n}_{i}.txt")
print(sufijo_archivos("documento"))  
print(sufijo_archivos("taller"))  
