import mysql.connector

# CRIANDO CONEXÃO COM O BANCO DE DADOS

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='database'
)

cursor = conexao.cursor()

def criarConta():
    print("Você Escolheu Criar Uma Conta")
    print("-"*60)

    nome = input("Insira Seu Nome: ")
    email= input("Insira Seu Email: ")
    senha= input("Insira Sua Senha: ")
    print("-"*60)
    if "@" not in email:
        print("INSIRA UM EMAIL VÁLIDO")
        print("-"*60)
        criarConta()
    else:
        comando = f'SELECT * FROM login'
        cursor.execute(comando)
        varredura = cursor.fetchall()
        comando2 = f'SELECT MAX(id) as maxId FROM login'
        cursor.execute(comando2)
        num_id_str = cursor.fetchall()
        num_id_int = (num_id_str[0][0])

        for id in range(num_id_int):
            email_bd = (varredura[id][2])
            if (email_bd == email):
                print("Email Já Utilizado, Tente Com Outro")
                criarConta()
                break
        else:
            comando = f'INSERT INTO login (nome,email,senha) VALUES ("{nome}","{email}","{senha}")'
            cursor.execute(comando)
            conexao.commit()            
            print("Conta Criada! Se Deseja Logar Digite 1")
            retorno = int(input())
            print("-"*60)
            if retorno == 1:
                loginConta()

def loginConta():
    print("Você Escolheu Fazer Login")
    print("-"*60)

    email = input("Insira Seu Email: ")
    senha = input("Insira Sua Senha: ")
    print("-"*60)

    comando = f'SELECT * FROM login'
    cursor.execute(comando)
    varredura = cursor.fetchall()
    comando2 = f'SELECT MAX(id) as maxId FROM login'
    cursor.execute(comando2)
    num_id_str = cursor.fetchall()

    num_id_int = (num_id_str[0][0])

    for id in range(num_id_int):
        email_bd = (varredura[id][2])
        senha_bd = (varredura[id][3])
        if (email_bd == email) and (senha_bd == senha):
            print("Bem Vindo")
            print("-"*60)
            break
    else:
        print("Conta Não Encontrada, Digite 1 Para Tentar Novamente")
        retorno = int(input())
        print("-"*60)
        if retorno == 1:
            loginConta()

# INICIO

print("-"*60)
print("Olá Seja Bem-Vindo")
print("-"*60)
print("Digite 1 Para Fazer Login")
print("Digite 2 Para Criar Uma Conta")
print("-"*60)
escolha = int(input())

if escolha == 1:
    loginConta()

elif escolha == 2:
    criarConta()

else:
    print("Por Favor, Escolha Uma Opção Válida")
    print("-"*60)

# FECHANDO A CONEXÃO

cursor.close()
conexao.close()