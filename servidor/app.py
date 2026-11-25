"""Servidor do chatbot (tarefa 01-04).

Subir:  uvicorn servidor.app:app --port 8000   (na raiz do projeto)
Abrir:  http://localhost:8000

Nesta tarefa a Groq responde sozinha, sem documentos nem Espaço Aluno:
é a prova de que a ponta que escreve a resposta funciona. O classificador,
a busca e o leitor entram em 03-01.

Regras (NFR-05, NFR-10, D-007):
- a chave vem só da variável de ambiente GROQ_API_KEY;
- nenhum texto de pergunta ou resposta vai para disco ou log;
- não há histórico: cada pergunta é respondida sozinha.
"""

import time
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from servidor.groq_cliente import ErroGroq, _chave, responder

AQUI = Path(__file__).resolve().parent
app = FastAPI(title="Chatbot UniCEUB", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=AQUI / "static"), name="static")


class Pergunta(BaseModel):
    pergunta: str = Field(min_length=1, max_length=1000)


class Resposta(BaseModel):
    resposta: str
    modelo: str
    segundos: float


@app.get("/")
def tela():
    return FileResponse(AQUI / "static" / "index.html")


@app.get("/api/saude")
def saude():
    return {"ok": True, "chave_groq": bool(_chave())}


@app.post("/api/perguntar", response_model=Resposta)
def perguntar(dados: Pergunta):
    inicio = time.perf_counter()
    try:
        texto, modelo = responder(dados.pergunta.strip())
    except ErroGroq as e:
        # A mensagem de erro nunca contém o texto da pergunta.
        raise HTTPException(status_code=e.status, detail=e.mensagem)
    return Resposta(resposta=texto, modelo=modelo,
                    segundos=round(time.perf_counter() - inicio, 2))
