import os
credenciados = {
        '1': {
            'a': {
                'A-250': 'Ocupada',
                'A-251': 'Disponível',
                'A-252': 'Disponível',
                'A-253': 'Disponível',
                'A-254': 'Disponível',
                'A-255': 'Disponível',
                'A-256': 'Ocupada',
                'A-257': 'Ocupada',
                'A-258': 'Disponível',
                'A-259': 'Disponível',},

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
                'B10':'Disponível',},

          'c': {'A1': 'Disponível',
                'A2': 'Disponível',
                'A3': 'Disponível',}
    }
}

def selecionar_vaga(escolha_shopping, escolha_loja):
    escolha_vaga = 0

    while escolha_vaga not in credenciados[escolha_shopping][escolha_loja]:
        
        for chave in credenciados[escolha_shopping][escolha_loja].keys():
            print(f'{chave} → {credenciados[escolha_shopping][escolha_loja][chave]}')

        escolha_vaga = input('\nSelecione a vaga: ').upper()

        if escolha_vaga not in credenciados[escolha_shopping][escolha_loja]:
            os.system('cls')
            print('Vaga INVÁLIDA. Escolha uma vaga existente!\n')
            
        verificar_vaga(escolha_shopping, escolha_loja, escolha_vaga)

    return escolha_vaga

def verificar_vaga(escolha_shopping, escolha_loja, escolha_vaga):
    while escolha_vaga in credenciados[escolha_shopping][escolha_loja]:
        if credenciados[escolha_shopping][escolha_loja][escolha_vaga] == 'Ocupada':
            os.system('cls')
            print('Vaga OCUPADA, escolha outra vaga!\n')
            for chave in credenciados[escolha_shopping][escolha_loja].keys():
                print(f'{chave} → {credenciados[escolha_shopping][escolha_loja][chave]}')
            escolha_vaga = input('\nSelecione a vaga: ').upper()

        else:
            os.system('cls')
            print(f'Vaga {escolha_vaga} selecionada com SUCESSO! Você tem 1 hora para chegar até a sua vaga!')
            credenciados[escolha_shopping][escolha_loja][escolha_vaga] = 'Ocupada'
            break
        