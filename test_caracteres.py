# test_caracteres.py

import pytest
from caracteres import Caracteres

car = Caracteres()

def test_mayusculas():
    assert car.mayusculas('semaforo') == 'SEMAFORO'

def test_ultimos_4_caracteres():
    assert car.ultimos_4('pytest') == 'test'

# def test_raises_exception_usando_numeros_en_vez_de_caracteres():
#     with pytest.raises(TypeError):
#         car.mayusculas(123)