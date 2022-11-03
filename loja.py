credenciados = {
    '1': {
        'a': 'Renner',
        'b': 'C&A',
        'c': 'Tokstok',
    },
    '2': {
        'a': 'Camicado',
        'b': 'Tokstok',
        'c': 'Riachuelo',
    },
    '3':{ 
        'a': 'Renner',
        'b': 'McDonalds',
    }
}

def escolher_loja(escolhaShopping):
    escolhaLoja = 0
    while escolhaLoja not in credenciados[escolhaShopping]:
        print(credenciados[escolhaShopping])
        escolhaLoja = input('Selecione a loja: ').lower()
        if escolhaLoja in credenciados[escolhaShopping].keys():
            print(credenciados[escolhaShopping][escolhaLoja])
        elif escolhaLoja not in credenciados[escolhaShopping]:
            print("Comando inválido. Escolha um comando correspondente.")
    return escolhaLoja
