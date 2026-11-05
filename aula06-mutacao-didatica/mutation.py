"""
Aula: Teste de Mutação em Python
Objetivo:
    Demonstrar, de forma didática, como o teste de mutação funciona.

Conceitos abordados:
    - Função original
    - Casos de teste
    - Mutantes
    - Mutante vivo x mutante morto
    - Mutation score
    - Importância de testes de fronteira
    - Interpretação da força do conjunto de testes

Observação:
    Este script NÃO depende de pytest.
    Ele foi feito para ser autoexplicativo e executável diretamente.
"""

from dataclasses import dataclass
from typing import Callable, List, Tuple


# ============================================================
# 1. FUNÇÃO ORIGINAL DO SISTEMA
# ============================================================

def classificar_aluno_original(media: float) -> str:
    """
    Regra de negócio:
    - média >= 7.0  -> Aprovado
    - média < 7.0   -> Reprovado
    """
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"


# ============================================================
# 2. DEFINIÇÃO DOS MUTANTES
# ============================================================

def mutante_a(media: float) -> str:
    """
    Mutação na fronteira:
    troca >= por >
    Erro clássico de fronteira.
    """
    if media > 7.0:
        return "Aprovado"
    else:
        return "Reprovado"


def mutante_b(media: float) -> str:
    """
    Mutação no retorno do ramo verdadeiro.
    """
    if media >= 7.0:
        return "Reprovado"
    else:
        return "Reprovado"


def mutante_c(media: float) -> str:
    """
    Mutação no retorno do ramo falso.
    """
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Aprovado"


def mutante_d(media: float) -> str:
    """
    Mutação no limiar da regra:
    troca 7.0 por 6.0
    """
    if media >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"


def mutante_e(media: float) -> str:
    """
    Mutação mais drástica:
    condição invertida.
    """
    if media < 7.0:
        return "Aprovado"
    else:
        return "Reprovado"


def mutante_f(media: float) -> str:
    """
    Mutação com pequeno deslocamento numérico.
    Pode sobreviver dependendo do conjunto de testes.
    """
    if media >= 7.1:
        return "Aprovado"
    else:
        return "Reprovado"


def mutante_g(media: float) -> str:
    """
    Mutação lógica sutil:
    arredondamento implícito que altera comportamento.
    """
    if round(media) >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


def mutante_h(media: float) -> str:
    """
    Mutação que cria uma regra incorreta para médias negativas.
    """
    if media < 0:
        return "Aprovado"
    elif media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"


# ============================================================
# 3. ESTRUTURAS DE DADOS
# ============================================================

@dataclass
class CasoDeTeste:
    nome: str
    entrada: float
    esperado: str


@dataclass
class Mutante:
    nome: str
    funcao: Callable[[float], str]
    descricao: str


@dataclass
class ResultadoTeste:
    nome_teste: str
    passou: bool
    esperado: str
    obtido: str


@dataclass
class ResultadoMutante:
    nome_mutante: str
    descricao: str
    resultados_testes: List[ResultadoTeste]
    morto: bool


# ============================================================
# 4. CONJUNTOS DE TESTES
# ============================================================

def obter_testes_fracos() -> List[CasoDeTeste]:
    """
    Conjunto inicial de testes:
    cobre apenas um caso de aprovação e um de reprovação.
    É propositalmente fraco para mostrar mutantes sobrevivendo.
    """
    return [
        CasoDeTeste(
            nome="teste_aprovado_basico",
            entrada=8.0,
            esperado="Aprovado"
        ),
        CasoDeTeste(
            nome="teste_reprovado_basico",
            entrada=5.0,
            esperado="Reprovado"
        ),
    ]


def obter_testes_fortes() -> List[CasoDeTeste]:
    """
    Conjunto ampliado:
    inclui fronteiras, vizinhança do limite e caso inválido.
    """
    return [
        CasoDeTeste(
            nome="teste_aprovado_basico",
            entrada=8.0,
            esperado="Aprovado"
        ),
        CasoDeTeste(
            nome="teste_reprovado_basico",
            entrada=5.0,
            esperado="Reprovado"
        ),
        CasoDeTeste(
            nome="teste_limite_exato",
            entrada=7.0,
            esperado="Aprovado"
        ),
        CasoDeTeste(
            nome="teste_abaixo_do_limite",
            entrada=6.9,
            esperado="Reprovado"
        ),
        CasoDeTeste(
            nome="teste_acima_do_limite",
            entrada=7.1,
            esperado="Aprovado"
        ),
        CasoDeTeste(
            nome="teste_media_baixa_mas_valida",
            entrada=6.0,
            esperado="Reprovado"
        ),
        CasoDeTeste(
            nome="teste_media_muito_alta",
            entrada=10.0,
            esperado="Aprovado"
        ),
        CasoDeTeste(
            nome="teste_media_negativa",
            entrada=-1.0,
            esperado="Reprovado"
        ),
    ]


# ============================================================
# 5. EXECUÇÃO DOS TESTES
# ============================================================

def executar_testes(
    funcao: Callable[[float], str],
    testes: List[CasoDeTeste]
) -> List[ResultadoTeste]:
    """
    Executa todos os testes contra uma função qualquer
    (original ou mutante).
    """
    resultados = []

    for teste in testes:
        obtido = funcao(teste.entrada)
        passou = obtido == teste.esperado

        resultados.append(
            ResultadoTeste(
                nome_teste=teste.nome,
                passou=passou,
                esperado=teste.esperado,
                obtido=obtido
            )
        )

    return resultados


def avaliar_mutante(mutante: Mutante, testes: List[CasoDeTeste]) -> ResultadoMutante:
    """
    Um mutante é considerado morto se pelo menos um teste falhar.
    Se todos os testes passarem, ele sobrevive.
    """
    resultados = executar_testes(mutante.funcao, testes)
    morto = any(not r.passou for r in resultados)

    return ResultadoMutante(
        nome_mutante=mutante.nome,
        descricao=mutante.descricao,
        resultados_testes=resultados,
        morto=morto
    )


# ============================================================
# 6. CÁLCULO DO MUTATION SCORE
# ============================================================

def calcular_mutation_score(resultados: List[ResultadoMutante]) -> float:
    """
    Mutation Score = mutantes mortos / total de mutantes * 100
    """
    if not resultados:
        return 0.0

    mortos = sum(1 for r in resultados if r.morto)
    total = len(resultados)
    return (mortos / total) * 100.0


# ============================================================
# 7. RELATÓRIOS
# ============================================================

def imprimir_linha(tamanho: int = 70) -> None:
    print("-" * tamanho)


def imprimir_relatorio_funcao_original(testes: List[CasoDeTeste]) -> None:
    """
    Mostra se a função original atende ao conjunto de testes.
    """
    print("\nRELATÓRIO DA FUNÇÃO ORIGINAL")
    imprimir_linha()

    resultados = executar_testes(classificar_aluno_original, testes)

    for r in resultados:
        status = "PASSOU" if r.passou else "FALHOU"
        print(
            f"{r.nome_teste:30s} | {status:6s} | "
            f"esperado={r.esperado:10s} | obtido={r.obtido}"
        )

    imprimir_linha()
    todos_passaram = all(r.passou for r in resultados)
    print(
        f"Resultado geral da função original: {'OK' if todos_passaram else 'PROBLEMA'}")


def imprimir_relatorio_mutante(resultado: ResultadoMutante) -> None:
    """
    Exibe o relatório detalhado de um mutante.
    """
    status_mutante = "MORTO" if resultado.morto else "VIVO"

    print(f"\nMutante: {resultado.nome_mutante}")
    print(f"Descrição: {resultado.descricao}")
    print(f"Classificação: {status_mutante}")
    imprimir_linha()

    for r in resultado.resultados_testes:
        status_teste = "PASSOU" if r.passou else "FALHOU"
        print(
            f"{r.nome_teste:30s} | {status_teste:6s} | "
            f"esperado={r.esperado:10s} | obtido={r.obtido}"
        )


def imprimir_resumo_geral(resultados: List[ResultadoMutante]) -> None:
    """
    Resumo final dos mutantes.
    """
    print("\nRESUMO GERAL DOS MUTANTES")
    imprimir_linha()

    for r in resultados:
        status = "MORTO" if r.morto else "VIVO"
        print(f"{r.nome_mutante:12s} | {status:5s} | {r.descricao}")

    imprimir_linha()

    score = calcular_mutation_score(resultados)
    mortos = sum(1 for r in resultados if r.morto)
    vivos = len(resultados) - mortos

    print(f"Total de mutantes: {len(resultados)}")
    print(f"Mutantes mortos : {mortos}")
    print(f"Mutantes vivos  : {vivos}")
    print(f"Mutation Score  : {score:.2f}%")

    if score < 50:
        interpretacao = "Conjunto de testes fraco."
    elif score < 75:
        interpretacao = "Conjunto de testes razoável, mas com lacunas."
    elif score < 90:
        interpretacao = "Conjunto de testes bom."
    else:
        interpretacao = "Conjunto de testes muito forte."

    print(f"Interpretação   : {interpretacao}")


# ============================================================
# 8. LISTA DE MUTANTES
# ============================================================

def obter_mutantes() -> List[Mutante]:
    return [
        Mutante(
            nome="Mutante_A",
            funcao=mutante_a,
            descricao="Troca >= por > (erro de fronteira)."
        ),
        Mutante(
            nome="Mutante_B",
            funcao=mutante_b,
            descricao="Altera retorno do ramo verdadeiro."
        ),
        Mutante(
            nome="Mutante_C",
            funcao=mutante_c,
            descricao="Altera retorno do ramo falso."
        ),
        Mutante(
            nome="Mutante_D",
            funcao=mutante_d,
            descricao="Troca o limiar 7.0 por 6.0."
        ),
        Mutante(
            nome="Mutante_E",
            funcao=mutante_e,
            descricao="Inverte a lógica da condição."
        ),
        Mutante(
            nome="Mutante_F",
            funcao=mutante_f,
            descricao="Desloca discretamente o limite para 7.1."
        ),
        Mutante(
            nome="Mutante_G",
            funcao=mutante_g,
            descricao="Usa arredondamento antes de comparar."
        ),
        Mutante(
            nome="Mutante_H",
            funcao=mutante_h,
            descricao="Cria regra incorreta para médias negativas."
        ),
    ]


# ============================================================
# 9. EXPERIMENTO COMPLETO
# ============================================================

def executar_experimento(nome_cenario: str, testes: List[CasoDeTeste]) -> None:
    """
    Executa todo o experimento de mutação para um conjunto de testes.
    """
    print("\n" + "=" * 70)
    print(f"CENÁRIO: {nome_cenario}")
    print("=" * 70)

    imprimir_relatorio_funcao_original(testes)

    resultados_mutantes = []
    for mutante in obter_mutantes():
        resultado = avaliar_mutante(mutante, testes)
        resultados_mutantes.append(resultado)
        imprimir_relatorio_mutante(resultado)

    imprimir_resumo_geral(resultados_mutantes)


# ============================================================
# 10. FUNÇÃO PRINCIPAL
# ============================================================

def main() -> None:
    """
    Executa dois cenários:
    1) testes fracos
    2) testes fortalecidos

    Assim, o aluno consegue visualizar como o mutation score muda.
    """
    testes_fracos = obter_testes_fracos()
    testes_fortes = obter_testes_fortes()

    executar_experimento(
        nome_cenario="Conjunto de Testes Inicial (Fraco)",
        testes=testes_fracos
    )

    executar_experimento(
        nome_cenario="Conjunto de Testes Ampliado (Mais Forte)",
        testes=testes_fortes
    )


if __name__ == "__main__":
    main()
