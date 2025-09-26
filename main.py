    #Criar um banco de daos SQLite e uma tabela
import sqlite3

#Criar a conexão com o banco de dados chamando de "escola.db"
conexao = sqlite3.connect("escola.db")

#Criar o objeto chamando de "cursor" que será usado para excutar os comandos sql
cursor = conexao.cursor()

# #Criar uma tabela no banco 
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS alunos (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,           
#     nome TEXT NOT NULL,
#     idade INTEGER, 
#     curso TEXT
#     )          
# """)
# nome = input("Digite o nome do aluno?: ").lower()
# idade = int(input("Digite a idade do aluno: "))
# curso = input("Digite o curso do aluno: ").lower()
# #Inserir um dado na tabela
# cursor.execute("""
# INSERT INTO alunos (nome, idade, curso)
# VALUES (?, ?, ?)
# """,
# (nome, idade, curso)
# )


# #Confirmar as alterações no banco
# conexao.commit()

#Inserir varios alunos de uma só vez
alunos = [
    ("yago", 28, "Diretor"),
    ("Jessica", 24, "Computação"),
    ("Breno", 52, "Computação"),
]
#executamany permite inserir múltiplas linhas de uma vez só
cursor.executemany("""
INSERT INTO alunos (nome, idade, curso)                
VALUES (?, ?, ?)
""",
(alunos)
)
conexao.commit()