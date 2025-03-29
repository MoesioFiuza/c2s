from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from .db.base import get_db 
from .models.veiculo import Veiculo

app = FastAPI(title="API de Busca de Veículos", version="0.1.0")

class VeiculoSearchCriteria(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None
    ano_min: Optional[int] = None       
    ano_max: Optional[int] = None       
    cor: Optional[str] = None
    preco_min: Optional[float] = None   
    preco_max: Optional[float] = None   
    combustivel: Optional[str] = None   
    km_max: Optional[int] = None        
    portas: Optional[int] = None        
    transmissao: Optional[str] = None   
    

class VeiculoResponse(BaseModel):
    id: int
    marca: str
    modelo: str
    ano_fabricacao: Optional[int]
    ano_modelo: Optional[int]
    combustivel: Optional[str]
    cor: Optional[str]
    quilometragem: Optional[int]
    numero_portas: Optional[int]
    transmissao: Optional[str] 
    preco: Optional[float]

    class Config:
        from_attributes = True


@app.post("/search/", response_model=List[VeiculoResponse])
def search_veiculos(
    criteria: VeiculoSearchCriteria,
    db: Session = Depends(get_db)
):
    
    print(f"INFO: Recebidos critérios de busca: {criteria.dict(exclude_none=True)}") # exclude_none para log mais limpo
    query = db.query(Veiculo)

    if criteria.marca:
        query = query.filter(Veiculo.marca.ilike(f"%{criteria.marca}%"))
    if criteria.modelo:
        query = query.filter(Veiculo.modelo.ilike(f"%{criteria.modelo}%"))
    if criteria.ano_min:
        query = query.filter(Veiculo.ano_modelo >= criteria.ano_min)
    if criteria.ano_max:
        query = query.filter(Veiculo.ano_modelo <= criteria.ano_max)
    if criteria.cor:
        query = query.filter(Veiculo.cor.ilike(f"%{criteria.cor}%"))
    if criteria.preco_min:
        query = query.filter(Veiculo.preco >= criteria.preco_min)
    if criteria.preco_max:
        query = query.filter(Veiculo.preco <= criteria.preco_max)
    if criteria.combustivel:
        query = query.filter(Veiculo.combustivel.ilike(f"%{criteria.combustivel}%"))
    if criteria.km_max is not None:
        query = query.filter(Veiculo.quilometragem <= criteria.km_max)
    if criteria.portas:
        query = query.filter(Veiculo.numero_portas == criteria.portas)
    if criteria.transmissao:
        query = query.filter(Veiculo.transmissao.ilike(f"%{criteria.transmissao}%"))
    
    try:
        results = query.all()
        print(f"INFO: Encontrados {len(results)} veículos.")
        return results
    except Exception as e:
        print(f"ERRO ao buscar veículos: {e}")
        raise HTTPException(status_code=500, detail="Erro interno ao processar a busca.")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Busca de Veículos!"}