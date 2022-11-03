# Criar lista/dicionário?? de credenciados
credenciados = {'1': 'Shopping Tacaruna',
                '2': 'Shopping Recife',
                '3': 'Shopping Rio Mar',
                '4': 'Shopping Plaza',
                '5': 'Camará Shopping'}

def selecionar_shopping():
    escolhaShopping = 0
    while escolhaShopping not in credenciados:
        print(credenciados)
        escolhaShopping = input('Selecione o shopping: ')
        if escolhaShopping in credenciados.keys():
            print(credenciados[escolhaShopping])
        elif escolhaShopping not in credenciados:
            print("Comando inválido. Escolha um código válido!")
    return escolhaShopping
