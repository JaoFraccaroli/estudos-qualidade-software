from __future__ import annotations

import csv
import random
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Caso:
    valor: float
    esperado: str  # número (como string) ou "ERRO"


def esperado_calcular_desconto(valor: float) -> Caso:
    """
    Espelha a REGRA do app.py:
    - valor < 0 => ERRO
    - >= 500 => valor*0.8
    - >= 200 => valor*0.9
    - senão => valor
    """
    if valor < 0:
        return Caso(valor, "ERRO")
    if valor >= 500:
        return Caso(valor, f"{valor * 0.8:.2f}")
    if valor >= 200:
        return Caso(valor, f"{valor * 0.9:.2f}")
    return Caso(valor, f"{valor:.2f}")


def gerar_casos(seed: int, n: int) -> list[Caso]:
    rng = random.Random(seed)
    casos: list[Caso] = []

    # Casos fixos (limites clássicos)
    fixos = [
        -1, 0, 1,
        199.99, 200.00, 200.01,
        499.99, 500.00, 500.01,
        1000.00
    ]
    for v in fixos:
        casos.append(esperado_calcular_desconto(v))

    # Casos aleatórios (válidos e inválidos)
    for _ in range(n):
        tipo = rng.choice(["valido_baixo", "valido_medio", "valido_alto", "invalido", "limite"])
        if tipo == "valido_baixo":
            valor = round(rng.uniform(0, 199.99), 2)
        elif tipo == "valido_medio":
            valor = round(rng.uniform(200.00, 499.99), 2)
        elif tipo == "valido_alto":
            valor = round(rng.uniform(500.00, 5000.00), 2)
        elif tipo == "limite":
            valor = rng.choice([199.99, 200.00, 200.01, 499.99, 500.00, 500.01])
        else:  # invalido
            valor = round(rng.uniform(-500.00, -0.01), 2)

        casos.append(esperado_calcular_desconto(valor))

    return casos


def salvar_csv(casos: list[Caso], caminho: str | Path) -> Path:
    caminho = Path(caminho)
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["valor", "resultado_esperado"])
        for c in casos:
            w.writerow([f"{c.valor:.2f}", c.esperado])
    return caminho


def main() -> None:
    seed = 260206  # mude em sala para mostrar reprodutibilidade
    n = 80         # quantidade de casos aleatórios
    casos = gerar_casos(seed=seed, n=n)
    saida = salvar_csv(casos, "casos_teste.csv")
    print(f"[OK] CSV gerado: {saida.resolve()}  (seed={seed}, casos={len(casos)})")


if __name__ == "__main__":
    main()