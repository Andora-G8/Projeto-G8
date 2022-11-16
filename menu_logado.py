import os

menu_logado = {1: 'Reserve sua Vaga',
               2: 'Histórico de Reservas',
               3: 'Fechar Aplicativo'}

def selecionar_menu_logado(usuario): 
    escolha_menu = 0
    print(f'Bem vinde, {usuario}!\n')

    while escolha_menu not in menu_logado:
        print('Menu Home:\n')
        
        for chave in menu_logado.keys():
            print(f'{chave} → {menu_logado[chave]}')

        escolha_menu = int(input('\nDigite o código do que deseja fazer: '))

        if escolha_menu == 1: 
            os.system('cls')
            escolha_menu = 1

        elif escolha_menu == 2: 
            os.system('cls')
            escolha_menu = 2
        
        elif escolha_menu == 3: 
            os.system('cls')
            print("Aplicação encerrada, volte sempre ao ParkIt\n")
            break
        else:
            os.system('cls')
            print('Opção INVÁLIDA. Escolha uma Opção existente!\n')
     
    return escolha_menu



    
            
