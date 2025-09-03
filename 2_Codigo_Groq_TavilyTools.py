from agno.agent import Agent
from agno.models.message import Message
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv

load_dotenv()

model = Groq(id="llama-3.3-70b-versatile")

agent = Agent(
    model= model,
    tools= [TavilyTools()],
    debug_mode = True
)

prompt = "Use suas ferramentas para pesquisar a temperatura em Bauru, SP"

agent.print_response(prompt)
