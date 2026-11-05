# test_app.py
from app import media_aprovacao, aprovado

def test_media_basica():
    # Este teste é fraco: só testa um caso "bonitinho"
    assert media_aprovacao([6, 8]) == 7.0

def test_aprovacao_basica():
    # Outro teste básico que passa, mas não garante qualidade
    assert aprovado(6.0) is True
    assert aprovado(5.9) is False