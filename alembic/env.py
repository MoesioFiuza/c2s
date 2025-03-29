# alembic/env.py

# Imports padrão (já existentes)
import os # Adicione se não estiver
import sys # Adicione se não estiver
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# --- INÍCIO DAS NOSSAS ADIÇÕES/MODIFICAÇÕES ---

# 1. Adicionar o diretório 'src' ao Path
# (Coloque isso ANTES de tentar importar seus módulos de 'src')
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# 2. Importar Base, Modelos e Configuração da URL
from src.db.base import Base                 # Importa nossa Base declarativa
from src.models.veiculo import Veiculo      # Importa nosso modelo Veiculo (e outros se tiver)
from src.core.config import DATABASE_URL    # Importa a URL do banco do .env

# --- FIM DAS NOSSAS ADIÇÕES DE IMPORT ---


# Configuração padrão do Alembic (já existente)
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --- MODIFICAÇÃO PRINCIPAL: Definir target_metadata ---
# Comente ou remova a linha original: target_metadata = None
# Adicione esta linha para apontar para os metadados dos seus modelos:
target_metadata = Base.metadata
# ----------------------------------------------------

# Restante das configurações padrão (já existentes)
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    # --- MODIFICAÇÃO: Usar nossa URL e metadados ---
    # url = config.get_main_option("sqlalchemy.url") # Linha original (pode manter ou usar DATABASE_URL)
    context.configure(
        url=DATABASE_URL, # Usa nossa URL carregada
        target_metadata=target_metadata, # Usa nossos metadados
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    # ---------------------------------------------

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""

    # --- MODIFICAÇÃO: Usar nossa URL e metadados ---

    # 1. Definir a URL programaticamente (sobrescreve alembic.ini)
    # Coloque isso ANTES de chamar engine_from_config
    config.set_main_option('sqlalchemy.url', DATABASE_URL)

    # 2. Chamar engine_from_config (geralmente já está assim)
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        # Adicione esta linha para garantir que a URL definida acima seja usada:
        url=DATABASE_URL # Passa explicitamente a URL aqui também
    )

    # 3. Configurar o contexto com nossos metadados
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata # Garante que nossos metadados são usados
        )

        # 4. Executar as migrações (padrão)
        with context.begin_transaction():
            context.run_migrations()

    # --- FIM DAS MODIFICAÇÕES ---


# Lógica padrão para escolher offline ou online (já existente)
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()