def crear_validador_multiple(*lambdas_criterios):
    def validador(objeto):
        return all(criterio(objeto) for criterio in lambdas_criterios)
    return validador

validador_usuario = crear_validador_multiple(
    lambda u: u["edad"] >= 18,
    lambda u: "@" in u["email"]
)

print(validador_usuario({"edad": 20, "email": "test@mail.com"}))  
print(validador_usuario({"edad": 15, "email": "mail.com"}))       
