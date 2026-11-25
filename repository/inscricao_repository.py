from database.conexao import conectar


def inserir_inscricao(id_atleta, id_competicao):
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
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT
                i.id_atleta,
                i.id_competicao,
                a.nome AS nome_atleta,
                c.nome AS nome_competicao
            FROM inscricao i
            INNER JOIN atleta a
                ON i.id_atleta = a.id_atleta
            INNER JOIN competicao c
                ON i.id_competicao = c.id_competicao
        """

        cursor.execute(sql)
        return cursor.fetchall()

    finally:
        cursor.close()
        conexao.close()


def listar_atletas_por_competicao(id_competicao):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT
                a.id_atleta AS id,
                a.nome,
                a.cpf,
                a.idade
            FROM inscricao i
            INNER JOIN atleta a
                ON i.id_atleta = a.id_atleta
            WHERE i.id_competicao = %s
        """

        cursor.execute(sql, (id_competicao,))
        return cursor.fetchall()

    finally:
        cursor.close()
        conexao.close()


def excluir_inscricao(id_atleta, id_competicao):
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
