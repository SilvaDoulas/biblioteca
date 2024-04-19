from tkinter import *
from tkinter import messagebox
from usuario import *
from bd import *
from conexao import *


def inicio():
    #Criar nossa janela
    jan = Tk()
    jan.title("Biblioteca BGD²")
    jan.geometry("1200x600")
    #======Widgets==============
    Leftframe = Frame(jan, width=600, height=1200, bg="MIDNIGHTBLUE", relief="raise")
    Leftframe.pack(side=LEFT)

    Rightframe = Frame(jan, width=1000, height=1200, bg="MIDNIGHTBLUE", relief="raise")
    Rightframe.pack(side=RIGHT)

    label_inicial = Label(Rightframe, text="Bem vindo a Biblioteca!", font=("Century Gothic", 25), bg="MIDNIGHTBLUE", fg="white")
    label_inicial.place(x=1, y=250)

    #Botões
    LoginButton = Button(Rightframe, text="Login", width=30, command= Telas_Usuario.login_user)
    LoginButton.place(x=90, y=350)

    RegiButton = Button(Rightframe, text="Registrar", width=30, command= Telas_Usuario.cadastrar_user)
    RegiButton.place(x=90, y=385)

    jan.mainloop()

def menu_opcoes():
      #Criar nossa janela
    jan = Tk()
    jan.title("Biblioteca BGD²")
    jan.geometry("1200x600")
    #======Widgets==============
    Leftframe = Frame(jan, width=600, height=1200, bg="MIDNIGHTBLUE", relief="raise")
    Leftframe.pack(side=LEFT)

    Rightframe = Frame(jan, width=1000, height=1200, bg="MIDNIGHTBLUE", relief="raise")
    Rightframe.pack(side=RIGHT)

    label_inicial = Label(Rightframe, text="Biblioteca BGD²", font=("Century Gothic", 25), bg="MIDNIGHTBLUE", fg="white")
    label_inicial.place(x=1, y=200)

    #Botões
    CadastroButton = Button(Rightframe, text="Cadastrar Livro", width=30, command= Telas_Livro.cadastrar_livro)
    CadastroButton.place(x=90, y=300)

    AtualizarButton = Button(Rightframe, text="Atualizar Livro", width=30, command= Telas_Livro.autualizar_livro)
    AtualizarButton.place(x=90, y=340)

    AcervoButton = Button(Rightframe, text="Mostrar Acervo", width=30, command= Telas_Livro.listagem_livro)
    AcervoButton.place(x=90, y=380)

    EmprestimoButton = Button(Rightframe, text="Emprestrar Livro", width=30, command= Telas_Livro.emprestar_livro)
    EmprestimoButton.place(x=90, y=420)

    DevolverButton = Button(Rightframe, text="Devolver Livro", width=30, command= Telas_Livro.devolver_livro)
    DevolverButton.place(x=90, y=460)

    jan.mainloop()

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
            if insert:
                messagebox.showinfo("Cadastro Livro", "Cadastro do livro bem-sucedido!")
                
            

        btn_Cadastrar = Button(root, text='Cadastrar Livro', command=registrar_livro)
        btn_Cadastrar.grid(row=3, columnspan=2, padx=5, pady=5)
        btn_voltar = Button(root, text='Voltar', command= menu_opcoes )
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
            if update:
                messagebox.showinfo("Atualização de Livro", "Atualização do livro bem-sucedido!")
            else:
                messagebox.showerror("Atualizar Livro", "Não foi possivel fazer a acão!")

        botao_atualizar = Button(tela, text='Atualizar Livro', command= registrar_atualizacao)
        botao_atualizar.grid(column=1, row=4)
        btn_voltar = Button(tela, text='Voltar', command= menu_opcoes )
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
            tl2 = entrada_titulo.get()
            to_lend2(mydb, tl2)
            if to_lend2:
                messagebox.showinfo("Emprestrar Livro", "Empréstimo bem-sucedido!")
            else:
                messagebox.showerror("Devolver Livro", "Não foi possivel fazer a acão!")
            
        botao_emprestar = Button(tela, text='Emprestar Livro', command= registrar_emprestimo)
        botao_emprestar.grid(column=1, row=1)
        btn_voltar = Button(tela, text='Voltar', command= menu_opcoes)
        btn_voltar.grid(row= 4, columnspan=3, padx= 6, pady=6 )
        tela.mainloop()
        mydb.close()

    def devolver_livro():
        mydb = connect()
        tela = Tk()
        tela.title('Devolver Livro')

        label_titulo = Label(tela, text='Digite o Titulo do Livro: ')
        label_titulo.grid(column=0, row=0)
        entrada_titulo = Entry(tela)
        entrada_titulo.grid(column=1, row=0)

        def registrar_devolucao():
            tl = []
            tl.append(entrada_titulo.get())
            give_back2(mydb, tl)
            if give_back2:
                messagebox.showinfo("Devolver Livro", "Devoluçao bem-sucedida!")
            else:
                messagebox.showerror("Devolver Livro", "Não foi possivel fazer a acão!")
        
        botao_devolver = Button(tela, text='Devolver Livro', command= registrar_devolucao)
        botao_devolver.grid(column=1, row=2)
        btn_voltar = Button(tela, text='Voltar', command= menu_opcoes)
        btn_voltar.grid(row= 4, columnspan=3, padx= 6, pady=6 )
        tela.mainloop()
        mydb.close()

    def listagem_livro():
        mydb = connect()
    
        lista_window = Tk()
        lista_window.title('Lista de Livros')

        Label_header = Label(lista_window, text = 'Título\tAutor\tAno')
        Label_header.pack()
        query(mydb= Label_header)
        

        Root = Tk()
        Root.title('Listagem de Livros')

        btn_listar = Button(Root, text='Mostrar Listagem', command=query)
        btn_listar.grid(padx=10, pady=10)

        mydb.close()
        Root.mainloop()
    

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
            if register:
                messagebox.showinfo("Cadastro", "Cadastro bem-sucedido!")
                messagebox.showinfo("", "Faça login para acessar nosso sistema!")
        
        botao_cadastrar = Button(tela, text='Cadastrar', command= registro_user)
        botao_cadastrar.grid(column= 1, row= 12)
        tela.mainloop()
        mydb.close()
    
    def login_user():
        mydb = connect()
        tela = Tk()
        tela.title('Login')

        label_email = Label(tela, text='Digite seu email: ')
        label_email.grid (column=0, row=0)
        entrada_email = Entry(tela)
        entrada_email.grid (column=1, row=0)

        label_senha = Label(tela, text='Digite sua senha: ')
        label_senha.grid(column=0, row=1)
        entrada_senha = Entry(tela, show='*')
        entrada_senha.grid(column=1, row=1)

        def registrar_login():
            em = entrada_email.get()
            sen = entrada_senha.get()
            login(mydb, em, sen)

            if login:
                messagebox.showinfo('Login', 'Usuário aceito')
                menu_opcoes()
             
            else:
                messagebox.showerror("Login", "Usuário ou senha incorretos!")
                

       
        botao_login = Button(tela, text='Login', command=registrar_login)
        botao_login.grid (column=1, row= 2)
        tela.mainloop()
        mydb.close()

