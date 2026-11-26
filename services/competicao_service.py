from repository import competicao_repository

def validar_premio(premio):
    if premio < 0:
        raise ValueError("Premiação não pode ser negativa.")

def cadastrar_competicao(nome, local, data, premio):
    validar_premio(premio)
    dados = {
        "nome": nome.strip(),
        "local": local.strip(),
        "data": data.strip(),
        "premio": premio
    }
    return competicao_repository.inserir_competicao(dados)

def listar_todas_competicoes():
    return competicao_repository.listar_competicoes()

def atualizar_competicao(id_competicao, nome, local, data, premio):
    validar_premio(premio)
    dados = {
        "nome": nome.strip(),
        "local": local.strip(),
        "data": data.strip(),
        "premio": premio
    }
    return competicao_repository.atualizar_competicao(id_competicao, dados)

def remover_competicao(id_competicao):
    return competicao_repository.excluir_competicao(id_competicao)

def buscar_competicao(id_competicao):
    return competicao_repository.buscar_competicao(id_competicao)