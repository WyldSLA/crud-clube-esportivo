from database.connection import conectar

def inserir_inscricao(id_atleta, id_competicao):
    conexao = conectar()
    if not conexao:
        return None
    cursor = conexao.cursor()

    try:
        sql = "INSERT INTO inscricoes (id_atleta, id_competicao) VALUES (%s, %s)"
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
    if not conexao:
        return []
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT
                i.id_atleta,
                i.id_competicao,
                a.nome AS nome_atleta,
                c.nome AS nome_competicao
            FROM inscricoes i
            INNER JOIN atletas a ON i.id_atleta = a.id
            INNER JOIN competicoes c ON i.id_competicao = c.id
        """
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()

def listar_atletas_por_competicao(id_competicao):
    conexao = conectar()
    if not conexao:
        return []
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT
                a.id,
                a.nome,
                a.cpf,
                a.idade
            FROM inscricoes i
            INNER JOIN atletas a ON i.id_atleta = a.id
            WHERE i.id_competicao = %s
            ORDER BY a.id ASC
        """
        cursor.execute(sql, (id_competicao,))
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()