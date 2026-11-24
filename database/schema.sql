CREATE TABLE IF NOT EXISTS atletas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cpf CHAR(14) UNIQUE NOT NULL,
    idade INT,
    premio VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS competicoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    local VARCHAR(255),
    data DATE,
    modalidade VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS inscricoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_atleta INT NOT NULL,
    id_competicao INT NOT NULL,

    FOREIGN KEY (id_atleta) REFERENCES atletas(id),
    FOREIGN KEY (id_competicao) REFERENCES competicoes(id)
);
