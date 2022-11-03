from random import randint
from time import sleep

def gerar_pins():
    # Gerar 4 números aleatórios
    gerar = [randint(0, 9) for x in range(4)]
    sleep(10)
    print(f"Quando você chegar na sua vaga insira o seguinte PIN: {gerar}")
    return gerar

def validar(pin, tentativa):
    # Verificar se a tentativa é igual ao pin
    return pin == tentativa

def confirmar_vaga():
    pin = gerar_pins()
    tentativa = [int(x) for x in input("você chegou na sua vaga! Por favor, digite o PIN: ")]

    while not validar(pin, tentativa):
        tentativa = [int(x) for x in input("PIN Incorreto! Por favor, digite o PIN correto: ")]
    print("PIN correto! Vaga validada! Divirta-se!")
