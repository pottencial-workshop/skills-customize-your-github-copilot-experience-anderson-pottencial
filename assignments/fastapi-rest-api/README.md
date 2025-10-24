# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Nesta tarefa, você aprenderá a construir uma API REST completa usando o framework FastAPI do Python. Você criará uma API para gerenciar uma biblioteca digital, implementando operações CRUD (Create, Read, Update, Delete) para livros e autores.

## 📝 Tasks

### 🛠️ Configuração do Ambiente e Estrutura Básica

#### Description
Configure o ambiente de desenvolvimento e crie a estrutura básica da API FastAPI. Você instalará as dependências necessárias e criará os endpoints fundamentais.

#### Requirements
O projeto configurado deve:

- Instalar FastAPI e Uvicorn usando pip
- Criar um arquivo `main.py` com uma aplicação FastAPI básica
- Implementar um endpoint de saúde GET `/health` que retorna status da API
- Configurar e executar o servidor de desenvolvimento local
- Documentar como executar a aplicação

### 🛠️ Modelagem de Dados e Validação

#### Description
Defina os modelos de dados usando Pydantic para representar livros e autores. Implemente validação de dados de entrada e saída da API.

#### Requirements
Os modelos implementados devem:

- Criar modelo `Author` com campos: id, nome, nacionalidade, data_nascimento
- Criar modelo `Book` com campos: id, titulo, isbn, ano_publicacao, author_id
- Implementar validação de tipos de dados adequados
- Adicionar validações customizadas (ex: ano não pode ser futuro, ISBN deve ter formato válido)
- Criar modelos de resposta e request separados quando necessário

### 🛠️ Implementação dos Endpoints CRUD

#### Description
Implemente todos os endpoints necessários para operações CRUD completas tanto para livros quanto para autores, utilizando métodos HTTP apropriados.

#### Requirements
A API completa deve incluir:

- GET `/authors` - listar todos os autores
- GET `/authors/{id}` - obter autor específico por ID
- POST `/authors` - criar novo autor
- PUT `/authors/{id}` - atualizar autor existente
- DELETE `/authors/{id}` - remover autor
- GET `/books` - listar todos os livros com informações do autor
- GET `/books/{id}` - obter livro específico por ID
- POST `/books` - criar novo livro
- PUT `/books/{id}` - atualizar livro existente
- DELETE `/books/{id}` - remover livro
- Implementar tratamento adequado de erros HTTP (404, 400, 422)
- Adicionar documentação automática dos endpoints

### 🛠️ Funcionalidades Avançadas e Testes

#### Description
Adicione funcionalidades avançadas como filtros de busca, paginação e implemente testes básicos para validar o funcionamento da API.

#### Requirements
As funcionalidades avançadas devem incluir:

- Implementar filtros de busca: GET `/books?author_name=`, `/books?year=`
- Adicionar paginação com parâmetros `skip` e `limit`
- Criar endpoint GET `/books/author/{author_id}` para listar livros de um autor
- Implementar middleware de CORS para permitir requisições de frontend
- Criar pelo menos 5 testes unitários usando pytest
- Adicionar logging básico para requisições
- Documentar todos os endpoints na documentação automática do FastAPI