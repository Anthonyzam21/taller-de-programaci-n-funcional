def componer_dos(f, g):
    def compuesto(x):
        return f(g(x))
    return compuesto

doble = lambda x: x * 2
incrementar = lambda x: x + 1

comp = componer_dos(doble, incrementar)
print(comp(5))  