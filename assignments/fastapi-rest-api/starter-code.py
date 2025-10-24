# FastAPI REST API - Código Inicial
# Este arquivo fornece a estrutura básica para começar sua API

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import date
import uvicorn

# Inicializar a aplicação FastAPI
app = FastAPI(
    title="Biblioteca Digital API",
    description="Uma API REST para gerenciar livros e autores",
    version="1.0.0"
)

# TODO: Definir modelos Pydantic aqui
class Author(BaseModel):
    id: Optional[int] = None
    nome: str = Field(..., min_length=2, max_length=100)
    nacionalidade: str = Field(..., min_length=2, max_length=50)
    data_nascimento: date
    
    # TODO: Adicionar validadores customizados
    
class Book(BaseModel):
    id: Optional[int] = None
    titulo: str = Field(..., min_length=1, max_length=200)
    isbn: str = Field(..., regex=r"^[\d-]{10,17}$")
    ano_publicacao: int = Field(..., ge=1000, le=2025)
    author_id: int
    
    # TODO: Adicionar validadores customizados

# Simulação de banco de dados em memória (para fins didáticos)
fake_authors_db = []
fake_books_db = []

# TODO: Implementar endpoint de saúde
@app.get("/health")
async def health_check():
    """Endpoint para verificar se a API está funcionando"""
    # TODO: Implementar verificação de saúde
    pass

# TODO: Implementar endpoints para autores
@app.get("/authors")
async def get_authors():
    """Listar todos os autores"""
    # TODO: Implementar listagem de autores
    pass

@app.get("/authors/{author_id}")
async def get_author(author_id: int):
    """Obter autor específico por ID"""
    # TODO: Implementar busca de autor por ID
    pass

@app.post("/authors")
async def create_author(author: Author):
    """Criar novo autor"""
    # TODO: Implementar criação de autor
    pass

# TODO: Implementar PUT e DELETE para autores

# TODO: Implementar endpoints para livros
@app.get("/books")
async def get_books(skip: int = 0, limit: int = 10):
    """Listar todos os livros com paginação"""
    # TODO: Implementar listagem de livros
    pass

# TODO: Implementar demais endpoints para livros

# TODO: Implementar endpoints avançados (busca, filtros)

if __name__ == "__main__":
    # Para executar: python starter-code.py
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)