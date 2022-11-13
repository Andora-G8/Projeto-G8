import os

credenciados = {'1': 'Shopping Tacaruna',
                '2': 'Shopping Recife',
                '3': 'Shopping Rio Mar',
                '4': 'Shopping Plaza',
                '5': 'Camará Shopping'}

def selecionar_shopping(): 
    escolha_shopping = 0

    print('\nDigite o código do shopping desejado: \n')

    for chave in credenciados.keys():
        print(f'{chave} → {credenciados[chave]}')

    escolha_shopping = input('\nSelecione o shopping: ')

    if escolha_shopping == 1: 
        print('Shopping Tacaruna')

    elif escolha_shopping == 2: 
        print('Shopping Recife')
            
    elif escolha_shopping == 3: 
        print('Shopping Rio Mar')

    return escolha_shopping
