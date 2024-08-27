hora = int(input('digite a hora atual: '))
# manha = hora <= 11
# tarde = hora > 11 and hora <= 17
# noite = hora >17 and hora <= 24
if hora <= 11:
    print('bom dia')
elif hora > 11 and hora <= 17:
    print('boa tarde')
elif hora >17 and hora <= 24:
    print('boa noite')
else:
    print('digite uma hora valida')