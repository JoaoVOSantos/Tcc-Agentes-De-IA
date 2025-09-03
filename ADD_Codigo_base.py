
#--------------------------- sqllite3 -----------------------
import sqlite3

def criar_tabela():
    conexao = sqlite3.connect('tccagenteia.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY NOT NULL,
                    nome TEXT NOT NULL,
                    idade INTEGER )''')
    conexao.commit()
    conexao.close()
    
def adicionar_usuario(nome, idade):
    conexao = sqlite3.connect('tccagenteia.db')
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO usuarios (nome, idade) VALUES (?, ?)''', (nome, idade))
    conexao.commit()
    conexao.close()
    
def deletar_usuario(id):
    conexao = sqlite3.connect('tccagenteia.db')
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM usuarios WHERE id = ?''', (id,))
    conexao.commit()
    conexao.close()
    
def listar_usuarios():
    conexao = sqlite3.connect('tccagenteia.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM usuarios''')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()
    
def atualizar_usuario(id, nome, idade):
    conexao = sqlite3.connect('tccagenteia.db')
    cursor = conexao.cursor()
    cursor.execute('''UPDATE usuarios SET nome = ?, idade = ? WHERE id = ? ''', (nome, idade, id))
    conexao.commit()
    conexao.close()
    
def listar_usuarios_idade(idade):
    conexao = sqlite3.connect('tccagenteia.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM usuarios WHERE idade <= ? ''',(idade,))
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()
    
    
def menu():
    print("\n1. Adicionar usuario")
    print("\n2. Listar usuario")
    print("\n3. Atualizar usuario")
    print("\n4. Deletar usuario")
    print("\n5. Atividade 01")
    print("\n6. Sair")
    
criar_tabela()

while True:
    menu()
    escolha = input("Escolha uma opção: ")
    if escolha ==  '1':
        nome = input("Digite o nome de usuario: ")
        idade = int(input("Digite a idade do usuario: "))
        adicionar_usuario(nome, idade)
        print("Usuario cadastrado com sucesso")
    elif escolha == '2':
        print("\n Todos os usuarios")
        listar_usuarios()
    elif escolha == '3':
        id = int(input("Digite o ID do usuario a ser atualizade: "))
        nome = input("Digite o novo nome de usuario: ")
        idade = int(input("Digite a nova idade do usuario: "))
        atualizar_usuario(id, nome, idade)
        print("Usuario atualizado com sucesso")
    elif escolha == '4':
        id = int(input("Digite o ID do usuario a ser deletado: "))
        deletar_usuario(id)
        print("Usuario deletado com sucesso")
    elif escolha == '5':
        idade = int(input("Digite a idade que queira listar usuarios com idades menores: "))
        listar_usuarios_idade(idade)
    elif escolha == '6':
        print("Saindo do programa...")
        break
    else:
        print("Opção invalida. Por favor, escolha uma opção valida.")
        

#--------------------------- mysqliconnector -----------------------

import mysql.connector

# Função para criar a tabela
def criar_tabela():
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="tccagenteia")
    cursor = conexao.cursor()
    conexao.commit()
    conexao.close()

def adicionar_usuario(nome, email, fone):
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="tccagenteia")
    cursor = conexao.cursor()
    sql = "INSERT INTO pessoas (nome, email, fone) VALUES (%s, %s, %s)"
    val = (nome, email, fone)
    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()
    
def listar_usuario():
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="tccagenteia")
    cursor = conexao.cursor()
    sql = "SELECT * from pessoas"
    cursor.execute(sql)
    pessoas = cursor.fetchall()
    for pessoa in pessoas:
        print(pessoa)
    conexao.commit()
    conexao.close()
    
def atualizar_usuario(id, nome, email, fone):
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="tccagenteia")
    cursor = conexao.cursor()
    
    sql = "UPDATE pessoas SET nome = %s, email = %s, fone = %s WHERE id = %s"
    val = (nome, email, fone, id)
    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()
    
def deletar_usuario(id):
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="tccagenteia")
    cursor = conexao.cursor()
    
    sql = "DELETE FROM pessoas WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()


def menu():
    print("\n1. Adicionar usuário")
    print("2. Listar usuários")
    print("3. Atualizar usuário")
    print("4. Deletar usuário")
    print("5. Sair")

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        fone = input("Digite o fone do usuário: ")
        adicionar_usuario(nome, email, fone)
        print("Usuário adicionado com sucesso!")


    elif escolha == '2':
        print("\n Todos os usuarios")
        listar_usuario()
        
    elif escolha == '3':
        id = int(input("Digite o ID do usuario a ser atualizade: "))
        nome = input("Digite o novo nome de usuario: ")
        email = input("Digite o novo email do usuario: ")
        telefone = input("Digite o novo telefone do usuario: ")
        atualizar_usuario(id, nome, email, telefone)
        print("Usuario atualizado com sucesso")
        
    elif escolha == '4':
        id = int(input("Digite o ID do usuario a ser deletado: "))
        deletar_usuario(id)
        print("Usuario deletado com sucesso")
    
    elif escolha == '5':
        print("Saindo do programa...")
        break