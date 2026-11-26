from database.connection import conectar

def inserir_competicao(dados):
    conexao = conectar()
    if not conexao:
        return None
    cursor = conexao.cursor()

    try:
        sql = """
            INSERT INTO competicoes (nome, local, data, premio)
            VALUES (%s, %s, STR_TO_DATE(%s, '%d/%m/%Y'), %s)
        """
        cursor.execute(sql, (dados["nome"], dados["local"], dados["data"], dados["premio"]))
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
    if not conexao:
        return []
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT
                id,
                nome,
                local,
                DATE_FORMAT(data, '%d/%m/%Y') AS data,
                premio
            FROM competicoes
            ORDER BY id ASC
        """
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()

def buscar_competicao(id_competicao):
    conexao = conectar()
    if not conexao:
        return None
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT
                id,
                nome,
                local,
                DATE_FORMAT(data, '%d/%m/%Y') AS data,
                premio
            FROM competicoes
            WHERE id = %s
        """
        cursor.execute(sql, (id_competicao,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conexao.close()

def atualizar_competicao(id_competicao, dados):
    conexao = conectar()
    if not conexao:
        return 0
    cursor = conexao.cursor()

    try:
        sql = """
            UPDATE competicoes
            SET nome = %s, local = %s, data = STR_TO_DATE(%s, '%d/%m/%Y'), premio = %s
            WHERE id = %s
        """
        cursor.execute(sql, (dados["nome"], dados["local"], dados["data"], dados["premio"], id_competicao))
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
    if not conexao:
        return 0
    cursor = conexao.cursor()

    try:
        cursor.execute("DELETE FROM inscricoes WHERE id_competicao = %s", (id_competicao,))
        cursor.execute("DELETE FROM competicoes WHERE id = %s", (id_competicao,))
        conexao.commit()
        return cursor.rowcount
    except Exception:
        conexao.rollback()
        raise
    finally:
        cursor.close()
        conexao.close()