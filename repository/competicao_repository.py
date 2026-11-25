from database.conexao import conectar


def inserir_competicao(nome, modalidade, data):
    """Cadastra uma competição."""
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = """
            INSERT INTO competicao (nome, modalidade, data)
            VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (nome, modalidade, data))
        conexao.commit()
        return cursor.lastrowid
    except Exception:
        conexao.rollback()
        raise
    finally:
        cursor.close()
        conexao.close()


def listar_competicoes():
    """Retorna todas as competições como uma lista de dicionários."""
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM competicao")
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()


def buscar_competicao(id_competicao):
    """Busca uma competição pelo ID."""
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT * FROM competicao WHERE id_competicao = %s",
            (id_competicao,)
        )
        return cursor.fetchone()
    finally:
        cursor.close()
        conexao.close()


def atualizar_competicao(id_competicao, nome, modalidade, data):
    """Atualiza os dados de uma competição."""
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = """
            UPDATE competicao
            SET nome = %s, modalidade = %s, data = %s
            WHERE id_competicao = %s
        """
        cursor.execute(sql, (nome, modalidade, data, id_competicao))
        conexao.commit()
        return cursor.rowcount
    except Exception:
        conexao.rollback()
        raise
    finally:
        cursor.close()
        conexao.close()


def excluir_competicao(id_competicao):
    """Exclui uma competição pelo ID."""
    conexao = conectar()
    cursor = conexao.cursor()
    try:
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
