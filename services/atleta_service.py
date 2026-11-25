def validar_cpf(cpf): 

    if len(cpf) != 11: 
        raise ValueError("CPF deve conter 11 dígitos.")
    if not cpf.isdigit(): 
        raise ValueError("CPF deve conter apenas números.")

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
    
    if int(cpf[9]) != digito1 or int(cpf[10]) != digito2 or cpf == cpf[0]* 11:
        raise ValueError("CPF Inválido")

    

    return "CPF válido!"

def validar_idade(idade):
    if idade < 18: 
        raise ValueError("Idade insuficiente.")
