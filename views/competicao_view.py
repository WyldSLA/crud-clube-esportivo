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

    print("=" * 44)
    print("[0] Voltar ao Menu Principal")

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
    print("\n" + "-" * 90)
    print(
        f"{'ID':<4} | "
        f"{'COMPETIÇÃO':<25} | "
        f"{'LOCAL':<20} | "
        f"{'DATA':<12} | "
        f"{'PRÊMIO (R$)'}"
    )
    print("-" * 90)

    if not competicoes:
        print(" NENHUMA COMPETIÇÃO CADASTRADA.".center(90))
    else:
        for comp in competicoes:
            id_fmt = f"{comp['id']:02d}"
            nome_fmt = comp['nome'][:25]
            local_fmt = comp['local'][:20]
            premio_fmt = f"R$ {comp['premio']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

            print(
                f"{id_fmt:<4} | "
                f"{nome_fmt:<25} | "
                f"{local_fmt:<20} | "
                f"{comp['data']:<12} | "
                f"{premio_fmt}"
            )

    print("-" * 90)
    input("\nPressione ENTER para voltar...")