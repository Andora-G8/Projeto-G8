# Criar lista/dicionário de vagas

credenciados = {
    '1': {
        'a': {
            'G1-246': 'Ocupada',
            'G1-217': 'Disponível',
            'G1-247': 'Disponível',
            'G1-216': 'Disponível',
            'G1-248': 'Disponível',
            'G1-215': 'Disponível',
            'G1-249': 'Ocupada',
            'G1-214': 'Ocupada',
            'G1-250': 'Disponível',
            'G1-213': 'Disponível',
        },
        'b': {
            'B1': 'Ocupada',
            'B2': 'Disponível',
            'B3': 'Disponível', 
            'B4': 'Ocupada',
            'B5': 'Disponível',
            'B6': 'Disponível',
            'B7': 'Ocupada',
            'B8': 'Disponível',
            'B9': 'Disponível',
            'B10':'Disponível',
        },
        'c': { # COLOCAR MAIS VAGAS
            'A1': 'Disponível',
            'A2': 'Disponível',
            'A3': 'Disponível', 
        }
    }
}

def verificar_vaga(escolhaShopping, escolhaLoja, escolhaVaga):
    while escolhaVaga in credenciados[escolhaShopping][escolhaLoja]:
        if credenciados[escolhaShopping][escolhaLoja][escolhaVaga] == 'Ocupada':
            print('Vaga ocupada, escolha outra vaga.')
            escolhaVaga = input('Selecione a vaga: ').upper()
        else:
            print(f'\nVaga {escolhaVaga} selecionada com sucesso! Você tem 1 hora para chegar até a sua vaga!\n')
            credenciados[escolhaShopping][escolhaLoja][escolhaVaga] = 'Ocupada'
            break

def selecionar_vaga(escolhaShopping, escolhaLoja): # A função pode receber zero ou mais parâmetros
    escolhaVaga = 0
    while escolhaVaga not in credenciados[escolhaShopping][escolhaLoja]:
        print(credenciados[escolhaShopping][escolhaLoja])
        escolhaVaga = input('\nSelecione a vaga: ').upper()
        if escolhaVaga not in credenciados[escolhaShopping][escolhaLoja]:
            print ("\nComando inválido. Escolha um comando correspondente.\n")
            
        verificar_vaga(escolhaShopping, escolhaLoja, escolhaVaga)
    return escolhaVaga
