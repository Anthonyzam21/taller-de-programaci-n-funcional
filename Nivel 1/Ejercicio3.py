def crear_descuento_dinamico(regla_condicional_lambda):
    def aplicar_descuento(precio):
        if regla_condicional_lambda(precio):
            return precio * 0.9  
        return precio
    return aplicar_descuento

descuento_mayores_100 = crear_descuento_dinamico(lambda p: p > 100)
print(descuento_mayores_100(150))  
print(descuento_mayores_100(80))   
