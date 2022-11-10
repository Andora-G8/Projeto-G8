# Criar lista/dicionário?? de credenciados
credenciados = {'1': 'Shopping Tacaruna',
                '2': 'Shopping Recife',
                '3': 'Shopping Rio Mar',
                '4': 'Shopping Plaza',
                '5': 'Camará Shopping'}

def selecionar_shopping(): #primeira função quando o código inicia
    escolhaShopping = 0
    while escolhaShopping not in credenciados: 
        print(credenciados) # Se o shopping não estiver em credenciados print os credenciados
        escolhaShopping = input('Selecione o shopping: ') # Atribui um novo valor a variável escolhaShopping, referente
        # ao shopping que a pessoa quer ir.
        if escolhaShopping in credenciados.keys(): # Se a chave estiver em credenciados ele printa a escolha 
            print(f"\nO local escolhido foi o {credenciados[escolhaShopping]}\n")
        else:
            print("\nComando inválido. Escolha um código válido!\n")
    return escolhaShopping
