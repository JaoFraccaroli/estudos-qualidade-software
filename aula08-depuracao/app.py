# app.py
from __future__ import annotations


def preco_com_desconto(preco: float, desconto_percentual: float) -> float:
    """
    Esperado:
    - preco > 0
    - desconto_percentual entre 0 e 100
    - retorno com 2 casas

    Defeito proposital:
    - aplica desconto_percentual como fração errada (ex.: 10 vira 10x em vez de 10%)
    """
    if preco <= 0:
        raise ValueError("preco inválido")
    if desconto_percentual < 0 or desconto_percentual > 100:
        raise ValueError("desconto inválido")

    # BUG: deveria ser (desconto_percentual / 100)
    preco_final = preco * (1 - desconto_percentual)

    return round(preco_final, 2)
