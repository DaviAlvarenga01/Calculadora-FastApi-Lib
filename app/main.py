from fastapi import FastAPI, HTTPException
from app.models import OperationRequest, OperationResponse
from app.operations import add, subtract, multiply, divide

app = FastAPI(
    Tittle="Calculadora API"
    Version = "1.0.0"
)


