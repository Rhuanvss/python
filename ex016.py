def expoente(numero):
    return numero * 2
    
ex2 = expoente(3)

def expoente(numero):
    return numero * 3
    
ex3 = expoente(3)

def expoente(numero):
    return numero * 4
    
ex4 = expoente(3)

print(ex2)
print(ex3)
print(ex4)

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

dulplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(dulplicar(2))
print(triplicar(2))
print(quadruplicar(2))
