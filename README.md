# API de CRUD de Produtos

Este projeto é uma API de CRUD (Create, Read, Update, Delete) de produtos, construída usando FastAPI e SQLAlchemy. A API permite que você crie, leia, atualize e delete produtos de um banco de dados PostgreSQL.

## Tecnologias Utilizadas

- **FastAPI**: Um framework moderno, rápido (alto desempenho) e assíncrono para construção de APIs com Python 3.7+ baseado em type hints.
- **SQLAlchemy**: Um toolkit SQL e ORM para Python.
- **Uvicorn**: Um servidor ASGI para rodar a aplicação FastAPI.
- **PostgreSQL**: Um sistema de gerenciamento de banco de dados relacional avançado e de código aberto.
- **Pyenv**: Uma ferramenta para gerenciar múltiplas versões de Python.
- **Poetry**: Um gerenciador de dependências e ambientes virtuais para Python.

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- **Python 3.12.1+** (gerenciado pelo pyenv)
- **PostgreSQL**
- **Pyenv**
- **Poetry**
- **Git**

## Configuração do Projeto

1. **Clone o repositório**:

    ```sh
    git clone git@github.com:alexandremedeiros/exemplo-fasapi.git
    cd exemplo-fasapi
    ```

2. **Instale a versão correta do Python com pyenv**:

    ```sh
    pyenv install 3.12.1
    pyenv local 3.12.1
    ```

3. **Instale as dependências com o Poetry**:

    ```sh
    poetry install
    ```

4. **Ative o ambiente virtual do Poetry**:

    ```sh
    poetry shell
    ```

5. **Configuração do Banco de Dados**:

    Edite o arquivo database.py e coloque os valores para se conectar ao seu banco de dados:

    ```sh
    USERNAME = 'postgres'
    PASSWORD = 'xxxxx@'
    HOST = '111.11.111.999'
    PORT = '8989'
    DATABASE = 'database'
    ```

## Executando a Aplicação

Para rodar a aplicação, use o Uvicorn:

```sh
uvicorn main:app --reload
