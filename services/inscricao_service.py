from repository import atleta_repository
from repository import competicao_repository
from repository import inscricao_repository

def validar_competicao(id_competicao):

    if id_competicao < 1:
        raise ValueError("ID Inválido, digite um número maior que zero.")
        
    competicao = competicao_repository.buscar_competicao(id_competicao)
    if competicao is None:
        raise ValueError("Digite um ID de competição existente.")

def inscrever_atleta(id_atleta, id_competicao):
    
    if id_atleta < 1:
        raise ValueError("Digite um número acima de zero.")
    
    atleta = atleta_repository.buscar_atleta(id_atleta)

    if atleta is None: 
        raise ValueError("Atleta não encontrado.")

    validar_competicao(id_competicao)
    return inscricao_repository.inserir_inscricao(
        id_atleta, id_competicao
    )
