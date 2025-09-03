from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.message import Message
# from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from agno.playground import Playground
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

model = OpenAIChat(id="gpt-4.1-mini")

# com problema acredito que seja pq ele tenta se conectar, porem o codigo dele nao esta rodando na minha maquina.
# def conectar():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="tccagenteia"
#     )
    
# def executar_sql(sql, fetch=False):
#     conexao = conectar()
#     cursor = conexao.cursor()
#     cursor.execute(sql)
#     resultado = None
#     if fetch:
#         resultado = cursor.fetchall()
#     conexao.commit()
#     conexao.close()
#     return resultado

# def criar_tabela():
#     sql = """
#     CREATE TABLE IF NOT EXISTS pessoas (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         nome VARCHAR(255),
#         idade INT
#     )
#     """
#     executar_sql(sql)

agent = Agent(
    model= model,
    tools= [
        conectar,
        executar_sql,
        criar_tabela,
        TavilyTools()],
    instructions="responda em português, seja direto, fale como se falasse com uma criança, seja assertivo",
    debug_mode = True
)

playground_app = Playground(
    agents=[agent]
)

app = playground_app.get_app()

if __name__ == "__main__":
    playground_app.serve("5_Codigo_GPT_TCC:app", reload=True)