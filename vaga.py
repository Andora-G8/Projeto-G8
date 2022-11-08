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
            'G2-246': 'Ocupada',
            'G2-217': 'Disponível',
            'G2-247': 'Disponível', 
            'G2-216': 'Ocupada',
            'G2-248': 'Disponível',
            'G2-215': 'Disponível',
            'G2-249': 'Ocupada',
            'G2-214': 'Disponível',
            'G2-250': 'Disponível',
            'G2-213':'Disponível',
        },
        'c': { 
            'G3-246': 'Disponível',
            'G3-217': 'Ocupada',
            'G3-247': 'Disponível', 
            'G3-216': 'Ocupada',
            'G3-248': 'Ocupada',
            'G3-215': 'Disponível',
            'G3-249': 'Ocupada',
            'G3-214': 'Ocupada',
            'G3-250': 'Disponível',
            'G3-213': 'Disponível',
        }
    },
    '2': {
        'a':{
            'G1-171': 'Ocupada',
            'G1-172': 'Disponível',
            'G1-173': 'Disponível',
            'G1-216': 'Disponível',
            'G1-248': 'Disponível',
            'G1-215': 'Disponível',
            'G1-249': 'Ocupada',
            'G1-214': 'Ocupada',
            'G1-250': 'Disponível',
            'G1-213': 'Disponível',
        },
    },
    '3':{
        'a': {

        },
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
