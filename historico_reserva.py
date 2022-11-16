from time import sleep
import pandas as pd
import os

    

def registrar_historico(cliente_id, shopping_nome, loja_nome, vaga_id, reserva_chegada_confirmada, reserva_data, reserva_chegada_hora, reserva_saida_hora):
    
    reserva = [cliente_id, shopping_nome, loja_nome, vaga_id, reserva_chegada_confirmada, reserva_data, reserva_chegada_hora, reserva_saida_hora]
   
    coluna = ['cliente_ID', 'shopping_nome', 'loja_nome', 'vaga_id', 'reserva_chegada_confirmada', 'reserva_data', 'reserva_chegada_hora', 'reserva_saida_hora']
    dataframe_historico = pd.read_csv('historico_reserva.csv')
    dataframe = pd.DataFrame([reserva], columns= coluna)
    dataframe_historico = pd.concat([dataframe, dataframe_historico])
    dataframe_historico.to_csv('historico_reserva.csv', index = False, header= True)

    return dataframe_historico

def visualizar_historico(cliente_id): 

    dataframe_historico = pd.read_csv('historico_reserva.csv')
    qtd_linhas = len(dataframe_historico)
    
    cliente_historico = False   

    print('Seu Histórico de Reserva')

    for linha in range(qtd_linhas):
        if dataframe_historico._get_value(linha, 0, takeable = True) == int(cliente_id): 
            cliente_historico = True
            print(f'Reserva no {dataframe_historico._get_value(linha, 1, takeable = True)} | {dataframe_historico.   _get_value(linha, 2, takeable = True)}\n',
                f'Data: {dataframe_historico._get_value(linha, 5, takeable = True)}\n',
                f'Local onde foi estacionado: {dataframe_historico._get_value(linha, 3, takeable = True)}\n',
                f'Horário de chegada: {dataframe_historico._get_value(linha, 6, takeable = True)} - {dataframe_historico._get_value(linha, 7, takeable = True)}\n',)
            sleep(3)
            print('Você será direcionado ao menu principal')
            sleep(3)
    
    
    
    if cliente_historico == False: 
       
        print("Você ainda não finalinalizou nenhuma reserva e voltará ao nosso menu!\n")
        sleep(2)
        
   
        






  




