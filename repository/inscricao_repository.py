from database.conexao import conectar


def inserir_inscricao(id_atleta, id_competicao):
    """Inscreve um atleta em uma competição."""
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = """
            INSERT INTO inscricao (id_atleta, id_competicao)
            VALUES (%s, %s)
        """
        cursor.execute(sql, (id_atleta, id_competicao))
        conexao.commit()
        return cursor.lastrowid
    except Exception:
        conexao.rollback()
        raise
    finally:
        cursor.close()
        conexao.close()


def listar_inscricoes():
    """Retorna todas as inscrições como uma lista de dicionários."""
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM inscricao")
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()


def listar_atletas_por_competicao(id_competicao):
    """
    Lista os atletas inscritos em uma competição específica.
    O resultado é uma lista de dicionários.
    """
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        sql = """
            SELECT
                atleta.id_atleta,
                atleta.nome,
                atleta.idade,
                atleta.modalidade,
                competicao.id_competicao,
                competicao.nome AS nome_competicao
            FROM inscricao
            INNER JOIN atleta
                ON inscricao.id_atleta = atleta.id_atleta
            INNER JOIN competicao
                ON inscricao.id_competicao = competicao.id_competicao
            WHERE competicao.id_competicao = %s
        """
        cursor.execute(sql, (id_competicao,))
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()


def excluir_inscricao(id_atleta, id_competicao):
    """Remove a inscrição de um atleta em uma competição."""
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = """
            DELETE FROM inscricao
            WHERE id_atleta = %s
              AND id_competicao = %s
        """
        cursor.execute(sql, (id_atleta, id_competicao))
        conexao.commit()
        return cursor.rowcount
    except Exception:
        conexao.rollback()
        raise
    finally:
        cursor.close()
        conexao.close()
