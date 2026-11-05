# Estudos de Qualidade de Software

![Testes](https://github.com/JaoFraccaroli/estudos-qualidade-software/actions/workflows/testes.yml/badge.svg)

Exercícios práticos da disciplina de **Qualidade de Software** do curso de Engenharia da Computação. Cada pasta trata de um tema de teste de software, com código em **Python** e testes automatizados com **pytest**.

> O código base dos exercícios foi fornecido em aula, muitas vezes com defeitos colocados de propósito para serem encontrados pelos testes.

## Conteúdo

| Pasta | Tema | O que tem |
|---|---|---|
| [`aula01-qualidade-de-software`](aula01-qualidade-de-software) | Introdução à qualidade | Função de média com erros conceituais e testes "fracos" que mesmo assim passam: mostra por que cobertura de casos importa |
| [`aula02-automacao-de-testes`](aula02-automacao-de-testes) | Automação de testes | Cálculo de frete testado com pytest e script que guarda evidências da execução |
| [`aula03-maturidade-e-metricas`](aula03-maturidade-e-metricas) | Normas e maturidade | Diagnóstico de maturidade do processo de teste e métricas de defeitos (MTTR, defeitos em produção x em teste), com relatório gerado em Markdown |
| [`aula04-execucao-automatica`](aula04-execucao-automatica) | Execução automática | Testes de limites (valores de fronteira), relatório JUnit XML e cobertura com pytest-cov |
| [`aula04-testes-dirigidos-por-dados`](aula04-testes-dirigidos-por-dados) | Testes dirigidos por dados | 90 casos gerados com seed fixa (limites + aleatórios) em CSV e executados automaticamente |
| [`aula06-testes-de-mutacao`](aula06-testes-de-mutacao) | Teste de mutação | Script que cria mutantes do código, roda os testes e mostra se eles "matam" cada mutante |
| [`aula06-mutacao-didatica`](aula06-mutacao-didatica) | Teste de mutação | 8 mutantes e cálculo do *mutation score* para medir a força dos testes |
| [`aula08-depuracao`](aula08-depuracao) | Depuração | Localização de um defeito de cálculo de desconto a partir dos testes que falham |

## Defeitos encontrados pelos testes

Alguns testes falham **de propósito**, porque o código tem defeitos que o exercício pede para encontrar. Eles estão marcados com `@pytest.mark.xfail(strict=True)`: o teste documenta o defeito e, se alguém corrigir o código, o pytest avisa para atualizar o teste.

| Onde | Defeito |
|---|---|
| Aula 02 | A regra diz frete grátis **a partir de** R$ 200 (`>=`), mas o código usa `> 200` |
| Aula 08 | O desconto usa o percentual inteiro (10) em vez da fração (0,10): um desconto de 10% deixa o preço negativo |

Ao organizar o repositório, também encontrei um problema no **próprio executor de testes** da aula 04: ele comparava o resultado com tolerância de `1e-9`, mas o valor esperado no CSV tem só 2 casas decimais. Isso gerava **39 falsas falhas** em 90 casos. Com a comparação ajustada para 2 casas, os 90 casos passam, e o script agora retorna erro quando algum caso falha (para o CI detectar).

## Como rodar

```bash
pip install -r requirements.txt
cd aula02-automacao-de-testes
pytest -v
```

Todos os testes rodam automaticamente no **GitHub Actions** a cada push.
