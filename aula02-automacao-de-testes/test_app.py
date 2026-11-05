# test_app.py
import pytest
from app import calcular_frete


def test_frete_base_cliente_normal():
    assert calcular_frete(50, False) == 20.0


def test_frete_vip_paga_metade():
    assert calcular_frete(50, True) == 10.0


@pytest.mark.xfail(strict=True, reason="Defeito encontrado: a regra diz frete grátis a partir de 200 (>=), mas o código usa > 200")
def test_frete_gratis_acima_de_200():
    assert calcular_frete(200, False) == 0.0
    assert calcular_frete(500, True) == 0.0


def test_valor_invalido():
    with pytest.raises(ValueError):
        calcular_frete(-1, False)