nome = input('digite seu nome: ')
tamanho_nome = len(nome)
nova_str = ''
contador = 0
while contador < tamanho_nome:
    nova_str += '*' + nome[contador]
    contador += 1
print(nova_str)
