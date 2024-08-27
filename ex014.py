def soma(*args):  
    total = 1   
    for numero in args:
        total = total * numero
    return total


numeros = 1, 2, 3, 4, 5
outra_soma = soma(*numeros)
print(outra_soma)