def visualizarInscritosCompeticaoView(competicao: dict, atletas: list[dict]):
    print("\n" + "=" * 70)
    print(f" COMPETIÇÃO: {competicao['nome'].upper()} (ID: {competicao['id']:02d})".center(70))
    print(f" Local: {competicao['local']} | Data: {competicao['data']} | Prêmio: R$ {competicao['premio']:,.2f}".center(70))
    print("=" * 70)
    
    print("\nATLETAS INSCRITOS:")
    print("-" * 70)

    if not atletas:
        print(" Nenhum atleta inscrito nesta competição até o momento.")
    else:
        print(f"{'ID':<4} | {'NOME DO ATLETA':<30} | {'CPF':<15} | {'IDADE':<6}")
        print("-" * 70)
        for atleta in atletas:
            id_fmt = f"{atleta['id']:02d}"
            print(
                f"{id_fmt:<4} | "
                f"{atleta['nome'][:30]:<30} | "
                f"{atleta['cpf']:<15} | "
                f"{atleta['idade']:<6}"
            )

    print("-" * 70)
    print(f"Total de inscrições nesta competição: {len(atletas)}")
    print("=" * 70)
    input("\nPressione ENTER para voltar ao menu...")