def crear_conversor(tasa, margen_lambda):
    def convertir(monto):
        margen = margen_lambda(monto)
        return monto * tasa + margen
    return convertir

usd_a_eur = crear_conversor(0.92, lambda m: m * 0.02)  
print(usd_a_eur(100)) 
