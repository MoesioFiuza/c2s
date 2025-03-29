from sqlalchemy import Column, Integer, String, Float, DateTime, Index
from datetime import datetime
from src.db.base import Base

class Veiculo(Base):
    __tablename__ = 'veiculos'

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String(100), nullable=False, index=True) 
    modelo = Column(String(100), nullable=False, index=True) 
    ano_fabricacao = Column(Integer)
    ano_modelo = Column(Integer, index=True) 
    combustivel = Column(String(50))
    cor = Column(String(50))
    quilometragem = Column(Integer, default=0)
    numero_portas = Column(Integer)
    transmissao = Column(String(50))
    preco = Column(Float, index=True) 
    data_cadastro = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Veiculo(id={self.id}, marca='{self.marca}', modelo='{self.modelo}', ano='{self.ano_modelo}')>"
