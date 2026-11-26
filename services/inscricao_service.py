from repository import atleta_repository, competicao_repository, inscricao_repository

def validar_competicao(id_competicao):
    if id_competicao < 1:
        raise ValueError("ID inválido, digite um número maior que zero.")
        
    competicao = competicao_repository.buscar_competicao(id_competicao)
    if competicao is None:
        raise ValueError("A competição informada não existe no banco de dados.")

def listar_atletas_por_competicao(id_competicao):
    validar_competicao(id_competicao)
    competicao = competicao_repository.buscar_competicao(id_competicao)
    atletas = inscricao_repository.listar_atletas_por_competicao(id_competicao)
    return competicao, atletas