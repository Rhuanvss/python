import os
palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0
while True:
    letra_digitada = input('digite apenas uma letra: ')
    if len(letra_digitada) > 1:
        print('digite apenas 1 letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    tentativas += 1
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('PARABÉNS VOCÊ GANHOU')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', tentativas)
