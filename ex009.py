while True:
    n1 = input('digite um número: ')
    n2 = input('digite outro número: ')
    operador = input('digite seu operador (+-*/): ')
    numeros_validos = None
    n1_float = 0
    n2_float = 0
    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos  os numeros são invalidos.')
        continue
    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Seu operador não é valido.')
        continue
    if len(operador) > 1:
        print('digite apenas 1 operador.')
        continue

    if operador == '+':
        print(f'a soma dos numeros {n1_float} e {n2_float} é de {n1_float + n2_float}')
    elif operador == '-':
        print(f'a subtração dos numeros {n1_float} e {n2_float} é de {n1_float - n2_float}')
    elif operador == '*':
        print(f'a multiplicação dos numeros {n1_float} e {n2_float} é de {n1_float * n2_float}')
    elif operador == '/':
        print(f'a divisão dos numeros {n1_float} e {n2_float} é de {n2_float / n2_float}')
    else:
        print('nunca deveria chegar aqui.')

    sair = input('quer sair? [Sim] ou [Não]: ').lower().startswith('s')
    if sair is True:
        break
