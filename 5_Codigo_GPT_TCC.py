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

def inserir_dados(nome_tabela, dados):
    """
    Insere dados em uma tabela do banco SQLite 'exemplo.db'.

    Parâmetros:
    - nome_tabela: nome da tabela onde os dados serão inseridos.
    - dados: dicionário com chave=nome do campo e valor=valor a ser inserido.

    Exemplo:
    inserir_dados("usuarios", {"nome": "João", "idade": 25, "email": "joao@email.com"})
    """
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()

    colunas = ', '.join(dados.keys())  # "nome, idade, email"
    placeholders = ', '.join(['?' for _ in dados])  # "?, ?, ?"
    valores = tuple(dados.values())  # ("João", 25, "joao@email.com")

    comando = f"INSERT INTO {nome_tabela} ({colunas}) VALUES ({placeholders})"
    
    cursor.execute(comando, valores)
    conexao.commit()
    conexao.close()

def atualizar_registros(nome_tabela, condicoes, novos_dados):
    """
    Atualiza um ou mais registros em uma tabela SQLite com base em condições.

    Parâmetros:
    - nome_tabela: nome da tabela no banco.
    - condicoes: dicionário com os critérios de seleção (ex: {"id": 1}).
    - novos_dados: dicionário com os campos a serem atualizados e seus novos valores.

    Exemplo:
    atualizar_registros("usuarios", {"id": 1}, {"nome": "Novo Nome", "idade": 30})
    """
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()

    # Monta parte do SET
    set_str = ', '.join([f"{campo} = ?" for campo in novos_dados])
    valores = list(novos_dados.values())

    # Monta parte do WHERE
    where_str = ' AND '.join([f"{campo} = ?" for campo in condicoes])
    valores += list(condicoes.values())

    comando = f"UPDATE {nome_tabela} SET {set_str} WHERE {where_str}"

    cursor.execute(comando, valores)
    conexao.commit()
    conexao.close()
    
def excluir_registros(nome_tabela, condicoes):
    """
    Exclui registros de uma tabela SQLite com base em condições.

    Parâmetros:
    - nome_tabela: nome da tabela.
    - condicoes: dicionário com os critérios de exclusão (ex: {"id": 2}).

    Exemplo:
    excluir_registros("usuarios", {"id": 2})
    """
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()

    where_str = ' AND '.join([f"{campo} = ?" for campo in condicoes])
    valores = list(condicoes.values())

    comando = f"DELETE FROM {nome_tabela} WHERE {where_str}"

    cursor.execute(comando, valores)
    conexao.commit()
    conexao.close()

def listar_registros(nome_tabela, campos='*', condicoes=None):
    """
    Lista registros de uma tabela SQLite com campos e condições opcionais.

    Parâmetros:
    - nome_tabela: nome da tabela no banco de dados.
    - campos: lista com os nomes dos campos a selecionar (ex: ["nome", "idade"]) ou "*" para todos.
    - condicoes: dicionário com condições do WHERE (ex: {"idade": 25}) ou None para nenhuma condição.

    Retorna:
    - Lista de tuplas com os registros encontrados.
    
    Exemplo:
    listar_registros("usuarios")  # Lista todos os campos de todos os usuários
    listar_registros("usuarios", campos=["nome"])  # Lista só os nomes
    listar_registros("usuarios", campos=["nome", "idade"], condicoes={"idade": 30})  # Filtra por idade
    """
    conexao = sqlite3.connect('exemplo.db')
    cursor = conexao.cursor()

    # Define os campos a selecionar
    if isinstance(campos, list):
        campos_str = ", ".join(campos)
    else:
        campos_str = campos  # Assume que já é "*"

    comando = f"SELECT {campos_str} FROM {nome_tabela}"

    valores = []
    if condicoes:
        clausulas = [f"{campo} = ?" for campo in condicoes]
        comando += " WHERE " + " AND ".join(clausulas)
        valores = list(condicoes.values())

    cursor.execute(comando, valores)
    resultados = cursor.fetchall()

    conexao.close()
    return resultados

agent = Agent(
    model= model,
    tools= [
        criar_tabela,
        inserir_dados,
        atualizar_registros,
        excluir_registros,
        listar_registros,
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