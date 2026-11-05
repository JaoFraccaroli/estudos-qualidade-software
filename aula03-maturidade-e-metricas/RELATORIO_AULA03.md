# Relatório de Qualidade – Aula 03 (Normas e Maturidade)

## 1) Resultado do Diagnóstico de Maturidade (simulado)
**Nível estimado:** 3  
**Descrição:** Definido (processo padronizado/documentado)

> Observação: este diagnóstico é didático. Em modelos reais, existe avaliação formal.

---

## 2) Checklist de Processo (evidências)
- [ ] Processo de teste documentado
- [ ] Casos de teste revisados
- [ ] Critérios de entrada/saída definidos
- [x] Execução repetível (rotina)
- [x] Automação aplicada com critério
- [x] Métricas de qualidade coletadas
- [x] Relatórios gerados e arquivados
- [ ] Melhoria contínua baseada em dados

---

## 3) Métricas simples (baseadas em dados de defeitos)
- Total de defeitos: **6**
- Defeitos encontrados em teste: **3**
- Defeitos encontrados em produção: **3**
- MTTR (tempo médio de correção): **4.33 dias**
- MTTR (somente gravidade alta): **3.33 dias**

**Interpretação (para discussão em sala):**
- Quanto maior o número de defeitos em produção, maior o risco operacional.
- MTTR alto sugere gargalo de diagnóstico, priorização ou correção.
- Métricas isoladas não “provam” qualidade, mas guiam decisão.

---

## 4) Tabela de defeitos (evidência)
| ID | Gravidade | Origem | Aberto em | Fechado em | Tempo (dias) |
|---:|:---------:|:------:|:---------:|:----------:|-------------:|
| 1 | alta | producao | 2026-01-10 | 2026-01-11 | 1 |
| 2 | media | teste | 2026-01-12 | 2026-01-20 | 8 |
| 3 | alta | producao | 2026-01-15 | 2026-01-16 | 1 |
| 4 | baixa | teste | 2026-01-18 | 2026-01-25 | 7 |
| 5 | media | teste | 2026-01-22 | 2026-01-23 | 1 |
| 6 | alta | producao | 2026-01-25 | 2026-02-02 | 8 |

---

## 5) Conclusão (ligação com a teoria)
- **Normas** dão linguagem comum e padronizam o processo.
- **Maturidade** é previsibilidade e controle (não “perfeição”).
- **Evidências e relatórios** são fundamentais para auditoria e melhoria.
