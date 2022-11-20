import random
import os

def cadastrar(usuario,senha):
    arq = open('cadastro.txt', 'a')
    pin = gerar_pin_id()
    arq.write(f'{usuario};{senha};{pin}\n')
    arq.close()

def login(usuario,senha):
    arq = open('cadastro.txt', 'r')
    for linha in arq:
        linha = linha.strip()
        usuario_txt = linha.split(';')[0]
        senha_txt = linha.split(';')[1].split(';')[0]
        if usuario == usuario_txt and senha == senha_txt:
            return True
    return False

def verificar_usuario(usuario):
    arq = open('cadastro.txt', 'r')
    for linha in arq:
        if usuario in linha:
            return True
    return False

def gerar_pin_id():
    pin_id = ''
    for i in range(0,5):
        pin_id += str(random.randint(1,9))
    return pin_id

def acessar_client_id(usuario,senha):
    arq = open('cadastro.txt', 'r')
    
    for linha in arq:
        linha = linha.strip()
        usuario_txt = linha.split(';')[0]
        senha_txt = linha.split(';')[1].split(';')[0]
        
        if usuario == usuario_txt and senha == senha_txt:
            cliente_id = linha.split(';')[2].split(';')[0]

    return cliente_id 
    

def menu():
    print('[1] - Cadastrar')
    print('[2] - Login')

def registro():
    opcao = -1
    while opcao != 3:
        menu()
        opcao = int(input('\nDigite uma opção: '))
        
        if opcao == 1:
            os.system('cls')
            print('Área de cadastro de novo usuário')
            usuario = input('\nDigite o usuário: ').strip()
            senha = input('Digite a senha: ').strip()
            
            if verificar_usuario(usuario):
                os.system('cls')
                print('Usuário já cadastrado!\n')
            
            else:
                cadastrar(usuario,senha)
                os.system('cls')
                print('Usuário cadastrado com sucesso!\n')
                
        elif opcao == 2:
            os.system('cls')

            print('Área de login')
            usuario = input('\nDigite o usuário: ').strip()
            senha = input('Digite a senha: ').strip()
            
            if login(usuario,senha):
                os.system('cls')
                print('Login efetuado com sucesso!\n')
                opcao = 3
            
            else:
                os.system('cls')
                print('Usuário ou senha inválidos!\n')
        else:
            os.system('cls')
            print('Opção inválida!\n')

    cliente_id = acessar_client_id(usuario, senha)

    return usuario, cliente_id
