dicionario_exemplo = {
    'NOME SHOPPING': {'LOJAS': [('VAGA', 'DISPONIBILIDADE')]}
}

dicionario_pratico = {
    'Shopping Recife': {'Renner': [('G1-217', 'Disponível'), ('G1-246', 'Ocupada')],
                        'C&A': [('B1', 'Ocupada'), ('B2', 'Disponível')]},

    'Shopping Tacaruna': {'Camicado': [('A1', 'Ocupada'), ('A2', 'Disponível')]}
}


def selecionar_shopping():
    escolha_shopping = 0

    while escolha_shopping not in dicionario_pratico: 
            print('Aperte o número do Shopping que você deseja\n')

            for index in range(len(dicionario_pratico)):
                print(f'{index+1} → {list(dicionario_pratico)[index]}')

            escolha_shopping = int(input('\nSelecione o shopping: '))

            if escolha_shopping == 1: 
                print(dicionario_pratico['Shopping Recife'])

            elif escolha_shopping == 2: 
                print(dicionario_pratico['Shopping Tacaruna'])
            
            elif escolha_shopping == 3: 
                print(dicionario_pratico['Shopping Plaza'])