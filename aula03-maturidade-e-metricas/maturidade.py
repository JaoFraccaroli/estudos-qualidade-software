from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from statistics import mean


DATE_FMT = "%Y-%m-%d"


@dataclass
class Defeito:
    id: int
    gravidade: str
    aberto_em: datetime
    fechado_em: datetime
    origem: str  # "teste" ou "producao"

    @property
    def tempo_correcao_dias(self) -> int:
        return (self.fechado_em - self.aberto_em).days


def carregar_defeitos(caminho_csv: str | Path) -> list[Defeito]:
    defeitos: list[Defeito] = []
    with open(caminho_csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            defeitos.append(
                Defeito(
                    id=int(row["id"]),
                    gravidade=row["gravidade"].strip().lower(),
                    aberto_em=datetime.strptime(row["aberto_em"], DATE_FMT),
                    fechado_em=datetime.strptime(row["fechado_em"], DATE_FMT),
                    origem=row["origem"].strip().lower(),
                )
            )
    return defeitos


def avaliar_maturidade(checklist: dict[str, bool]) -> tuple[int, str]:
    """
    Regra simples e didática:
    - Nível 1: quase nada existe
    - Nível 2: planejamento básico e execução repetível
    - Nível 3: processos documentados e padronizados
    - Nível 4: métricas e gestão por dados
    - Nível 5: melhoria contínua e prevenção

    Isso NÃO é um modelo oficial, é uma simulação pedagógica.
    """
    pontos = sum(1 for v in checklist.values() if v)
    total = len(checklist)
    perc = pontos / total

    if perc < 0.25:
        return 1, "Inicial (ad hoc, imprevisível)"
    if perc < 0.45:
        return 2, "Gerenciado (planejamento básico, repetível)"
    if perc < 0.70:
        return 3, "Definido (processo padronizado/documentado)"
    if perc < 0.90:
        return 4, "Medido (métricas e gestão por dados)"
    return 5, "Otimizado (melhoria contínua e prevenção)"


def gerar_relatorio_md(
    defeitos: list[Defeito],
    nivel: int,
    descricao_nivel: str,
    checklist: dict[str, bool],
    caminho_saida: str | Path = "RELATORIO_AULA03.md",
) -> Path:
    total = len(defeitos)
    prod = sum(1 for d in defeitos if d.origem == "producao")
    teste = sum(1 for d in defeitos if d.origem == "teste")

    tempos = [d.tempo_correcao_dias for d in defeitos]
    mttr = mean(tempos) if tempos else 0.0  # Mean Time To Repair

    altas = [d for d in defeitos if d.gravidade == "alta"]
    mttr_altas = mean([d.tempo_correcao_dias for d in altas]) if altas else 0.0

    checklist_md = "\n".join(
        [f"- [{'x' if v else ' '}] {k}" for k, v in checklist.items()]
    )

    linhas_defeitos = "\n".join(
        [
            f"| {d.id} | {d.gravidade} | {d.origem} | {d.aberto_em.date()} | {d.fechado_em.date()} | {d.tempo_correcao_dias} |"
            for d in defeitos
        ]
    )

    md = f"""# Relatório de Qualidade – Aula 03 (Normas e Maturidade)

## 1) Resultado do Diagnóstico de Maturidade (simulado)
**Nível estimado:** {nivel}  
**Descrição:** {descricao_nivel}

> Observação: este diagnóstico é didático. Em modelos reais, existe avaliação formal.

---

## 2) Checklist de Processo (evidências)
{checklist_md}

---

## 3) Métricas simples (baseadas em dados de defeitos)
- Total de defeitos: **{total}**
- Defeitos encontrados em teste: **{teste}**
- Defeitos encontrados em produção: **{prod}**
- MTTR (tempo médio de correção): **{mttr:.2f} dias**
- MTTR (somente gravidade alta): **{mttr_altas:.2f} dias**

**Interpretação (para discussão em sala):**
- Quanto maior o número de defeitos em produção, maior o risco operacional.
- MTTR alto sugere gargalo de diagnóstico, priorização ou correção.
- Métricas isoladas não “provam” qualidade, mas guiam decisão.

---

## 4) Tabela de defeitos (evidência)
| ID | Gravidade | Origem | Aberto em | Fechado em | Tempo (dias) |
|---:|:---------:|:------:|:---------:|:----------:|-------------:|
{linhas_defeitos}

---

## 5) Conclusão (ligação com a teoria)
- **Normas** dão linguagem comum e padronizam o processo.
- **Maturidade** é previsibilidade e controle (não “perfeição”).
- **Evidências e relatórios** são fundamentais para auditoria e melhoria.
"""

    caminho_saida = Path(caminho_saida)
    caminho_saida.write_text(md, encoding="utf-8")
    return caminho_saida


def main() -> None:
    # Checklist didático: você pode ligar/desligar itens em sala
    checklist = {
        "Processo de teste documentado": False,
        "Casos de teste revisados": False,
        "Critérios de entrada/saída definidos": False,
        "Execução repetível (rotina)": True,
        "Automação aplicada com critério": True,
        "Métricas de qualidade coletadas": True,
        "Relatórios gerados e arquivados": True,
        "Melhoria contínua baseada em dados": False,
    }

    defeitos = carregar_defeitos("dados_defeitos.csv")
    nivel, desc = avaliar_maturidade(checklist)
    saida = gerar_relatorio_md(defeitos, nivel, desc, checklist)
    print(f"[OK] Relatório gerado: {saida.resolve()}")


if __name__ == "__main__":
    main()