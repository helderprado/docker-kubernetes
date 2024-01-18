from fastapi import FastAPI
import os

HOSTNAME = os.environ["HOSTNAME"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": f"Estou rodando dentro do pod Kubernetes de nome {HOSTNAME}"}

@app.get("/variaveis_de_ambiente")
async def variaveis_de_ambiente():
    return {
        "username": USERNAME,
        "password": PASSWORD
        }