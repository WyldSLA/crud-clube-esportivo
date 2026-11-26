from repository import atleta_repository
from services.inscricao_service import validar_competicao

def validar_cpf(cpf): 

    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11: 
        raise ValueError("CPF deve conter 11 dígitos.")
    if not cpf.isdigit(): 
        raise ValueError("CPF deve conter apenas números.")
    if cpf == cpf[0]* 11: 
        raise ValueError("CPF Inválido")


    soma = 0 
    for indice in range(9): 
        numero = int(cpf[indice])
        peso= 10 - indice
        soma += numero * peso
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto


    soma2 = 0
    for indice in range(10): 
        numero = int(cpf[indice])
        peso = 11 - indice
        soma2 += numero * peso
    resto2 = soma2 % 11
    if resto2 < 2: 
        digito2 = 0
    else: 
        digito2 = 11 - resto2
    
    if int(cpf[9]) != digito1 or int(cpf[10]) != digito2:
        raise ValueError("CPF Inválido")


def validar_idade(idade):
    if idade < 18: 
        raise ValueError("Idade insuficiente.")


def cadastrar_atleta(nome, cpf, idade, id_competicao):
    cpf = cpf.replace(".", "").replace("-", "")
    validar_cpf(cpf)
    validar_idade(idade)
    validar_competicao(id_competicao)

    dados = {
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "id_competicao": id_competicao
    }
    return atleta_repository.inserir_atleta(dados)
