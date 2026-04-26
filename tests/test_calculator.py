import pytest
from services.calculator import *


def test_descuentos():
    assert calcular_descuento(50) == 0
    assert calcular_descuento(1000) == 100
    assert calcular_descuento(10000) == 1300


def test_iva():
    assert calcular_iva(1000) == 190


def test_conversion():
    assert convertir_a_clp(10, 900) == 9000


def test_total():
    resultado = calcular_total(1000, 900)
    assert resultado["total"] > 0


def test_cero():
    resultado = calcular_total(0, 900)
    assert resultado["total"] == 0


def test_negativo():
    with pytest.raises(ValueError):
        calcular_total(-100, 900)


def test_limites():
    assert calcular_descuento(100) == 0
    assert calcular_descuento(1000) == 100
    assert calcular_descuento(10000) == 1300

    