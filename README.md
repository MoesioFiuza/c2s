# Desafio Técnico C2S - Busca de Veículos

Este projeto implementa uma solução para o desafio técnico da C2S, que envolve a criação de uma API de busca de veículos e um agente de terminal interativo para consulta.

## Funcionalidades

- **API REST (FastAPI):** Um servidor que expõe um endpoint `/search/` para buscar veículos no banco de dados com base em diversos critérios (marca, modelo, ano, preço, combustível, etc.).
- **Banco de Dados (SQLite + SQLAlchemy):** Armazena informações sobre veículos. O schema é gerenciado via Alembic.
- **População de Dados:** Script para popular o banco com dados fictícios usando a biblioteca Faker.
- **Agente de Terminal:** Uma aplicação de linha de comando que simula um agente virtual, coleta critérios de busca do usuário, consulta a API e exibe os resultados formatados em tabela (`tabulate`).

## Pré-requisitos

- Python 3.10 ou superior
- Git

## Instalação

1.  **Clone o Repositório:**

    ```bash
    git clone https://github.com/MoesioFiuza/c2s.git
    cd Contact2Sale
    ```

2.  **Crie e Ative o Ambiente Virtual:**

    - Recomendado usar o nome `C2S`:
      ```bash
      python -m venv C2S
      ```
    - Ative o ambiente:
      - **Linux/macOS:**
        ```bash
        source C2S/bin/activate
        ```
      - **Windows:**
        ```bash
        .\C2S\Scripts\activate
        ```
      - Você deverá ver `(C2S)` no início do seu prompt do terminal.

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuração

1.  **Arquivo de Ambiente (`.env`):**
    - Este projeto usa um arquivo `.env` para configurar a URL do banco de dados. Um arquivo de exemplo (`.env.examplo`) é fornecido.
    - Copie o exemplo para criar seu arquivo `.env`:
      ```bash
      cp .env.examplo .env
      ```
    - O valor padrão `DATABASE_URL=sqlite:///./veiculos.db` no `.env.examplo` criará um banco de dados SQLite chamado `veiculos.db` na raiz do projeto e deve funcionar sem modificações para este desafio.

## Execução

Siga os passos na ordem abaixo. Os passos 3 e 4 precisam ser executados em terminais **separados**.

1.  **Configure o Banco de Dados (Criação/Atualização de Tabelas):**

    - Certifique-se de que seu ambiente virtual (`C2S`) esteja ativo.
    - Execute o Alembic para aplicar as migrações e criar as tabelas:
      ```bash
      alembic upgrade head
      ```
    - _(Este comando criará o arquivo `veiculos.db` se ele não existir e garantirá que as tabelas `veiculos` e `alembic_version` estejam criadas/atualizadas)._

2.  **Popule o Banco de Dados com Dados Fictícios:**

    - Execute o script de população:
      ```bash
      python src/scripts/populate.py
      ```

3.  **Execute o Servidor da API:**

    - Abra um **primeiro terminal**, ative o ambiente virtual (`C2S`) e execute:
      ```bash
      uvicorn src.server_app:app --host 0.0.0.0 --port 8000
      ```
    - Mantenha este terminal aberto. O servidor estará rodando e aguardando conexões na porta 8000. Você pode acessar a documentação interativa em `http://127.0.0.1:8000/docs`.

4.  **Execute o Agente de Terminal:**
    - Abra um **segundo terminal**, ative o ambiente virtual (`C2S`) e execute:
      ```bash
      python src/agent_app.py
      ```
    - Interaja com o agente virtual para buscar veículos. Digite `sair` para finalizar a conversa.

## Estrutura do Projeto

Contact2Sale/

├── alembic/ # Arquivos de migração do Alembic

├── src/ # Código fonte principal

│ ├── core/ # Configurações centrais (config.py)

│ ├── db/ # Configuração do banco (base.py)

│ ├── models/ # Modelos SQLAlchemy (veiculo.py)

│ ├── scripts/ # Scripts auxiliares (populate.py)

│ ├── agent_app.py # Aplicação do agente de terminal (Cliente)

│ └── server_app.py # Aplicação da API FastAPI (Servidor)

├── .env.examplo # Arquivo de exemplo para variáveis de ambiente

├── .gitignore # Arquivos ignorados pelo Git


├── alembic.ini # Configuração do Alembic

├── README.md # Este arquivo

└── requirements.txt # Dependências Python
