from tkinter import *
from usuario import *
from bd import *
from conexao import *
from tela_inicial import *

class Telas_Livro:

    def cadastrar_livro():
        mydb = connect() 
        root = Tk()
        root.title('Cadastro de Livros')

        label_titulo = Label(root, text='Título:')
        label_titulo.grid(row=0, column=0, padx=5, pady=5)
        Entry_titulo = Entry(root)
        Entry_titulo.grid(row=0, column=1, padx=5, pady=5)

        label_autor = Label(root, text='Autor da Obra: ')
        label_autor.grid(row=1, column=0, padx=5, pady=5)
        Entry_autor = Entry(root)
        Entry_autor.grid(row=1, column=1, padx=5, pady=5)

        label_ano = Label(root, text='Ano: ')
        label_ano.grid(row=2, column=0, padx=5, pady=5)
        Entry_ano = Entry(root)
        Entry_ano.grid(row=2, column=1, padx=5, pady=5)

       
        def registrar_livro():
            t = Entry_titulo.get()
            au = Entry_autor.get()
            an = Entry_ano.get()
            d = 1
            insert(mydb, t, au, an, d)
        
        def limpar():
            Entry_titulo
        

        btn_Cadastrar = Button(root, text='Cadastrar Livro', command=registrar_livro)
        btn_Cadastrar.grid(row=3, columnspan=2, padx=5, pady=5)
        btn_voltar = Button(root, text='Voltar', command= Men )
        btn_voltar.grid(row= 4, columnspan=3, padx= 6, pady=6 )
        root.mainloop()
        mydb.close()
    
    def autualizar_livro():
        mydb = connect()
        tela = Tk()
        tela.title('Atualizar Livro')

        label_titulo_antigo = Label(tela, text='Digite o Titulo Antigo: ')
        label_titulo_antigo.grid(column=0, row=0)
        entrada_titulo_antigo = Entry(tela)
        entrada_titulo_antigo.grid(column=1, row=0)

        label_titulo_novo = Label(tela, text='Digite o Titulo Novo: ')
        label_titulo_novo.grid(column=0, row=1)
        entrada_titulo_novo = Entry(tela)
        entrada_titulo_novo.grid(column=1, row= 1)

        label_autor = Label(tela, text='Digite o Autor Novo: ')
        label_autor.grid(column=0, row=2)
        entrada_autor = Entry(tela)
        entrada_autor.grid(column=1, row=2)

        label_ano = Label(tela, text='Digite o Ano: ')
        label_ano.grid(column=0, row=3)
        entrada_ano = Entry(tela)
        entrada_ano.grid(column=1, row=3)

        def registrar_atualizacao():
            ta = entrada_titulo_antigo.get()
            tn = entrada_titulo_novo.get()
            au = entrada_autor.get()
            an = entrada_ano.get()
            d = 1
            update(mydb, ta, tn, au, an, d)

        botao_atualizar = Button(tela, text='Atualizar Livro', command= registrar_atualizacao)
        botao_atualizar.grid(column=1, row=4)
        btn_voltar = Button(tela, text='Voltar', command= Men )
        btn_voltar.grid(row= 4, columnspan=3, padx= 6, pady=6 )
        tela.mainloop()
        mydb.close()

    def emprestar_livro():
        mydb= connect()
        tela = Tk()
        tela.title('Emprestar Livro')

        label_titulo = Label(tela, text='Digite o Titulo do Livro: ')
        label_titulo.grid(column=0, row=0)
        entrada_titulo = Entry(tela)
        entrada_titulo.grid(column=1, row=0)

        def registrar_emprestimo():
            t = entrada_titulo.get()
            to_lend2(mydb, t)
            
        botao_emprestar = Button(tela, text='Emprestar Livro', command= registrar_emprestimo)
        botao_emprestar.grid(column=1, row=1)
        btn_voltar = Button(tela, text='Voltar', command= Men )
        btn_voltar.grid(row= 4, columnspan=3, padx= 6, pady=6 )
        tela.mainloop()
        mydb.close()

    def devolver_livro():
        mydb = connect()
        tela = Tk()
        tela.title('Devolver Livro')

        
    

class Telas_Usuario:
    def cadastrar_user():
        mydb = connect()
        tela = Tk()
        tela.title('Cadastro de Usuário da Biblioteca')
        nome = Label(tela, text='Nome Completo: ')
        nome.grid (column=0, row= 0)
        entrada_nome = Entry(tela)
        entrada_nome.grid (column= 1, row= 0)
        

        email = Label(tela, text='Email: ')
        email.grid (column=0, row= 1)
        entrada_email = Entry(tela)
        entrada_email.grid (column=1, row= 1)

        senha = Label(tela, text='Senha: ')
        senha.grid (column=0, row= 2)
        entrada_senha = Entry(tela, show='*')
        entrada_senha.grid (column=1, row= 2)

        nascimento = Label(tela, text='Data de Nascimento: ')
        nascimento.grid (column=0, row= 3)
        entrada_nascimento = Entry(tela)
        entrada_nascimento.grid (column=1, row= 3)

        rua = Label(tela, text='Rua: ')
        rua.grid (column=0, row= 4)
        entrada_rua = Entry(tela)
        entrada_rua.grid (column=1, row= 4)

        bairro = Label(tela, text='Bairro: ')
        bairro.grid (column=0, row= 5)
        entrada_bairro = Entry(tela)
        entrada_bairro.grid (column=1, row= 5)

        cidade  = Label(tela, text='Cidade: ')
        cidade.grid (column=0, row= 6)
        entrada_cidade = Entry(tela)
        entrada_cidade.grid (column=1, row= 6)

        estado  = Label(tela, text='Estado (Digite a sigla): ')
        estado.grid (column=0, row= 7)
        entrada_estado = Entry(tela)
        entrada_estado.grid (column=1, row= 7)

        CEP = Label(tela, text='CEP: ')
        CEP.grid (column=0, row= 8)
        entrada_CEP = Entry(tela)
        entrada_CEP.grid (column=1, row= 8)

        def registro_user():
            n = entrada_nome.get()
            em = entrada_email.get()
            s = entrada_senha.get()
            nas = entrada_nascimento.get()
            r = entrada_rua.get()
            b = entrada_bairro.get()
            c = entrada_cidade.get()
            es = entrada_estado.get()
            cpe = entrada_CEP.get()
            register(mydb, n, em, s, nas,  r, b, c, es, cpe)
        
        botao_login = Button(tela, text='Cadastrar', command= registro_user)
        botao_login.grid(column= 1, row= 12)


        tela.mainloop()
        mydb.close()
