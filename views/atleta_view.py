def formatar_cpf(cpf: str) -> str:
    cpf_limpo = ''.join(filter(str.isdigit, str(cpf)))
    if len(cpf_limpo) == 11:
        return f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"
    return cpf

def menuAtletas() -> str:
    print("-" * 44)
    print("GESTÃO DE ATLETAS".center(44))
    print("-" * 44)

    opcs = ["Cadastrar Atleta", "Listar Todos os Atletas", "Atualizar Dados do Atleta", "Remover Atleta"]

    for i, opc in enumerate(opcs, start=1):
        print(f"[{i}] {opc}")

    print("[0] Voltar ao Menu Principal")
    print("=" * 44)

    return input("Opção > ").strip()

def menuCadastroAtleta() -> dict | None:
    print("\n--- CADASTRAR NOVO ATLETA ---")
    try: 
        nome = input("Nome Completo: ").strip()
        cpf = input("CPF (apenas números ou 000.000.000-00): ").strip()
        idade = int(input("Idade: "))
        id_competicao = int(input("Selecione a Competição (ID): "))
        
        return {
            "nome": nome,
            "cpf": cpf,
            "idade": idade,
            "id_competicao": id_competicao
        }

    except ValueError:
        print("\n[!] Erro: Idade e ID da Competição devem ser números inteiros válidos.")
        return None

def listarAtletasView(atletas: list[dict]):
    largura_tabela = 75
    print("\n" + "-" * largura_tabela)
    print(
        f"{'ID':<4} | "
        f"{'NOME':<25} | "
        f"{'CPF':<15} | "
        f"{'IDADE':<6} | "
        f"{'COMPETIÇÃO (ID)'}"
    )
    print("-" * largura_tabela)

    if not atletas:
        print(" NENHUM ATLETA CADASTRADO.".center(largura_tabela))
    else:
        for atleta in atletas:
            id_fmt = f"{atleta['id']:02d}"
            cpf_fmt = formatar_cpf(atleta['cpf'])
            
            if atleta.get('competicao_nome'):
                comp_fmt = f"{atleta['competicao_nome']} ({atleta['competicao_id']})"
            else:
                comp_fmt = "Sem Inscrição"

            nome_fmt = atleta['nome'][:25]

            print(
                f"{id_fmt:<4} | "
                f"{nome_fmt:<25} | "
                f"{cpf_fmt:<15} | "
                f"{atleta['idade']:<6} | "
                f"{comp_fmt}"
            )
    print("-" * largura_tabela)
    input("\nPressione ENTER para voltar...")

def menuAtualizarAtleta(atleta_atual: dict) -> dict | None:
    print(f"\n--- ATUALIZAR ATLETA (ID: {atleta_atual['id']:02d}) ---")
    print("(Pressione ENTER sem digitar nada para manter o valor atual)\n")

    try:
        nome = input(f"Nome [{atleta_atual['nome']}]: ").strip()
        if not nome:
            nome = atleta_atual['nome']

        cpf = input(f"CPF [{atleta_atual['cpf']}]: ").strip()
        if not cpf:
            cpf = atleta_atual['cpf']

        idade_input = input(f"Idade [{atleta_atual['idade']}]: ").strip()
        if not idade_input:
            idade = int(atleta_atual['idade'])
        else:
            idade = int(idade_input)

        return {
            "nome": nome,
            "cpf": cpf,
            "idade": idade
        }

    except ValueError:
        print("\n[!] Erro: A idade deve ser um número inteiro válido.")
        return None