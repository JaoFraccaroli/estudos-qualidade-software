# run_tests.py
from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path


def main() -> None:
    evid = Path("evidencias")
    evid.mkdir(exist_ok=True)

    log = evid / "execucao.log"
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cmd = ["pytest", "-q"]

    with log.open("a", encoding="utf-8") as f:
        f.write(f"\n=== EXECUCAO {ts} ===\n")
        f.write(f"Comando: {' '.join(cmd)}\n")

    p = subprocess.run(cmd, text=True, capture_output=True)
    saida = (p.stdout or "") + (p.stderr or "")

    with log.open("a", encoding="utf-8") as f:
        f.write(saida.strip() + "\n")
        f.write(f"Exit code: {p.returncode}\n")

    print(saida.strip())
    print("\n[OK] Evidência salva em:", log.resolve())


if __name__ == "__main__":
    main()