def identificar_intencao(mensagem):
    mensagem = mensagem.lower()

    if "olá" in mensagem or "oi" in mensagem:
        return "saudacao"

    if "horário" in mensagem or "funciona" in mensagem:
        return "horario"

    if "preço" in mensagem or "custa" in mensagem:
        return "preco"

    if "ajuda" in mensagem:
        return "ajuda"

    if "humano" in mensagem or "atendente" in mensagem:
        return "humano"

    return "desconhecido"