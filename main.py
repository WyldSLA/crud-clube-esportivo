from services import atleta_service, competicao_service, inscricao_service
from views import atleta_view, competicao_view, inscricoes_view, main_view


def gerenciar_atletas():
    while True:
        opc = atleta_view.menuAtletas()
        
        # 1. Cadastrar Atleta
        if opc == "1":
            dados = atleta_view.menuCadastroAtleta()
            if dados:
                try:
                    atleta_service.cadastrar_atleta(
                        dados["nome"], dados["cpf"], dados["idade"], dados["id_competicao"]
                    )
                    print("\n[✓] Atleta cadastrado com sucesso!")
                except ValueError as ve:
                    print(f"\n[!] Erro de Validação: {ve}")
                except Exception as e:
                    print(f"\n[❌] Erro no Banco de Dados: {e}")

        # 2. Listar Todos os Atletas
        elif opc == "2":
            atletas = atleta_service.listar_todos_atletas()
            atleta_view.listarAtletasView(atletas)

        # 3. Atualizar Dados do Atleta
        elif opc == "3":
            try:
                id_atleta = int(input("\nID do Atleta a atualizar: "))
                dados = atleta_view.menuCadastroAtleta()
                if dados:
                    if atleta_service.atualizar_atleta(
                        id_atleta, dados["nome"], dados["cpf"], dados["idade"], dados["id_competicao"]
                    ): 
                        print("\n[✓] Atleta atualizado com sucesso!")
                    else:
                        print("\n[!] Atleta não encontrado.")
            except ValueError as ve:
                print(f"\n[!] Erro de Validação: {ve}")

        # 4. Remover Atleta
        elif opc == "4":
            try:
                id_atleta = int(input("\nID do Atleta a ser removido: "))
                if atleta_service.remover_atleta(id_atleta):
                    print("\n[✓] Atleta e inscrição removidos com sucesso!")
                else:
                    print("\n[!] Atleta não encontrado.")
            except ValueError:
                print("\n[!] Digite um ID numérico válido.")
            except Exception as e:
                print(f"\n[❌] Erro ao remover: {e}")

        # 0. Voltar
        elif opc == "0":
            break
        else:
            print("\n[!] Opção inválida. Tente novamente.")


def gerenciar_competicoes():
    while True:
        opc = competicao_view.menuCompeticoes()
        
        # 1. Cadastrar Competição
        if opc == "1":
            dados = competicao_view.menuCadastroCompeticao()
            if dados:
                try:
                    competicao_service.cadastrar_competicao(
                        dados["nome"], dados["local"], dados["data"], dados["premio"]
                    )
                    print("\n[✓] Competição cadastrada com sucesso!")
                except ValueError as ve:
                    print(f"\n[!] Erro de Validação: {ve}")
                except Exception as e:
                    print(f"\n[❌] Erro no Banco de Dados: {e}")

        # 2. Listar Competições
        elif opc == "2":
            competicoes = competicao_service.listar_todas_competicoes()
            competicao_view.listarCompeticoesView(competicoes)

        # 3. Atualizar Competição
        elif opc == "3":
            try:
                id_comp = int(input("\nID da Competição a atualizar: "))
                dados = competicao_view.menuCadastroCompeticao()
                if dados:
                    if competicao_service.atualizar_competicao(
                        id_comp, dados["nome"], dados["local"], dados["data"], dados["premio"]
                    ):
                        print("\n[✓] Competição atualizada com sucesso!")
                    else:
                        print("\n[!] Competição não encontrada.")
            except ValueError as ve:
                print(f"\n[!] Erro de Validação: {ve}")

        # 4. Remover Competição
        elif opc == "4":
            try:
                id_comp = int(input("\nID da Competição a ser removida: "))
                if competicao_service.remover_competicao(id_comp):
                    print("\n[✓] Competição e inscrições associadas removidas com sucesso!")
                else:
                    print("\n[!] Competição não encontrada.")
            except ValueError:
                print("\n[!] Digite um ID numérico válido.")
            except Exception as e:
                print(f"\n[❌] Erro ao remover: {e}")

        # 0. Voltar
        elif opc == "0":
            break
        else:
            print("\n[!] Opção inválida. Tente novamente.")


def consultar_inscricoes():
    try:
        id_comp = int(input("\nInforme o ID da Competição: "))
        comp, atletas = inscricao_service.listar_atletas_por_competicao(id_comp)
        inscricoes_view.visualizarInscritosCompeticaoView(comp, atletas)
    except ValueError as ve:
        print(f"\n[!] Aviso: {ve}")
    except Exception as e:
        print(f"\n[❌] Erro ao consultar inscrições: {e}")


def main():
    while True:
        opc = main_view.menuInicial()
        
        if opc == "1":
            gerenciar_atletas()
        elif opc == "2":
            gerenciar_competicoes()
        elif opc == "3":
            consultar_inscricoes()
        elif opc == "0":
            print("\nEncerrando o Sistema de Gestão Esportiva...")
            break
        else:
            print("\n[!] Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()