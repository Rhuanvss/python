n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('{} é maior que {}'.format(n2, n1))
else:
    print('os numeros são iguais')