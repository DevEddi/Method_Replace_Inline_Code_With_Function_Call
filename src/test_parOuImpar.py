import pytest
import app

def test_answer_impar():
    assert app.verificaParouImpar(7) == 'Número ímpar'


def test_answer_par():
    assert app.verificaParouImpar(16) == 'Número par'

