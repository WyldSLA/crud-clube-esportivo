from repository import competicao_repository

def validar_premio(premio):
    if premio < 0:
        raise ValueError("Premiação não pode ser negativa.")

def cadastrar_competicao(nome, local, data, premio):

    validar_premio(premio)
    
    dados = {
        "nome": nome,
        "local": local,
        "data": data,
        "premio": premio
    }
    return competicao_repository.inserir_competicao(dados)

def atualizar_competicao(id_competicao, nome, local, data, premio):

    validar_premio(premio)
    
    dados = {
        "nome": nome,
        "local": local,
        "data": data,
        "premio": premio
    }
    return competicao_repository.atualizar_competicao(id_competicao, dados)
