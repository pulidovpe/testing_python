# test_caracteres.py

import pytest
from caracteres import Caracteres

car = Caracteres()

def test_mayusculas():
    assert car.mayusculas('semaforo') == 'SEMAFORO'