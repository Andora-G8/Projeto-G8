import pandas as pd
import os

def criar_historico():
    coluna = ['cliente_ID', 'shopping_nome', 'loja_nome', 'vaga_id', 'reserva_chegada_confirmada', 'reserva_data', 'reserva_chegada_hora', 'reserva_saida_hora']
    dataframe_inicial = pd.DataFrame(None, columns=coluna)
    dataframe_inicial.to_csv('historico_reserva.csv', header= True, index = False)
    os.system('cls')
    print("CSV gerado")
    return coluna

# index = True, index_label = 'reserva_id'    



criar_historico()

