import os

credenciados = {'1': 'Shopping Tacaruna',
                '2': 'Shopping Recife',
                '3': 'Shopping Rio Mar',
                '4': 'Shopping Plaza',
                '5': 'Camará Shopping'}

def selecionar_shopping(): 
    escolha_shopping = 0

    while escolha_shopping not in credenciados:

        print('\nDigite o código do shopping desejado: \n')

        for chave in credenciados.keys():
            print(f'{chave} → {credenciados[chave]}')

        escolha_shopping = input('\nSelecione o shopping: ')

        if escolha_shopping in credenciados.keys():
            os.system('cls') 
            print(f"O Shopping escolhido é: {credenciados[escolha_shopping]}\n")
        
        else:
            os.system('cls')
            print('Shopping INVÁLIDO. Escolha um Shopping existente!')

    return escolha_shopping, credenciados[escolha_shopping]
