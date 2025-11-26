from pydantic import BaseModel

class CalculoRequest(BaseModel):
    n1: float
    n2: float
    operacao: str

class CalculoResponse(BaseModel):
    resultado: float
    operacao: str