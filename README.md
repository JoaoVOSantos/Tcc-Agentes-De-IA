# Projeto `ex_agentes`

projeto foi criado com o objetivo de testar e utilizar a api do`gpt` em um ambiente isolado com `uv` para o tcc.

## Pré-requisitos

Antes de iniciar, certifique-se de que os seguintes itens estão instalados no seu sistema:

- [Python 3.11+](https://www.python.org/downloads/)
- [uv (Ultra Velocity)](https://github.com/astral-sh/uv) – um gerenciador de dependências moderno e rápido para projetos Python

## Instalação

Siga os passos abaixo para clonar o repositório, configurar o ambiente e instalar as dependências:

```bash
# 1. Crie e acesse a pasta do projeto
mkdir ex_agentes
cd ex_agentes

# 2. (Se estiver em outro ambiente virtual) Saia do ambiente atual
deactivate  # (se aplicável)

# 3. Inicialize o projeto com o uv
uv init

# 4. Crie o ambiente virtual
uv venv

# 5. Ative o ambiente virtual
source .venv/bin/activate  # ubuntu - wsl

# 6. Instale a biblioteca agno ou qualquer outra que usar
uv add agno, op

# Rode seu projeto
python meu_script.py

# rode o codigo
python 5_Codigo_GPT_TCC.py , ao abrir o link coloque no endpoint http://localhost:777/V1