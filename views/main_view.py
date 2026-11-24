def menuInicial() -> str:
    print("=" * 44)
    print("SISTEMA DE GESTÃO ESPORTIVA".center(44))
    print("=" * 44)

    opcs = ["Gerenciar Atletas", "Gerenciar Competições", "Consultar Inscrições por Competição"]

    for i, opc in enumerate(opcs, start=1):
        print(f"[{i}] {opc}")

    print("=" * 44)
    print("[0] Sair")

    return input("Opção > ").strip()