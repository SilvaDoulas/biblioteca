from conexao import connect
from bd import insert, update, delete, query, register, login, to_lend, give_back
from livro import Livro
from datetime import datetime
from usuario import Usuario

# Conectar ao banco de dados
mydb = connect()

print("Bem-vindo à Biblioteca")

while True:
    print("\nSelecione a operação desejada:")
    print("1. Registrar usuário")
    print("2. Fazer login")
    print("3. Inserir livro")
    print("4. Atualizar livro")
    print("5. Excluir livro")
    print("6. Consultar livros")
    print("7. Emprestar livro")
    print("8. Devolver livro")
    print("9. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input('Digite o Nome: ')
        email = input('Digite o Email: ')
        senha = input('Digite a Senha: ')
        data_nascimento = input('Digite a Data de Nascimento (DD/MM/YYYY): ')
        # Converter a string de data para um objeto datetime
        data_nascimento_obj = datetime.strptime(data_nascimento, '%d/%m/%Y')
        # Formatar a data no formato MySQL
        data_nascimento_formatada = data_nascimento_obj.strftime('%Y-%m-%d')
        rua = input('Digite a Rua: ')
        bairro = input('Digite o Bairro: ')
        cidade = input('Digite a Cidade: ')
        estado = input('Digite o Estado: ')
        cep = input('Digite o CEP: ')
        
        user = Usuario(nome, email, senha, data_nascimento, rua, bairro, cidade, estado, cep)

        register(mydb, user.nome, user.email, user.senha, user.data_nascimento,
                 user.rua, user.bairro, user.cidade, user.estado, user.cep)

    elif opcao == "2":
        email = input('Digite o Email: ')
        senha = input('Digite a Senha: ')

        user = login(mydb, email, senha)

    elif opcao == "3":
        titulo = input('Digite o Título: ')
        autor = input('Digite o Autor: ')
        ano = input('Digite o Ano: ')
        status_ = input(
            'Digite o Status (1 para Disponível, 0 para Indisponível): ')

        l = Livro(titulo, autor, ano)
        insert(mydb, l.titulo, l.autor, l.ano, status_)

    elif opcao == "4":
        titulo_antigo = input(
            'Digite o título do livro que deseja atualizar: ')
        titulo_novo = input('Digite o novo título: ')
        autor = input('Digite o novo autor: ')
        ano = input('Digite o novo ano: ')
        status_ = input(
            'Digite o novo status (1 para Disponível, 0 para Indisponível): ')

        update(mydb, titulo_antigo, titulo_novo, autor, ano, status_)

    elif opcao == "5":
        titulo = input('Digite o título do livro que deseja excluir: ')
        delete(mydb, titulo)

    elif opcao == "6":
        query(mydb)

    elif opcao == "7":
        if 'user' not in locals():
            print("Você precisa fazer login para emprestar um livro.")
            continue

        titulo = input('Digite o título do livro que deseja emprestar: ')
        to_lend(mydb, user, titulo)
    elif opcao == "8":
        if 'user' not in locals():
            print("Você precisa fazer login para devolver um livro.")
            continue

        titulo = input('Digite o título do livro que deseja devolver: ')
        give_back(mydb, user, titulo)


    elif opcao == "9":
        break

    else:
        print("Opção inválida!")

# Fechar a conexão com o banco de dados
mydb.close()
