def calcular_descuento(monto_usd):
    if monto_usd < 0:
        raise ValueError("El monto no puede ser negativo")

    if monto_usd < 100:
        return 0
    elif monto_usd >= 10000:
        return monto_usd * 0.13
    elif monto_usd >= 1000:
        return monto_usd * 0.10
    return 0


def convertir_a_clp(monto_usd, valor_dolar):
    return monto_usd * valor_dolar


def calcular_iva(monto_clp):
    return monto_clp * 0.19


def calcular_total(monto_usd, valor_dolar):
    if monto_usd < 0:
        raise ValueError("Monto inválido")

    descuento = calcular_descuento(monto_usd)
    neto_usd = monto_usd - descuento

    neto_clp = convertir_a_clp(neto_usd, valor_dolar)
    iva = calcular_iva(neto_clp)

    total = neto_clp + iva

    return {
        "usd": monto_usd,
        "descuento": descuento,
        "neto_clp": neto_clp,
        "iva": iva,
        "total": total
    }
