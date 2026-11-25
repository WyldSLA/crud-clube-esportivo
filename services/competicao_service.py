def validar_premio(premio):
    if premio < 0:
        raise ValueError("Premiação não pode ser negativa.")
    
