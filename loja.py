import os

credenciados = {
    '1': {'a': 'Renner',
          'b': 'C&A',
          'c': 'Tokstok',
          'd': 'Hiper', 
          'e': 'Leitura',
          'f': 'Americanas',
          'g': 'Casas Bahia',
          'h': 'Le Biscuit',
          'i': 'Riachuelo',
          'j': 'Jurandir Pires',},

    '2': {'a': 'Coco bambu',
          'b': 'Banco do Brasil',
          'c': 'Riachuelo',
          'd': 'Praça de Alimentação'},

    '3':{ 'a': 'Renner',
          'b': 'McDonalds',
          'c': 'Americanas',
          'd': 'Diagmax',
          'e': 'Tokstok'},

    '4':{ 'a': 'Donna Brigadeiro',
          'b': 'Detran',
          'c': 'Americanas',
          'd': 'Hiper Bompreço',
          'e': 'Kalunga'},

    '5':{ 'a': 'Nagem',
          'b': 'Centauro',
          'c': 'Americanas',
          'd': 'Game Station',
          'e': 'Big Bompreço',
          'f': 'Marisa',
          'g': 'Toli',
          'h': 'Farm',
          'i': 'Saraiva',
          'j': 'Tokstok'},
}


def escolher_loja(escolha_shopping):
    escolha_loja = 0
    
    while escolha_loja not in credenciados[escolha_shopping]:    

        for chave in credenciados[escolha_shopping].keys():
            print(f'{chave} → {credenciados[escolha_shopping][chave]}')

        escolha_loja = input('\nSelecione a loja: ').lower() 

        if escolha_loja == "d" or escolha_loja == "e" or escolha_loja == "f" :
            escolha_loja = "a"

        elif escolha_loja == "g" or escolha_loja == "h":
            escolha_loja = "b"

        elif escolha_loja == "j" or escolha_loja == "i":
            escolha_loja = "c"

        if escolha_loja in credenciados[escolha_shopping].keys():
            os.system('cls') 
            print(f"A entrada mais próxima da loja selecionada é: {credenciados[escolha_shopping][escolha_loja]}\n")
        else:
            os.system('cls')
            print("Loja INVÁLIDA. Escolha uma loja existente.\n")
    return escolha_loja, credenciados[escolha_shopping][escolha_loja]
