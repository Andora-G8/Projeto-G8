import os
os.system('cls')

from utils.bem_vindo import boas_vindas
from utils.cadastro_usuario import registro
from utils.menu_logado import selecionar_menu_logado
from utils.shopping import selecionar_shopping
from utils.loja import escolher_loja
from utils.vaga import selecionar_vaga
from utils.confirmar import confirmar_vaga
from utils.sair_vaga import sair_vaga
from utils.historico_reserva import registrar_historico
from utils.historico_reserva import visualizar_historico

bem_vindo = boas_vindas()
usuario_logado, cliente_id = registro()
menu_logado = 0

while menu_logado != 3:
    menu_logado = selecionar_menu_logado(usuario_logado)
    
    if menu_logado == 1: 
        escolha_shopping, shopping_nome = selecionar_shopping()
        escolha_loja, loja_nome = escolher_loja(escolha_shopping)
        vaga_id = selecionar_vaga(escolha_shopping, escolha_loja)
        reserva_chegada_confirmada, reserva_data, reserva_chegada_hora = confirmar_vaga()
        reserva_saida_hora = sair_vaga(usuario_logado)
        registro_historico = registrar_historico(cliente_id, shopping_nome, loja_nome, vaga_id, reserva_chegada_confirmada, reserva_data, reserva_chegada_hora, reserva_saida_hora)
    
    elif menu_logado == 2: 
        acessar_historico = visualizar_historico(cliente_id)
    