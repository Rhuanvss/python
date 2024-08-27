cpf = input('digite seu cpf: ').replace('.', '').replace('-', '').replace(' ', '')
cpf_digitos = cpf[:9]
cont = 10
resultado = 0
resultado_2 = 0
for digito in cpf_digitos:
    resultado += int(digito) * cont     
    cont -= 1
digito1 = (resultado * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0

cont_2 = 11
cpf_2 = cpf_digitos + str(digito1)
for digito in cpf_2:
    resultado_2 += int(digito) * cont_2     
    cont_2 -= 1
digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
cpf_calculo = f'{cpf_digitos}{digito1}{digito_2}'
if cpf == cpf_calculo:
    print(f'{cpf} é valido')
else:
    print('CPF Invalido')
