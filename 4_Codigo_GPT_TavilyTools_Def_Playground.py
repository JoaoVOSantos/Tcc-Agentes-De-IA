from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.message import Message
# from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from agno.playground import Playground
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

# model = Groq(id="llama-3.3-70b-versatile")
model = OpenAIChat(id="gpt-4.1-mini")
    
def conexao_com_banco(sqlGPT):
    """
    Conecta no banco e pode executar um codigo sql.
    Args:
        sqlGPT (str): query que sera executada no banco. (pode conter um placeholder %s).
        id (int): pode ser passado um usuario para a query.
    Returns: 
         list: Lista de tuplas contendo os resultados da query.
    """
    conexao = mysql.connector.connect(
                                      host="localhost",
                                      user="root",
                                      password="",
                                      database="bancotcc")
    cursor = conexao.cursor()
    cursor.execute(sqlGPT)
    resultados = cursor.fetchall()  # ou fetchone(), se for apenas 1 resultado
    conexao.close()
    return resultados


agent = Agent(
    model= model,
    tools= [
        conexao_com_banco,
        TavilyTools()],
    instructions="responda em português, seja direto, fale como se falasse com uma criança, seja assertivo, execute em linguagem mysql",
    debug_mode = True
)

# prompt = "Conversa 18 graus celsius para fahrenheit"
prompt = input("Digite o prompt: ")

agent.print_response(prompt)
# agent.print_response(prompt, stream=True)

# playground_app = Playground(
#     agents=[agent]
# )

# app = playground_app.get_app()

# if __name__ == "__main__":
#     playground_app.serve("chatgptagentedeia:app", reload=True)