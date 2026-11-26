from repository import atleta_repository
from services.inscricao_service import validar_competicao

def validar_cpf(cpf): 
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11: 
        raise ValueError("CPF deve conter exatamente 11 dígitos.")
    if not cpf.isdigit(): 
        raise ValueError("CPF deve conter apenas números.")
    if cpf == cpf[0] * 11: 
        raise ValueError("CPF inválido.")

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2
    
    if int(cpf[9]) != digito1 or int(cpf[10]) != digito2:
        raise ValueError("CPF inválido.")

def validar_idade(idade):
    if idade < 18: 
        raise ValueError("Idade insuficiente (mínimo 18 anos).")

def cadastrar_atleta(nome, cpf, idade, id_competicao):
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    validar_cpf(cpf_limpo)
    validar_idade(idade)
    validar_competicao(id_competicao)

    dados = {
        "nome": nome.strip(),
        "cpf": cpf_limpo,
        "idade": idade,
        "id_competicao": id_competicao
    }
    return atleta_repository.inserir_atleta(dados)

def listar_todos_atletas():
    return atleta_repository.listar_atletas()

def remover_atleta(id_atleta):
    return atleta_repository.excluir_atleta(id_atleta)