from fastapi import FastAPI

app = FastAPI()

@app.get("/api/vendas")
def get_vendas():
    dados = [
        {"id": 1, "mes": "Jan", "vendas": 2000},
        {"id": 2, "mes": "Fev", "vendas": 4000},
        {"id": 2, "mes": "Mar", "vendas": 3700}
    ]
    return dados
