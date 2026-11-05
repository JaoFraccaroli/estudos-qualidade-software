# app.py
from __future__ import annotations


def calcular_frete(valor_compra: float, cliente_vip: bool) -> float:
    """
    Regra:
    - valor_compra < 0: inválido
    - frete base: 20
    - se valor_compra >= 200: frete grátis
    - VIP paga metade do frete (exceto se grátis)
    """
    if valor_compra < 0:
        raise ValueError("valor_compra inválido")

    frete = 20.0

    # if valor_compra > 200: 
    if valor_compra > 200:
        return 0.0

    if cliente_vip:
        frete = frete / 2

    return frete