# app.py
from __future__ import annotations


def calcular_desconto(preco: float, percentual: float) -> float:
    """
    Retorna o preço com desconto.

    Regras de negócio esperadas (para discussão na aula):
    - preco deve ser > 0
    - percentual deve estar entre 0 e 100
    - retorna float com 2 casas (apenas para apresentação)
    """
    # deliberadamente "permissivo" para abrir debate sobre qualidade:
    if preco <= 0:
        return 0.0
    if percentual < 0:
        percentual = 0
    if percentual > 100:
        percentual = 100

    final = preco * (1 - percentual / 100)
    return round(final, 2)


def faixa_preco(preco_final: float) -> str:
    """Classifica um preço final por faixa."""
    if preco_final < 50:
        return "baixo"
    if preco_final < 200:
        return "medio"
    return "alto"