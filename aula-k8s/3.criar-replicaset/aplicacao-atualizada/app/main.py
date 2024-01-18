from fastapi import FastAPI
import os

HOSTNAME = os.environ["HOSTNAME"]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": f"Estou rodando dentro de um pod Kubernetes de nome {HOSTNAME} e sou uma versão atualizada..."}