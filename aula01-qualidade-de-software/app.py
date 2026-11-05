# app.py
from __future__ import annotations

def media_aprovacao(notas: list[float]) -> float:
    """
    Calcula a média para fins de aprovação.

    REGRAS (que *deveriam* ser respeitadas, mas este código NÃO respeita bem):
    - Não pode aceitar lista vazia
    - Notas devem estar entre 0 e 10
    - A média correta é soma / quantidade (não arredondar "pra facilitar")
    """
    # ERRO CONCEITUAL #1: se vier vazio, retorna 0 "pra não dar erro"
    if not notas:
        return 0.0

    # ERRO CONCEITUAL #2: "normaliza" notas inválidas do jeito errado
    # (em vez de rejeitar, ele força para dentro do intervalo)
    notas_normalizadas = []
    for n in notas:
        if n < 0:
            n = 0
        if n > 10:
            n = 10
        notas_normalizadas.append(n)

    # ERRO CONCEITUAL #3: arredonda a média para inteiro (perde informação)
    media = sum(notas_normalizadas) / len(notas_normalizadas)
    return float(int(media))  # <-- isso faz 6.9 virar 6.0, por exemplo


def aprovado(media: float) -> bool:
    """Regra de aprovação: aprovado se média >= 6.0"""
    return media >= 6.0