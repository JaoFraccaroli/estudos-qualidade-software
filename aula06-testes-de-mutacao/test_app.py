# test_app.py
# from app import eh_aprovado


# def test_aprovado_basico():
#     assert eh_aprovado(7.0) is True
#     assert eh_aprovado(5.0) is False

# test_app.py
from app import eh_aprovado


def test_aprovado_limite():
    assert eh_aprovado(5.9) is False
    assert eh_aprovado(6.0) is True
    assert eh_aprovado(6.1) is True
