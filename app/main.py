from fastapi import FastAPI, HTTPException
from app.models.models import OperacaoRequest, OperacaoResponse
from app.controller.operations import Calculadora

app = FastAPI(title="Calculadora API", version="1.0.0")

calc = Calculadora()

@app.post("/somar", response_model=OperacaoResponse)
def somar(dados: OperacaoRequest):
    try:
        resultado = calc.somar(dados.n1, dados.n2)
        return OperacaoResponse(resultado=resultado, operacao="somar")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/subtrair", response_model=OperacaoResponse)
def subtrair(dados: OperacaoRequest):
    try:
        resultado = calc.subtrair(dados.n1, dados.n2)
        return OperacaoResponse(resultado=resultado, operacao="subtrair")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/multiplicar", response_model=OperacaoResponse)
def multiplicar(dados: OperacaoRequest):
    try:
        resultado = calc.multiplicar(dados.n1, dados.n2)
        return OperacaoResponse(resultado=resultado, operacao="multiplicar")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/dividir", response_model=OperacaoResponse)
def dividir(dados: OperacaoRequest):
    try:
        resultado = calc.dividir(dados.n1, dados.n2)
        return OperacaoResponse(resultado=resultado, operacao="dividir")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))