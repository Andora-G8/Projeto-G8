
import os
from time import sleep
from datetime import datetime

menu_sim_nao = {'1': 'Não',
                '2': 'Sim',}

def sair_vaga(usuario): 
    sleep(5)
    sair_vaga = 0

    while sair_vaga != 1:
        
        print(f'{usuario}, seu carro ainda se encontra estacionado na vaga? \n')

        for chave in menu_sim_nao.keys():
            print(f'{chave} → {menu_sim_nao[chave]}')

        sair_vaga = input('\nDigite sua resposta:')
        sair_vaga = int(sair_vaga)
        
        if sair_vaga == 1: 
            os.system('cls')
            print(f'\n{usuario}, Obrigada por utilizar os serviços da PartIt! \nVocê será redirecionade ao menu principal\n')
            saida_hora = datetime.now()
            reserva_saida_hora = saida_hora.strftime('%H:%M')
            sleep(5)

        else:
            os.system('cls')
            sleep(5)
            os.system('cls')
            print('Você ainda chegou, ou digitou uma escolha invalida. Escolha uma das opções apresentadas!\n')    

    return reserva_saida_hora

