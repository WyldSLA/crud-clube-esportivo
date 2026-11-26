# 🏆 Sistema de Gestão Esportiva — Projeto CRUD 2026.2

> **Disciplina:** Coding
>
> **Curso:** Análise e Desenvolvimento de Sistemas (ADS) — 2º Período / Turma A
>
> **Instituição:** UNINASSAU Caruaru
>
> **Professor:** Leonardo Cordeiro de Araújo

## 📌 Sobre o Projeto

O **Sistema de Gestão Esportiva** é uma aplicação em linha de comando (CLI) desenvolvida em **Python** integrada ao banco de dados relacional **MySQL**. O sistema permite a gestão completa das entidades **Competições** e **Atletas**, estabelecendo um relacionamento do tipo **1:N (Um para Muitos)** através da entidade **Inscrições**.

O projeto atende a todos os requisitos solicitados na disciplina, aplicando conceitos de programação modular, validações de regra de negócio, tratamento de exceções (`try/except/finally`), manipulação de listas e dicionários, e controle de versão obrigatório via **Git/GitHub**.

## 🏛️ Arquitetura do Sistema (Layered Architecture)

A aplicação foi organizada em 4 camadas bem delimitadas para garantir modularidade, manutenibilidade e facilidade de testes:

```
projeto_crud_esportes/
├── main.py                    # Ponto de entrada e orquestração dos menus
├── database/
│   ├── connection.py          # Conexão MySQL e inicialização automática do banco
│   └── schema.sql             # Script DDL com a estrutura do banco e FKs (1:N)
├── repository/                # Camada de Acesso a Dados (SQL Puro com dictionary=True)
│   ├── atleta_repository.py
│   ├── competicao_repository.py
│   └── inscricao_repository.py
├── services/                  # Camada de Negócio e Validações de Regras
│   ├── atleta_service.py      # Validação de CPF e Idade Mínima
│   ├── competicao_service.py  # Validação de Prêmio Monetário
│   └── inscricao_service.py   # Validação de Integridade Referencial
└── views/                     # Camada de Interface CLI e Tabelas Formatadas
    ├── atleta_view.py
    ├── competicao_view.py
    ├── inscricoes_view.py
    └── main_view.py
```

## 🗄️ Modelo do Banco de Dados (Relacionamento 1:N)

* **Competições (1):** Armazena `id`, `nome`, `local`, `data` e `premio` (R\$).
* **Atletas (N):** Armazena `id`, `nome`, `cpf` (único) e `idade`.
* **Inscrições:** Tabela associativa que vincula múltiplos atletas a cada competição através de Chaves Estrangeiras (`FOREIGN KEY`) com suporte a deleção em cascata (`ON DELETE CASCADE`).

## 🛠️ Requisitos e Pré-requisitos

* **Python 3.10+**
* **MySQL Server 8.0+**
* Dependências Python:
  * `mysql-connector-python`
  * `python-dotenv`

## 🚀 Como Executar o Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Configurar o Ambiente Virtual (Opcional, mas recomendado)

```bash
python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

### 3. Instalar as Dependências

```bash
pip install mysql-connector-python python-dotenv
```

### 4. Configurar as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto contendo as credenciais de acesso ao seu MySQL:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha_aqui
DB_NAME=gestao_esportiva
```

### 5. Executar a Aplicação

```bash
python main.py
```

> *Nota: Ao rodar o `main.py`, o script verificará e criará as tabelas no MySQL automaticamente caso ainda não existam no seu banco de dados.*

## 📋 Funcionalidades Implementadas

### 🏅 Competições (CRUD Completo)

* [x] **Cadastrar:** Inserção com validação de prêmio não negativo.
* [x] **Listar:** Exibição em tabela com formatação de moeda (`R$`).
* [x] **Atualizar:** Edição com preenchimento opcional (tecla `ENTER` para manter o dado atual).
* [x] **Excluir:** Remoção com deleção em cascata nas inscrições.

### 🏃 Atletas (CRUD Completo)

* [x] **Cadastrar:** Inserção com validação matemática dos 11 dígitos do **CPF** e **idade mínima de 18 anos**.
* [x] **Listar:** Exibição em tabela com máscara de CPF (`000.000.000-00`).
* [x] **Atualizar:** Edição preservando dados não alterados via `ENTER`.
* [x] **Excluir:** Remoção individual de atleta do sistema.

### 🔗 Inscrições (Demonstração 1:N)

* [x] **Consulta de Inscritos:** Relatório visual por competição exibindo o cabeçalho da prova e a lista formatada de todos os atletas vinculados.

## 👥 Equipe de Desenvolvimento

* **Wyldson Marllon Lima Oliveira:** Banco de Dados (`schema.sql`, `connection.py`) & Interface do Usuário CLI (`views/`)
* **Davisson Ruann Marinho:** Orquestração da Aplicação (`main.py`)
* **Marcell César Machado de Oliveira:** Camada de Dados e Persistência (`repository/`)
* **Matheus Felipe da Silva:** Camada de Negócio e Validações (`services/`)

## 📄 Licença

Este projeto é de uso acadêmico exclusivo para avaliação na disciplina de Coding da **UNINASSAU Caruaru**.