from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.message import Message
# from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from agno.playground import Playground
from dotenv import load_dotenv
import sqlite3

load_dotenv()

model = OpenAIChat(id="gpt-4.1-mini")

# conectando o banco 

# criar banco
def criar_tabela(nome_tabela, campos):
    """
    Este código define uma função chamada criar_tabela que cria uma tabela em um banco de dados SQLite chamado 'exemplo.db'.

    1. A função recebe dois parâmetros:
    - nome_tabela: o nome da tabela que será criada.
    - campos: uma lista de strings que descrevem os campos e seus tipos (ex: ["id INTEGER PRIMARY KEY", "nome TEXT NOT NULL"]).

    2. Primeiro, o código conecta ao banco de dados 'exemplo.db'.
    Se o arquivo não existir, o SQLite cria um automaticamente.

    3. Depois, cria um cursor, que é o objeto usado para executar comandos SQL no banco.

    4. Em seguida, transforma a lista de campos em uma única string, separada por vírgulas.
    Exemplo: ["id INTEGER", "nome TEXT"] → "id INTEGER, nome TEXT".

    5. Monta o comando SQL:
    "CREATE TABLE IF NOT EXISTS <nome_tabela> (<campos>)"
    Isso garante que a tabela só será criada se ainda não existir.

    6. Executa o comando SQL no banco, confirma as mudanças (commit) e fecha a conexão.
    """
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()
    
    campos_str = ", ".join(campos)
    comando = f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({campos_str})"
    
    cursor.execute(comando)
    conexao.commit()
    conexao.close()


# adicionar usuario
def adicionar_usuario(nome, idade):
    """
    Esta função adiciona um novo usuário na tabela 'usuarios' do banco de dados SQLite chamado 'exemplo.db'.

    1. A função recebe dois parâmetros:
    - nome: o nome do usuário (string).
    - idade: a idade do usuário (inteiro).

    2. Primeiro, conecta ao banco de dados 'exemplo.db'.
    Se o arquivo não existir, o SQLite cria automaticamente.

    3. Cria um cursor, que é usado para executar comandos SQL no banco.

    4. Monta o comando SQL de inserção:
       "INSERT INTO usuarios (nome, idade) VALUES (?, ?)"
       Os "?" são *placeholders* para evitar SQL Injection.
       Os valores reais são passados separadamente como parâmetros.

    5. Executa o comando passando o nome e a idade do usuário.

    6. Confirma as mudanças no banco (commit) e fecha a conexão.
    """
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()

    comando = "INSERT INTO usuarios (nome, idade) VALUES (?, ?)"
    cursor.execute(comando, (nome, idade))

    conexao.commit()
    conexao.close()

# atualizar usuario 
def atualizar_usuario(id_usuario, novo_nome, nova_idade):
    """
    Esta função atualiza os dados de um usuário existente na tabela 'usuarios' do banco de dados SQLite chamado 'exemplo.db'.

    1. A função recebe três parâmetros:
    - id_usuario: o ID do usuário que será atualizado (inteiro).
    - novo_nome: o novo nome que substituirá o antigo (string).
    - nova_idade: a nova idade que substituirá a antiga (inteiro).

    2. Primeiro, conecta ao banco de dados 'exemplo.db'.

    3. Cria um cursor, usado para executar comandos SQL no banco.

    4. Monta o comando SQL de atualização:
       "UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?"
       Os "?" são placeholders para evitar SQL Injection.

    5. Executa o comando passando os novos valores e o ID do usuário.

    6. Confirma as mudanças no banco (commit) e fecha a conexão.
    """
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()

    comando = "UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?"
    cursor.execute(comando, (novo_nome, nova_idade, id_usuario))

    conexao.commit()
    conexao.close()


# listar usuario
def listar_usuarios():
    """
    Esta função recupera e retorna todos os usuários da tabela 'usuarios' 
    no banco de dados SQLite chamado 'exemplo.db'.

    1. Não recebe parâmetros, pois lista todos os usuários cadastrados.

    2. Conecta ao banco de dados 'exemplo.db'.

    3. Cria um cursor, que é usado para executar comandos SQL.

    4. Monta o comando SQL de consulta:
       "SELECT * FROM usuarios"
       Isso retorna todas as linhas da tabela.

    5. Executa o comando e armazena os resultados usando fetchall().

    6. Fecha a conexão com o banco.

    7. Retorna a lista de usuários, onde cada item é uma tupla no formato:
       (id, nome, idade).
    """
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()

    comando = "SELECT * FROM usuarios"
    cursor.execute(comando)

    usuarios = cursor.fetchall()

    conexao.close()
    return usuarios


# deletar usuario 
def deletar_usuario(id_usuario):
    """
    Esta função remove um usuário específico da tabela 'usuarios' 
    no banco de dados SQLite chamado 'exemplo.db'.

    1. A função recebe um parâmetro:
    - id_usuario: o ID do usuário que será deletado (inteiro).

    2. Conecta ao banco de dados 'exemplo.db'.

    3. Cria um cursor, usado para executar comandos SQL.

    4. Monta o comando SQL de exclusão:
       "DELETE FROM usuarios WHERE id = ?"
       O "?" é um placeholder para evitar SQL Injection.

    5. Executa o comando passando o ID do usuário como parâmetro.

    6. Confirma as mudanças no banco (commit) e fecha a conexão.

    7. O usuário com o ID informado será removido da tabela, 
       se existir.
    """
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()

    comando = "DELETE FROM usuarios WHERE id = ?"
    cursor.execute(comando, (id_usuario,))

    conexao.commit()
    conexao.close()





agent = Agent(
    model= model,
    tools= [
        criar_tabela,
        adicionar_usuario,
        atualizar_usuario,
        listar_usuarios,
        deletar_usuario,
        TavilyTools()],
    instructions="responda em português, seja direto, fale como se falasse com uma criança, seja assertivo, sempre mostre os dados em uma tabela",
    debug_mode = True
)

playground_app = Playground(
    agents=[agent]
)

app = playground_app.get_app()

if __name__ == "__main__":
    playground_app.serve("5_Codigo_GPT_TCC:app", reload=True)