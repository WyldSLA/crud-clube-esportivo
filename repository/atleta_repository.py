from database.connection import conectar

def inserir_atleta(dados):
    conexao = conectar()
    if not conexao:
        return None
    cursor = conexao.cursor()

    try:
        sql = "INSERT INTO atletas (nome, cpf, idade) VALUES (%s, %s, %s)"
        cursor.execute(sql, (dados["nome"], dados["cpf"], dados["idade"]))
        id_atleta = cursor.lastrowid

        sql_inscricao = "INSERT INTO inscricoes (id_atleta, id_competicao) VALUES (%s, %s)"
        cursor.execute(sql_inscricao, (id_atleta, dados["id_competicao"]))

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
    if not conexao:
        return []
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT
                a.id,
                a.nome,
                a.cpf,
                a.idade,
                c.id AS competicao_id,
                c.nome AS competicao_nome
            FROM atletas a
            LEFT JOIN inscricoes i ON a.id = i.id_atleta
            LEFT JOIN competicoes c ON i.id_competicao = c.id
            ORDER BY a.id ASC
        """
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()

def buscar_atleta(id_atleta):
    conexao = conectar()
    if not conexao:
        return None
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT
                a.id,
                a.nome,
                a.cpf,
                a.idade,
                c.id AS competicao_id,
                c.nome AS competicao_nome
            FROM atletas a
            LEFT JOIN inscricoes i ON a.id = i.id_atleta
            LEFT JOIN competicoes c ON i.id_competicao = c.id
            WHERE a.id = %s
        """
        cursor.execute(sql, (id_atleta,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conexao.close()

def atualizar_atleta(id_atleta, dados):
    conexao = conectar()
    if not conexao:
        return 0
    cursor = conexao.cursor()

    try:
        sql = "UPDATE atletas SET nome = %s, cpf = %s, idade = %s WHERE id = %s"
        cursor.execute(sql, (dados["nome"], dados["cpf"], dados["idade"], id_atleta))
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
    if not conexao:
        return 0
    cursor = conexao.cursor()

    try:
        cursor.execute("DELETE FROM inscricoes WHERE id_atleta = %s", (id_atleta,))
        cursor.execute("DELETE FROM atletas WHERE id = %s", (id_atleta,))
        conexao.commit()
        return cursor.rowcount
    except Exception:
        conexao.rollback()
        raise
    finally:
        cursor.close()
        conexao.close()


from database.connection import conectar

def inserir_atleta(dados):
    conexao = conectar()
    if not conexao:
        return None
    cursor = conexao.cursor()

    try:
        sql = "INSERT INTO atletas (nome, cpf, idade) VALUES (%s, %s, %s)"
        cursor.execute(sql, (dados["nome"], dados["cpf"], dados["idade"]))
        id_atleta = cursor.lastrowid

        sql_inscricao = "INSERT INTO inscricoes (id_atleta, id_competicao) VALUES (%s, %s)"
        cursor.execute(sql_inscricao, (id_atleta, dados["id_competicao"]))

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
    if not conexao:
        return []
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT
                a.id,
                a.nome,
                a.cpf,
                a.idade,
                c.id AS competicao_id,
                c.nome AS competicao_nome
            FROM atletas a
            LEFT JOIN inscricoes i ON a.id = i.id_atleta
            LEFT JOIN competicoes c ON i.id_competicao = c.id
            ORDER BY a.id ASC
        """
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()

def buscar_atleta(id_atleta):
    conexao = conectar()
    if not conexao:
        return None
    cursor = conexao.cursor(dictionary=True)

    try:
        sql = """
            SELECT
                a.id,
                a.nome,
                a.cpf,
                a.idade,
                c.id AS competicao_id,
                c.nome AS competicao_nome
            FROM atletas a
            LEFT JOIN inscricoes i ON a.id = i.id_atleta
            LEFT JOIN competicoes c ON i.id_competicao = c.id
            WHERE a.id = %s
        """
        cursor.execute(sql, (id_atleta,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conexao.close()

def atualizar_atleta(id_atleta, dados):
    conexao = conectar()
    if not conexao:
        return 0
    cursor = conexao.cursor()

    try:
        sql = "UPDATE atletas SET nome = %s, cpf = %s, idade = %s WHERE id = %s"
        
        if "id_competicao" in dados and dados["id_competicao"]:
            sql_inscricao = "UPDATE inscricoes SET id_competicao = %s WHERE id_atleta = %s"
            cursor.execute(sql_inscricao, (dados["id_competicao"], id_atleta))
        
        cursor.execute(sql, (dados["nome"], dados["cpf"], dados["idade"], id_atleta))
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
    if not conexao:
        return 0
    cursor = conexao.cursor()

    try:
        cursor.execute("DELETE FROM inscricoes WHERE id_atleta = %s", (id_atleta,))
        cursor.execute("DELETE FROM atletas WHERE id = %s", (id_atleta,))
        conexao.commit()
        return cursor.rowcount
    except Exception:
        conexao.rollback()
        raise
    finally:
        cursor.close()
        conexao.close()
