    #Criar um banco de daos SQLite e uma tabela
import sqlite3

#Criar a conexão com o banco de dados chamando de "escola.db"
conexao = sqlite3.connect("escola.db")

#Criar o objeto chamando de "cursor" que será usado para excutar os comandos sql
cursor = conexao.cursor()

#Criar uma tabela no banco 
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,           
    nome TEXT NOT NULL,
    idade INTEGER, 
    curso TEXT
    )          
""")