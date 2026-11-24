def formatar_cpf(cpf: str) -> str:
    cpf_limpo = ''.join(filter(str.isdigit, cpf))
    if len(cpf_limpo) == 11:
        return f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"
    return cpf

def menuAtleta():
    print("-" * 44)
    print("GESTAO DE ATLETAS".center(44))
    print("-" * 44)

    opcs = ["Cadastrar Atleta", "Listar Todos os Atletas", "Atualizar Dados do Atleta", "Remover Atleta"]

    for i, opc in enumerate(opcs, start=1):
        print(f"[{i}] {opc}")

    print("=" * 44)
    print("[0] Voltar ao Menu Principal")

    return input("Opção > ")

def menuCadastroAtleta():
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

def listarAtletasView(atleas: list[dict]):
    print("\n" + "-" * 90)
    print(
        f"{'ID':<4} | "
        f"{'NOME':<20} | "
        f"{'CPF':<15} | "
        f"{'IDADE':<6} | "
        f"{'MODALIDADE':<14} | "
        f"{'COMPETIÇÃO (ID)'}"
    )
    print("-" * 90)

    if not atleas:
        print(" NENHUM ATLETA CADASTRADO.".center(90))
    else:
        for atleta in atleas:

            id_fmt = f"{atleta['id']:02d}"
            cpf_fmt = formatar_cpf(str(atleta['cpf']))
            comp_fmt = f"{atleta['competicao_nome']} ({atleta['competicao_id']})"

            nome_fmt = atleta['nome'][:20]
            modalidade_fmt = atleta['modalidade'][:14]

            print(
                f"{id_fmt:<4} | "
                f"{nome_fmt:<20} | "
                f"{cpf_fmt:<15} | "
                f"{atleta['idade']:<6} | "
                f"{modalidade_fmt:<14} | "
                f"{comp_fmt}"
            )
    print("-" * 90)
    input("\nPressione ENTER para voltar...")