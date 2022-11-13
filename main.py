import os
os.system('cls')

from bem_vindo import boas_vindas
from cadastro_usuario import registro
from shopping import selecionar_shopping
from loja import escolher_loja
from vaga import selecionar_vaga
from confirmar import confirmar_vaga

bem_vindo = boas_vindas()
registro = registro()
escolha_shopping = selecionar_shopping()
escolha_loja = escolher_loja(escolha_shopping)
vaga = selecionar_vaga(escolha_shopping, escolha_loja)
confirmar_vaga = confirmar_vaga()
