class Calculadora:
    def somar(n1: float, n2: float) -> float:
        return n1 + n2

    def subtrair(n1: float, n2: float) -> float:
        return n1 - n2

    def multiplicar(n1: float, n2: float) -> float:
        return n1 * n2

    def dividir(n1: float, n2: float) -> float:
        if n2 == 0:
            raise ValueError("Divisão por zero não vai rolar.")
        return n1 / n2