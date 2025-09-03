from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.message import Message
# from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from agno.playground import Playground
from dotenv import load_dotenv

load_dotenv()

model = OpenAIChat(id="gpt-4.1-mini")

def celsius_to_fahrenheit(celsius: float):
    """
    Converte uma temperatura em graus celsius para fahrenheit.
    Args: 
        celsius (float): Temperatura em graus celsius.
    
    Returns: 
        float: temperatura convertida para graus fahrenheit.
    
    """
    return(celsius * 9/5) + 32

agent = Agent(
    model= model,
    tools= [
        celsius_to_fahrenheit,
        TavilyTools()],
    instructions="responda em português, seja direto, fale como se falasse com uma criança, seja assertivo",
    debug_mode = True
)

prompt = "Conversa 18 graus celsius para fahrenheit"

agent.print_response(prompt, stream=True)

playground_app = Playground(
    agents=[agent]
)

app = playground_app.get_app()

if __name__ == "__main__":
    playground_app.serve("4_Codigo_GPT_TavilyTools_Def_Playground:app", reload=True)