def gerar_sugestoes_avancado(mercado=None, min_odd=1.5, time=None):
    base = [
        {"partida": "Flamengo x Vasco", "mercado": "mais_2.5", "odd": 1.85, "time": "Flamengo", "confianca": "Alta"},
        {"partida": "Palmeiras x Corinthians", "mercado": "ambos_marcam", "odd": 1.75, "time": "Corinthians", "confianca": "Moderada"},
        {"partida": "São Paulo x Santos", "mercado": "mais_1.5", "odd": 1.65, "time": "São Paulo", "confianca": "Alta"}
    ]
    resultado = []
    for item in base:
        if mercado and mercado not in item["mercado"]:
            continue
        if time and time.lower() not in item["time"].lower():
            continue
        if item["odd"] < min_odd:
            continue
        resultado.append(item)
    return resultado