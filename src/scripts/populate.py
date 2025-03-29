import sys
import os
import random
from faker import Faker
from sqlalchemy.orm import Session

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from src.db.base import SessionLocal, engine, Base 
from src.models.veiculo import Veiculo 

fake = Faker('pt_BR')

marcas_modelos = {
    'Toyota': ['Corolla', 'Hilux', 'Etios', 'Yaris'],
    'Honda': ['Civic', 'HR-V', 'Fit', 'City'],
    'Volkswagen': ['Gol', 'Polo', 'Virtus', 'T-Cross', 'Nivus'],
    'Fiat': ['Mobi', 'Argo', 'Cronos', 'Toro', 'Strada'],
    'Chevrolet': ['Onix', 'Tracker', 'S10', 'Cruze', 'Onix Plus'],
    'Ford': ['Ranger', 'Territory', 'Mustang'], # Menos opções atuais no BR
    'Hyundai': ['HB20', 'Creta', 'Tucson'],
    'Renault': ['Kwid', 'Duster', 'Sandero', 'Captur']
}
tipos_combustivel = ['Gasolina', 'Etanol', 'Flex', 'Diesel', 'Elétrico']
cores = ['Preto', 'Branco', 'Prata', 'Cinza', 'Vermelho', 'Azul', 'Verde']
transmissoes = ['Manual', 'Automática', 'CVT', 'Automatizada']

def populate_database(db: Session, num_records: int = 100):
    print(f"Iniciando a população do banco com {num_records} registros...")
    try:
        for i in range(num_records):
            marca = random.choice(list(marcas_modelos.keys()))
            modelo = random.choice(marcas_modelos[marca])
            ano_fabricacao = fake.random_int(min=2005, max=2024)
            ano_modelo = random.choice([ano_fabricacao, ano_fabricacao + 1]) 
            combustivel = random.choice(tipos_combustivel)
            cor = random.choice(cores)
            max_km = max(1000, (2025 - ano_modelo) * 20000)
            min_km = max(0, (2025 - ano_modelo - 2) * 5000)
            quilometragem = fake.random_int(min=min_km, max=max_km)

            numero_portas = random.choice([2, 4])
            transmissao = random.choice(transmissoes)
            preco_base = max(15000, (ano_modelo - 2000) * 3000)
            preco = round(random.uniform(preco_base * 0.8, preco_base * 1.5), 2)

            veiculo = Veiculo(
                marca=marca,
                modelo=modelo,
                ano_fabricacao=ano_fabricacao,
                ano_modelo=ano_modelo,
                combustivel=combustivel,
                cor=cor,
                quilometragem=quilometragem,
                numero_portas=numero_portas,
                transmissao=transmissao,
                preco=preco
            )
            db.add(veiculo)

        db.commit()
        print(f"SUCESSO: {num_records} registros de veículos inseridos no banco.")

    except Exception as e:
        print(f"ERRO durante a população do banco: {e}")
        db.rollback()
    finally:
        db.close() 

if __name__ == "__main__":
   
    print("INFO: Tentando criar tabelas com Base.metadata.create_all()...")
   #Base.metadata.create_all(bind=engine)
    print("INFO: Base.metadata.create_all() executado.")
    db_session = SessionLocal()
    populate_database(db_session, num_records=150)