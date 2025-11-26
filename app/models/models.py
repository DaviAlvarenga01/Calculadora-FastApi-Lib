from pydantic import BaseModel

class OperacaoRequest(BaseModel):
    n1: float
    n2: float

class OperacaoResponse(BaseModel):
    resultado: float
    operacao: str