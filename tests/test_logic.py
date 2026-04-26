import pytest
from logic import calcular_descuento_usd, calcular_iva_clp

def test_descuento_alto():
    # Más de 10000 USD debe dar 13%
    assert calcular_descuento_usd(20000) == 2600.0

def test_descuento_medio():
    # Entre 1000 y 10000 USD debe dar 10%
    assert calcular_descuento_usd(1500) == 150.0

def test_sin_descuento():
    assert calcular_descuento_usd(500) == 0.0

def test_iva():
    # El IVA de 1000 debe ser 190
    assert calcular_iva_clp(1000) == 190.0

    