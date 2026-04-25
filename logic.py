def calcular_descuento_usd(monto_usd):
    """Calcula el descuento según los tramos del profesor."""
    if monto_usd > 10000:
        return monto_usd * 0.13  # 13% de descuento 
    elif monto_usd >= 1000:
        return monto_usd * 0.10  # 10% de descuento 
    return 0.0  # Menor a 100 USD es 0% 

def calcular_iva_clp(monto_neto_clp):
    """Aplica el IVA del 19% exigido."""
    return monto_neto_clp * 0.19  # IVA 19% 

def convertir_a_clp(monto_usd, valor_dolar):
    """Convierte USD a CLP según el valor del día."""
    return monto_usd * valor_dolar 
