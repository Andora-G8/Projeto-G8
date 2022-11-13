import random

def gerar_pin_id():
    pin_id = ''
    for i in range(0,5):
        pin_id += str(random.randint(0,5))
    return pin_id

def cadastrar(usuario,senha):
    arq = open('H:\Arquivos\Programação\Python\Projetos - G8 [2022.2]\cadastro.txt', 'a')
    pin = gerar_pin_id()
    arq.write(f'{usuario};{senha};{pin}\n')
    arq.close()

def login(usuario,senha):
    arq = open('H:\Arquivos\Programação\Python\Projetos - G8 [2022.2]\cadastro.txt', 'r')
    for linha in arq:
        linha = linha.strip()
        usuario_txt = linha.split(';')[0]
        senha_txt = linha.split(';')[1].split(';')[0]
        if usuario == usuario_txt and senha == senha_txt:
            return True
    return False

def verificar_usuario(usuario):
    arq = open('H:\Arquivos\Programação\Python\Projetos - G8 [2022.2]\cadastro.txt', 'r')
    for linha in arq:
        if usuario in linha:
            return True
    return False

def menu():
    print('[1] - Cadastrar')
    print('[2] - Login')

def registro():
    opcao = -1
    while opcao != 3:
        menu()
        opcao = int(input('Digite uma opção: '))
        if opcao == 1:
            usuario = input('Digite o usuário: ')
            senha = input('Digite a senha: ')
            if verificar_usuario(usuario):
                print('Usuário já cadastrado!')
            else:
                cadastrar(usuario,senha)
                print('Usuário cadastrado com sucesso!')
        elif opcao == 2:
            usuario = input('Digite o usuário: ')
            senha = input('Digite a senha: ')
            if login(usuario,senha):
                print('Login efetuado com sucesso!')
                opcao = 3
            else:
                print('Usuário ou senha inválidos!')
        else:
            print('Opção inválida!')
