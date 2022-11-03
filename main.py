import os
os.system('cls')

from boasVindas import boas_vindas
from shopping import selecionar_shopping
from loja import escolher_loja
from vaga import selecionar_vaga
from confirmar import confirmar_vaga

boasVindas = boas_vindas()
escolhaShopping = selecionar_shopping()
escolhaLoja = escolher_loja(escolhaShopping)
vaga = selecionar_vaga(escolhaShopping, escolhaLoja)
confirmarVaga = confirmar_vaga()
# print(f"Sua vaga é a {vaga}") 
