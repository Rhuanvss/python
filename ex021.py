produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
import copy

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.10, 2)}
    for p in copy.deepcopy(produtos)
]

ordena = sorted(
    copy.deepcopy(produtos), 
    key=lambda p: p['nome'],
    reverse=True
)

ordena_crescente = sorted(
    copy.deepcopy(produtos), 
    key=lambda p: p['preco']
)

print(*novos_produtos, sep= '\n')
print()
print(*ordena, sep= '\n')
print()
print(*ordena_crescente, sep= '\n')