import os
credenciados = {
        '1': {
            'a': {'A-250': 'Ocupada',
                'A-251': 'Disponível',
                'A-252': 'Disponível',
                'A-253': 'Disponível',
                'A-254': 'Disponível',
                'A-255': 'Disponível',
                'A-256': 'Ocupada',
                'A-257': 'Ocupada',
                'A-258': 'Disponível',
                'A-259': 'Disponível',},

            'b': {'R-110': 'Ocupada',
                'R-113': 'Disponível',
                'R-114': 'Disponível', 
                'R-115': 'Ocupada',
                'R-116': 'Disponível',
                'R-116': 'Disponível',
                'R-117': 'Ocupada',
                'R-118': 'Disponível',
                'R-119': 'Disponível',
                'R-120': 'Disponível',},

            'c': {'D-54': 'Disponível',
                'D-55': 'Ocupada',
                'D-56': 'Ocupada',
                'D-57': 'Ocupada',
                'D-58': 'Disponível',
                'D-59': 'Disponível',
                'D-60': 'Disponível',},},
        '2': {
            'a':{'A-250': 'Ocupada',
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
                'R-110': 'Ocupada',
                'R-113': 'Disponível',
                'R-114': 'Disponível', 
                'R-115': 'Ocupada',
                'R-116': 'Disponível',
                'R-116': 'Disponível',
                'R-117': 'Ocupada',
                'R-118': 'Disponível',
                'R-119': 'Disponível',
                'R-120': 'Disponível',},

            'c': {'D-54': 'Disponível',
                'D-55': 'Ocupada',
                'D-56': 'Ocupada',
                'D-57': 'Ocupada',
                'D-58': 'Disponível',
                'D-59': 'Disponível',
                'D-60': 'Disponível',},},
        '3': {
            'a':{'A-250': 'Ocupada',
                'A-251': 'Disponível',
                'A-252': 'Disponível',
                'A-253': 'Disponível',
                'A-254': 'Disponível',
                'A-255': 'Disponível',
                'A-256': 'Ocupada',
                'A-257': 'Ocupada',
                'A-258': 'Disponível',
                'A-259': 'Disponível',},

          'b': {'R-110': 'Ocupada',
                'R-113': 'Disponível',
                'R-114': 'Disponível', 
                'R-115': 'Ocupada',
                'R-116': 'Disponível',
                'R-116': 'Disponível',
                'R-117': 'Ocupada',
                'R-118': 'Disponível',
                'R-119': 'Disponível',
                'R-120': 'Disponível',},

          'c': {'D-54': 'Disponível',
                'D-55': 'Ocupada',
                'D-56': 'Ocupada',
                'D-57': 'Ocupada',
                'D-58': 'Disponível',
                'D-59': 'Disponível',
                'D-60': 'Disponível',},},
        '4': {
            'a':{'A-250': 'Ocupada',
                'A-251': 'Disponível',
                'A-252': 'Disponível',
                'A-253': 'Disponível',
                'A-254': 'Disponível',
                'A-255': 'Disponível',
                'A-256': 'Ocupada',
                'A-257': 'Ocupada',
                'A-258': 'Disponível',
                'A-259': 'Disponível',},

            'b': {'R-110': 'Ocupada',
                'R-113': 'Disponível',
                'R-114': 'Disponível', 
                'R-115': 'Ocupada',
                'R-116': 'Disponível',
                'R-116': 'Disponível',
                'R-117': 'Ocupada',
                'R-118': 'Disponível',
                'R-119': 'Disponível',
                'R-120': 'Disponível',},

            'c': {'D-54': 'Disponível',
                'D-55': 'Ocupada',
                'D-56': 'Ocupada',
                'D-57': 'Ocupada',
                'D-58': 'Disponível',
                'D-59': 'Disponível',
                'D-60': 'Disponível',},},
        '5': {
            'a':{'A-250': 'Ocupada',
                'A-251': 'Disponível',
                'A-252': 'Disponível',
                'A-253': 'Disponível',
                'A-254': 'Disponível',
                'A-255': 'Disponível',
                'A-256': 'Ocupada',
                'A-257': 'Ocupada',
                'A-258': 'Disponível',
                'A-259': 'Disponível',},

          'b': {'R-110': 'Ocupada',
                'R-113': 'Disponível',
                'R-114': 'Disponível', 
                'R-115': 'Ocupada',
                'R-116': 'Disponível',
                'R-116': 'Disponível',
                'R-117': 'Ocupada',
                'R-118': 'Disponível',
                'R-119': 'Disponível',
                'R-120': 'Disponível',},

          'c': {'D-54': 'Disponível',
                'D-55': 'Ocupada',
                'D-56': 'Ocupada',
                'D-57': 'Ocupada',
                'D-58': 'Disponível',
                'D-59': 'Disponível',
                'D-60': 'Disponível',},}
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
