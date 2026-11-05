from __future__ import annotations

import csv
from datetime import date, timedelta
from pathlib import Path


def gerar_dados_defeitos(caminho_saida: str | Path) -> None:
    """
    Gera um arquivo CSV padronizado de defeitos.
    Este script representa um processo controlado
    (evita erro humano na criação de dados).
    """

    cabecalho = [
        "id",
        "gravidade",
        "aberto_em",
        "fechado_em",
        "origem",
    ]

    dados = [
        # id, gravidade, aberto_em, fechado_em, origem
        (1, "alta",  date(2026, 1, 10), date(2026, 1, 11), "producao"),
        (2, "media", date(2026, 1, 12), date(2026, 1, 20), "teste"),
        (3, "alta",  date(2026, 1, 15), date(2026, 1, 16), "producao"),
        (4, "baixa", date(2026, 1, 18), date(2026, 1, 25), "teste"),
        (5, "media", date(2026, 1, 22), date(2026, 1, 23), "teste"),
        (6, "alta",  date(2026, 1, 25), date(2026, 2, 2),  "producao"),
    ]

    caminho_saida = Path(caminho_saida)

    with open(caminho_saida, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(cabecalho)

        for d in dados:
            writer.writerow(
                [
                    d[0],
                    d[1],
                    d[2].isoformat(),
                    d[3].isoformat(),
                    d[4],
                ]
            )


def main() -> None:
    caminho = Path("dados_defeitos.csv")
    gerar_dados_defeitos(caminho)
    print(f"[OK] CSV de defeitos gerado em: {caminho.resolve()}")


if __name__ == "__main__":
    main()