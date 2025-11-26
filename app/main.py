from fastapi import FastAPI, HTTPException
from app.models.models import CalculoRequest, CalculoResponse
from app.controller.operations import Calculadora

app = FastAPI(title="Calculadora API", version="1.0.0")

@app.post("/calcular", response_model=CalculoResponse)
def calcular(dados: CalculoRequest):
    calc = Calculadora()
    
    try:
        if dados.operacao == "somar":
            resultado = calc.somar(dados.num1, dados.num2)
        elif dados.operacao == "subtrair":
            resultado = calc.subtrair(dados.num1, dados.num2)
        elif dados.operacao == "multiplicar":
            resultado = calc.multiplicar(dados.num1, dados.num2)
        elif dados.operacao == "dividir":
            resultado = calc.dividir(dados.num1, dados.num2)
        else:
            raise HTTPException(status_code=400, detail="Operação inválida")
        
        return CalculoResponse(resultado=resultado, operacao=dados.operacao)
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))