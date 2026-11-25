from database.conexao import conectar


def inserir_competicao(dados):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = """
            INSERT INTO competicao (nome, local, data, premio)
            VALUES (%s, %s, STR_TO_DATE(%s, '%d/%m/%Y'), %s)
        """

        cursor.execute(sql, (
            dados["nome"],
            dados["local"],
            dados["data"],
            dados["premio"]
        ))

        conexao.commit()
        return cursor.lastrowid

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


def listar_competicoes():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT
                id_competicao AS id,
                nome,
                local,
                DATE_FORMAT(data, '%d/%m/%Y') AS data,
                premio
            FROM competicao
        """

        cursor.execute(sql)
        return cursor.fetchall()

    finally:
        cursor.close()
        conexao.close()


def buscar_competicao(id_competicao):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT
                id_competicao AS id,
                nome,
                local,
                DATE_FORMAT(data, '%d/%m/%Y') AS data,
                premio
            FROM competicao
            WHERE id_competicao = %s
        """

        cursor.execute(sql, (id_competicao,))
        return cursor.fetchone()

    finally:
        cursor.close()
        conexao.close()


def atualizar_competicao(id_competicao, dados):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = """
            UPDATE competicao
            SET nome = %s,
                local = %s,
                data = STR_TO_DATE(%s, '%d/%m/%Y'),
                premio = %s
            WHERE id_competicao = %s
        """

        cursor.execute(sql, (
            dados["nome"],
            dados["local"],
            dados["data"],
            dados["premio"],
            id_competicao
        ))

        conexao.commit()
        return cursor.rowcount

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


def excluir_competicao(id_competicao):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            "DELETE FROM inscricao WHERE id_competicao = %s",
            (id_competicao,)
        )

        cursor.execute(
            "DELETE FROM competicao WHERE id_competicao = %s",
            (id_competicao,)
        )

        conexao.commit()
        return cursor.rowcount

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()
