# Criar lista/dicionário de vagas

credenciados = {
    '1': {
        'a': {
            'G1': 'Ocupada',
            'G2': 'Disponível',
            'G3': 'Disponível',
        },
        'b': {
            'B1': 'Ocupada',
            'B2': 'Disponível',
        },
        'c': {
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
            print('Vaga selecionada com sucesso!')
            credenciados[escolhaShopping][escolhaLoja][escolhaVaga] = 'Ocupada'
            print(credenciados[escolhaShopping][escolhaLoja])
            break

def selecionar_vaga(escolhaShopping, escolhaLoja): # A função pode receber zero ou mais parâmetros
    escolhaVaga = 0
    while escolhaVaga not in credenciados[escolhaShopping][escolhaLoja]:
        print(credenciados[escolhaShopping][escolhaLoja])
        escolhaVaga = input('Selecione a vaga: ').upper()
        if escolhaVaga not in credenciados[escolhaShopping][escolhaLoja]:
            print ("Comando inválido. Escolha um comando correspondente.")
            
        verificar_vaga(escolhaShopping, escolhaLoja, escolhaVaga)
    return escolhaVaga
