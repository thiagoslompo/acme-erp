def calcular_icms(valor_nota, estado_destino):
    # Correcao ACME-1: aplica aliquota interestadual dinamica
    aliquota = 0.12 if estado_destino != "MG" else 0.18
    return valor_nota * aliquota
