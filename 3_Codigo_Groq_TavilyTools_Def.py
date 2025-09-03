from agno.agent import Agent
from agno.models.message import Message
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv

load_dotenv()

model = Groq(id="llama-3.3-70b-versatile")

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
    debug_mode = True
)

# prompt = "Conversa 18 graus celsius para fahrenheit"
prompt = "Pesquise a temperatura em celsius da cidade de Bauru, SP e converta para fahrenheit."


agent.print_response(prompt, stream=True)
