from conexao import connect
from bd import insert, update, delete, query, register, login, to_lend, give_back
from livro import Livro
from datetime import datetime
from usuario import Usuario
from comando_telas import *

# Conectar ao banco de dados
mydb = connect()
inicio()
# Fechar a conexão com o banco de dados
mydb.close()
