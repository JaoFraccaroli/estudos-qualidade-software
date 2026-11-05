# run_tests.py
from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path


def run(cmd: list[str]) -> int:
    """Executa comando e retorna código de saída."""
    print(f"\n[CMD] {' '.join(cmd)}")
    p = subprocess.run(cmd, text=True)
    return p.returncode


def main() -> None:
    evid = Path("evidencias")
    evid.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = evid / "execucao.log"
    junit_path = evid / "relatorio_junit.xml"

    # 1) Executa testes + JUnit XML (evidência padrão de mercado)
    cmd_tests = [
        "pytest",
        "-q",
        f"--junitxml={junit_path.as_posix()}",
    ]

    # Registra no log "o processo"
    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"\n=== EXECUCAO: {timestamp} ===\n")
        f.write(f"Comando: {' '.join(cmd_tests)}\n")

    code = run(cmd_tests)

    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"Resultado (exit code): {code}\n")

    # 2) (Opcional) Cobertura, se pytest-cov estiver instalado
    # Não falha a aula se não estiver. Apenas informa.
    cmd_cov = [
        "pytest",
        "-q",
        "--cov=app",
        f"--cov-report=term-missing",
        f"--cov-report=html:{(evid / 'htmlcov').as_posix()}",
    ]

    print("\n[INFO] Tentando gerar cobertura (opcional). Se falhar, instale: pip install pytest-cov")
    cov_code = run(cmd_cov)

    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"Cobertura (exit code): {cov_code}\n")

    print("\n[OK] Evidências geradas em:", evid.resolve())
    print(" -", log_path.resolve())
    print(" -", junit_path.resolve())
    if (evid / "htmlcov" / "index.html").exists():
        print(" -", (evid / "htmlcov" / "index.html").resolve())


if __name__ == "__main__":
    main()