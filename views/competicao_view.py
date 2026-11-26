def menuCompeticoes() -> str:
    print("-" * 44)
    print("GESTÃO DE COMPETIÇÕES".center(44))
    print("-" * 44)

    opcs = [
        "Cadastrar Competição", 
        "Listar Competições", 
        "Atualizar Competição", 
        "Remover Competição"
    ]

    for i, opc in enumerate(opcs, start=1):
        print(f"[{i}] {opc}")

    print("[0] Voltar ao Menu Principal")
    print("=" * 44)

    return input("Opção > ").strip()

def menuCadastroCompeticao() -> dict | None:
    print("\n--- CADASTRAR NOVA COMPETIÇÃO ---")
    try:
        nome = input("Nome da Competição: ").strip()
        local = input("Local: ").strip()
        data = input("Data (DD/MM/AAAA): ").strip()
        premio = float(input("Valor do Prêmio (R$): "))

        return {
            "nome": nome,
            "local": local,
            "data": data,
            "premio": premio
        }
    except ValueError:
        print("\n[!] Erro: O valor do prêmio deve ser um número válido (ex: 1500.00).")
        return None

def listarCompeticoesView(competicoes: list[dict]):
    largura_tabela = 80
    print("\n" + "-" * largura_tabela)
    print(
        f"{'ID':<4} | "
        f"{'COMPETIÇÃO':<25} | "
        f"{'LOCAL':<20} | "
        f"{'DATA':<12} | "
        f"{'PRÊMIO (R$)'}"
    )
    print("-" * largura_tabela)

    if not competicoes:
        print(" NENHUMA COMPETIÇÃO CADASTRADA.".center(largura_tabela))
    else:
        for comp in competicoes:
            id_fmt = f"{comp['id']:02d}"
            nome_fmt = comp['nome'][:25]
            local_fmt = comp['local'][:20]
            val_premio = float(comp['premio'])
            premio_fmt = f"R$ {val_premio:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

            print(
                f"{id_fmt:<4} | "
                f"{nome_fmt:<25} | "
                f"{local_fmt:<20} | "
                f"{comp['data']:<12} | "
                f"{premio_fmt}"
            )

    print("-" * largura_tabela)
    input("\nPressione ENTER para voltar...")

def menuAtualizarCompeticao(competicao_atual: dict) -> dict | None:
    print(f"\n--- ATUALIZAR COMPETIÇÃO (ID: {competicao_atual['id']:02d}) ---")
    print("(Pressione ENTER sem digitar nada para manter o valor atual)\n")

    try:
        nome = input(f"Nome [{competicao_atual['nome']}]: ").strip()
        if not nome:
            nome = competicao_atual['nome']

        local = input(f"Local [{competicao_atual['local']}]: ").strip()
        if not local:
            local = competicao_atual['local']

        data = input(f"Data [{competicao_atual['data']}]: ").strip()
        if not data:
            data = competicao_atual['data']

        premio_input = input(f"Prêmio [{competicao_atual['premio']}]: ").strip()
        if not premio_input:
            premio = float(competicao_atual['premio'])
        else:
            premio = float(premio_input)

        return {
            "nome": nome,
            "local": local,
            "data": data,
            "premio": premio
        }

    except ValueError:
        print("\n[!] Erro: O valor do prêmio deve ser um número válido.")
        return None