# app.py
def calcular_desconto(valor: float) -> float:
    """
    Regra de negócio:
    - compras >= 200 → desconto 10%
    - compras >= 500 → desconto 20%
    - caso contrário → sem desconto
    """

    if valor < 0:
        raise ValueError("valor inválido")

    if valor >= 500:
        return valor * 0.8

    if valor >= 200:
        return valor * 0.9

    return valor