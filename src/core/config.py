import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=dotenv_path)
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    print(f"AVISO: Variável de ambiente DATABASE_URL não definida. Verifique o arquivo: {dotenv_path}")
else:
    print(f"INFO [config.py]: DATABASE_URL carregada de {dotenv_path}: {DATABASE_URL}")
