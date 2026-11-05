from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

from app import calcular_desconto


def executar_testes(caminho_csv: str | Path) -> int:
    total = 0
    falhas = 0
    erros_esperados = 0

    with open(caminho_csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            valor = float(row["valor"])
            esperado = row["resultado_esperado"].strip().upper()

            total += 1

            if esperado == "ERRO":
                try:
                    calcular_desconto(valor)
                    falhas += 1
                    print(f"[FALHA] valor={valor:.2f} esperado=ERRO obtido=SEM_ERRO")
                except ValueError:
                    erros_esperados += 1
                    print(f"[OK] valor={valor:.2f} (erro esperado)")
                continue

            esperado_num = float(esperado)

            try:
                resultado = calcular_desconto(valor)
            except Exception as e:
                falhas += 1
                print(f"[FALHA] valor={valor:.2f} esperado={esperado_num:.2f} obtido=EXCECAO({type(e).__name__})")
                continue

            # O esperado no CSV tem 2 casas decimais; compara o resultado arredondado
            # para evitar falsas falhas por causa da precisão do float
            if abs(round(resultado, 2) - esperado_num) > 1e-9:
                falhas += 1
                print(f"[FALHA] valor={valor:.2f} esperado={esperado_num:.2f} obtido={resultado:.2f}")
            else:
                print(f"[OK] valor={valor:.2f}")

    print("\nResumo da execução")
    print(f"Total de testes: {total}")
    print(f"Passaram: {total - falhas}")
    print(f"Falhas: {falhas}")
    print(f"Erros esperados (ValueError): {erros_esperados}")
    return falhas


def main() -> None:
    print("Execução automática de testes (Aula 04)")
    print(f"Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    falhas = executar_testes("casos_teste.csv")
    raise SystemExit(1 if falhas else 0)


if __name__ == "__main__":
    main()