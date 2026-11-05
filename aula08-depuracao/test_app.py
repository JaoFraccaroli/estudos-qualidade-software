# test_app.py
import pytest
from app import preco_com_desconto


@pytest.mark.xfail(strict=True, reason="Defeito encontrado: o desconto usa o percentual inteiro (10) em vez de fração (0.10)")
def test_desconto_10_porcento():
    assert preco_com_desconto(100, 10) == 90.00


@pytest.mark.xfail(strict=True, reason="Defeito encontrado: o desconto usa o percentual inteiro (10) em vez de fração (0.10)")
def test_limites_validos():
    assert preco_com_desconto(200, 0) == 200.00
    assert preco_com_desconto(200, 100) == 0.00


def test_entrada_invalida():
    with pytest.raises(ValueError):
        preco_com_desconto(-1, 10)
    with pytest.raises(ValueError):
        preco_com_desconto(100, -1)
    with pytest.raises(ValueError):
        preco_com_desconto(100, 101)
