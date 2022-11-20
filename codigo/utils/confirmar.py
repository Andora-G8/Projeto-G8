from random import randint
from time import sleep
from datetime import date
from datetime import datetime
import os

def gerar_pins():
    gerar = [randint(0, 9) for x in range(4)]
    print(f"\nQuando chegar a sua vaga, insira o PIN: {gerar}")
    sleep(5)
    return gerar

def validar(pin, tentativa):
    return pin == tentativa
    
def confirmar_vaga(): 
    pin = gerar_pins()
    tentativa = [int(x) for x in input("\nVocê chegou na sua vaga! Por favor, digite o PIN: ")]

    while not validar(pin, tentativa):
        os.system('cls')
        print(f'Seu PIN: {pin}')
        tentativa = [int(x) for x in input("\nPIN Incorreto! Por favor, digite o PIN correto: ")]

    os.system('cls')
    print("PIN correto! Vaga validada! Aproveite!\n")
    
    reserva_data = date.today()
    reserva_data = reserva_data.strftime('%d/%m/%Y')

    chegada_hora = datetime.now()
    reserva_chegada_hora = chegada_hora.strftime('%H:%M')

    return True, reserva_data, reserva_chegada_hora

    