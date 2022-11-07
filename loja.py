# Mostrar apenas vagas disponíveis
# Lista referente a loja dizendo quantas vagas tem em cada uma daquelas lojas => Mostrar 
#               quantas vagas disponíneis em cada uma das lojas 
# 
# ##
credenciados = {
    '1': {
        'a': 'Renner',
        'b': 'C&A',
        'c': 'Tokstok',
        'd': 'Hiper', # Tupla com nome da loja e loja de vaga mais próxima pra assim ele inspecionar quais lojas próximas tem vagas
        'e': 'Leitura',
        'f': 'Americanas',
        'g': 'Casas Bahia',
        'h': 'Le Biscuit',
        'i': 'Riachuelo',
        'j': 'Jurandir Pires',
        # 10 lojas, as 3 primeiras são lojas âncoras e as demais são lojas secundárias
        # lojas d, e , f ligadas a loja A
        # lojas g, h ligadas a loja B
        # lojas j, i ligadas a loja C
    },
    '2': { #Shopping Recife => Sem vagas relacionadas a este shopping 
        'a': 'Camicado',
        'b': 'Tokstok',
        'c': 'Riachuelo',
    },
    '3':{ # Shopping Rio Mar => Sem vagas relacionadas a este shopping
        'a': 'Renner',
        'b': 'McDonalds',
    }
}

def escolher_loja(escolhaShopping):
    escolhaLoja = 0
    while escolhaLoja not in credenciados[escolhaShopping]: # Após a escolha do shopping ele verifica as lojas          
        # Referentes aquele shopping credenciado
        print(credenciados[escolhaShopping]) # Printa as lojas referentes ao shopping 
        escolhaLoja = input('Selecione a loja: ').lower() # Pede a loja que o cliente deseja
        if escolhaLoja == "d" or escolhaLoja == "e" or escolhaLoja == "f" :
            escolhaLoja = "a"
        elif escolhaLoja == "g" or escolhaLoja == "h":
            escolhaLoja = "b"
        elif escolhaLoja == "j" or escolhaLoja == "i":
            escolhaLoja = "c"
        if escolhaLoja in credenciados[escolhaShopping].keys(): # 
            #if escolhaLoja =='h':
                 #credenciados[escolhaShopping][escolhaLoja].keys()
            print(f"\nA entrada mais próxima da loja selecionada é {credenciados[escolhaShopping][escolhaLoja]}\n")
        elif escolhaLoja not in credenciados[escolhaShopping]:
            print("\nComando inválido. Escolha um comando correspondente.\n")
    return escolhaLoja
