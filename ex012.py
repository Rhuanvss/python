lista = []

while True:
    print('selecione uma opção')
    opcao = input('[I]nserir [A]pagar [L]istar ')
    opcao.upper
    if opcao == 'I':
            inserir = input('valor: ')
            lista.append(inserir)
    elif opcao == 'L':
          print(lista)
    elif opcao == 'A':
        apagar = input('insira o indice para apagar ')
        try:
            apagar_int = int(apagar)
            del lista[apagar_int]
        except ValueError:
             print('não foi possivel apagar o indice, digite um numero inteiro')
        except IndexError:
             print('indice não existe na lista')
    else:
        print('por favor escolha I, A ou L')