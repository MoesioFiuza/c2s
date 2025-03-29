# Desafio Técnico C2S - Busca de Veículos

Este projeto implementa uma solução para o desafio técnico da C2S, que envolve a criação de uma API de busca de veículos e um agente de terminal interativo para consulta.

## Funcionalidades

* **API REST (FastAPI):** Um servidor que expõe um endpoint `/search/` para buscar veículos no banco de dados com base em diversos critérios (marca, modelo, ano, preço, combustível, etc.).
* **Banco de Dados (SQLite + SQLAlchemy):** Armazena informações sobre veículos. O schema é gerenciado via Alembic.
* **População de Dados:** Script para popular o banco com dados fictícios usando a biblioteca Faker.
* **Agente de Terminal:** Uma aplicação de linha de comando que simula um agente virtual, coleta critérios de busca do usuário, consulta a API e exibe os resultados.

  
## Pré-requisitos

* Python 3.10 ou superior
* Git

## Instalação e Configuração

Siga os passos abaixo **na ordem indicada**.

1.  **Clone o Repositório:**
    Abra seu terminal ou prompt de comando.
    ```bash
    git clone https://github.com/MoesioFiuza/c2s.git
    ```

2.  **Entre na Pasta do Projeto:**
    ```bash
    cd c2s
    ```

3.  **(Opcional) Abra no Editor:**
    Neste ponto, abra a pasta `Contact2Sale` no seu editor de código preferido (VS Code, PyCharm, etc.) para visualizar a estrutura dos arquivos antes de continuar com os comandos no terminal.

4.  **Crie e Ative o Ambiente Virtual:**
    * No terminal, ainda dentro da pasta `Contact2Sale`, crie o ambiente (recomendado usar `C2S`):
        ```bash
        python -m venv C2S
        ```
        *(Use `python3` se `python` não for encontrado ou for uma versão antiga)*
    * Ative o ambiente:
        * **Linux/macOS:**
            ```bash
            source C2S/bin/activate
            ```
        * **Windows (PowerShell/CMD):**
            ```bash
            .\C2S\Scripts\activate
            ```
        * Você deverá ver `(C2S)` no início do seu prompt.

5.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

6.  **Configure o Arquivo de Ambiente (`.env`):**
    * Este projeto usa um arquivo `.env` para configurar a URL do banco de dados. Um arquivo de exemplo (`.env.examplo`) é fornecido.
    * **Renomeie** o arquivo `.env.examplo` para `.env`.
       
    * O conteúdo padrão (`DATABASE_URL=sqlite:///./veiculos.db`) dentro do arquivo funcionará sem modificações para este desafio.

## Execução

Execute os passos abaixo **com o ambiente virtual (C2S) ativo**. Os passos 3 e 4 precisam ser executados em terminais **separados**, porém no mesmo diretório. Abra um novo terminal e vá até a pasta do projeto
e ativo o ambiente virtual novamente seguindo os passos já colocados acima.

1.  **Crie as Tabelas do Banco de Dados:**
    * Execute o Alembic para aplicar as migrações:
        ```bash
       
        python -m alembic upgrade head
        ```
    * *(Este comando criará o arquivo `veiculos.db` e as tabelas `veiculos` e `alembic_version`).*

2.  **Popule o Banco de Dados:**
    * Execute o script de população:
        ```bash
        python src/scripts/populate.py
        ```

3.  **Execute o Servidor da API:**
    * Abra um **primeiro terminal** (com `(C2S)` ativo) e execute:
        ```bash
        uvicorn src.server_app:app --host 0.0.0.0 --port 8000
        ```
    * Mantenha este terminal aberto. Acesse `http://127.0.0.1:8000/docs` no navegador para ver a documentação interativa.

4.  **Execute o Agente de Terminal:**
    * Abra um **segundo terminal** (com `(C2S)` ativo) e execute:
        ```bash
        python src/agent_app.py
        ```
    * Interaja com o agente virtual. Digite `sair` para finalizar.

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
