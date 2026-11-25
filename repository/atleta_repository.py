from database.conexao import conectar


def inserir_atleta(dados):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = """
            INSERT INTO atleta (nome, cpf, idade)
            VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (
            dados["nome"],
            dados["cpf"],
            dados["idade"]
        ))

        id_atleta = cursor.lastrowid

        sql_inscricao = """
            INSERT INTO inscricao (id_atleta, id_competicao)
            VALUES (%s, %s)
        """

        cursor.execute(sql_inscricao, (
            id_atleta,
            dados["id_competicao"]
        ))

        conexao.commit()
        return id_atleta

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


def listar_atletas():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT
                a.id_atleta AS id,
                a.nome,
                a.cpf,
                a.idade,
                c.id_competicao AS competicao_id,
                c.nome AS competicao_nome
            FROM atleta a
            LEFT JOIN inscricao i
                ON a.id_atleta = i.id_atleta
            LEFT JOIN competicao c
                ON i.id_competicao = c.id_competicao
        """

        cursor.execute(sql)
        return cursor.fetchall()

    finally:
        cursor.close()
        conexao.close()


def buscar_atleta(id_atleta):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT
                a.id_atleta AS id,
                a.nome,
                a.cpf,
                a.idade,
                c.id_competicao AS competicao_id,
                c.nome AS competicao_nome
            FROM atleta a
            LEFT JOIN inscricao i
                ON a.id_atleta = i.id_atleta
            LEFT JOIN competicao c
                ON i.id_competicao = c.id_competicao
            WHERE a.id_atleta = %s
        """

        cursor.execute(sql, (id_atleta,))
        return cursor.fetchone()

    finally:
        cursor.close()
        conexao.close()


def atualizar_atleta(id_atleta, dados):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        sql = """
            UPDATE atleta
            SET nome = %s,
                cpf = %s,
                idade = %s
            WHERE id_atleta = %s
        """

        cursor.execute(sql, (
            dados["nome"],
            dados["cpf"],
            dados["idade"],
            id_atleta
        ))

        conexao.commit()
        return cursor.rowcount

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


def excluir_atleta(id_atleta):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            "DELETE FROM inscricao WHERE id_atleta = %s",
            (id_atleta,)
        )

        cursor.execute(
            "DELETE FROM atleta WHERE id_atleta = %s",
            (id_atleta,)
        )

        conexao.commit()
        return cursor.rowcount

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()
