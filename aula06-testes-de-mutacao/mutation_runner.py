# mutation_runner.py
from __future__ import annotations

import re
import subprocess
from datetime import datetime
from pathlib import Path

APP = Path("app.py")

MUTANTES_EXPR = {
    "mutante_1_maior_que": "media > 6.0",
    "mutante_2_maior_igual_7": "media >= 7.0",
    "mutante_3_maior_que_5": "media > 5.0",
}


def rodar_pytest() -> tuple[bool, str]:
    p = subprocess.run(["pytest", "-q"], text=True, capture_output=True)
    saida = (p.stdout or "") + (p.stderr or "")
    return (p.returncode == 0), saida


def localizar_return_em_funcao(texto: str, nome_func: str) -> tuple[int, str]:
    """
    Encontra a linha (índice) do primeiro 'return' dentro de uma função específica.
    Retorna (idx_linha, indentacao).
    """
    linhas = texto.splitlines()

    # acha a linha do def
    def_re = re.compile(rf"^\s*def\s+{re.escape(nome_func)}\s*\(")
    idx_def = None
    for i, line in enumerate(linhas):
        if def_re.match(line):
            idx_def = i
            break
    if idx_def is None:
        raise RuntimeError(f"Não encontrei def {nome_func}() em app.py")

    # indentação base do def (ex: "")
    indent_def = linhas[idx_def][: len(
        linhas[idx_def]) - len(linhas[idx_def].lstrip())]

    # procura o return dentro do bloco da função: linhas com indent > indent_def
    idx_return = None
    indent_return = None
    for j in range(idx_def + 1, len(linhas)):
        line = linhas[j]
        if not line.strip():
            continue

        indent_atual = line[: len(line) - len(line.lstrip())]

        # saiu do bloco da função (indentação voltou)
        if len(indent_atual) <= len(indent_def):
            break

        if line.lstrip().startswith("return "):
            idx_return = j
            indent_return = indent_atual
            break

    if idx_return is None or indent_return is None:
        raise RuntimeError(f"Não encontrei 'return' dentro de {nome_func}()")

    return idx_return, indent_return


def main() -> None:
    original_text = APP.read_text(encoding="utf-8")
    linhas = original_text.splitlines()

    idx_return, indent = localizar_return_em_funcao(
        original_text, "eh_aprovado")

    print("\n=== TESTE DE MUTAÇÃO (SIMULADO) ===\n")
    print(f"[INFO] Execução: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    for nome, expr in MUTANTES_EXPR.items():
        print(f"[TESTANDO] {nome}")

        # substitui só a linha do return dentro da função
        linhas_mut = linhas.copy()
        linhas_mut[idx_return] = f"{indent}return {expr}"
        APP.write_text("\n".join(linhas_mut) + "\n", encoding="utf-8")

        passou, saida = rodar_pytest()

        if passou:
            print("  ❌ MUTANTE VIVO (teste fraco)")
        else:
            if any(err in saida for err in ["IndentationError", "SyntaxError"]):
                print("  ⚠️ MUTANTE INVÁLIDO (erro de sintaxe/indentação; não conta)")
            else:
                print("  ✅ MUTANTE MORTO (teste forte)")

    APP.write_text(original_text, encoding="utf-8")
    print("\n[OK] Código original restaurado.")


if __name__ == "__main__":
    main()
