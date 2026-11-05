# test_app.py
from app import calcular_desconto, faixa_preco


def test_desconto_basico():
    assert calcular_desconto(100, 10) == 90.0


def test_percentual_limite_superior():
    assert calcular_desconto(100, 150) == 0.0  # 100% de desconto


def test_percentual_limite_inferior():
    assert calcular_desconto(100, -10) == 100.0  # vira 0%


def test_faixa_baixo():
    assert faixa_preco(49.99) == "baixo"


def test_faixa_medio():
    assert faixa_preco(50.00) == "medio"
    assert faixa_preco(199.99) == "medio"


def test_faixa_alto():
    assert faixa_preco(200.00) == "alto"