# CRUD COM POSTGRESQL + PYTHON

| Tecnologia   | Descrição                         |
|--------------|----------------------------------|
| PostgreSQL   | Banco de dados relacional         |
| psycopg2     | Driver para conexão com PostgreSQL |
| Streamlit    | Framework web para aplicações rápidas |
| Python       | Linguagem de programação          |

## Como executar

### 1. Clonar o repositório
```bash
git clone https://github.com/Kaua-santos/aula-postgresql.git

### 2. Criar ambiente virtual (opcinal)
```bash
python -m venv .venv
.venv\Scripts\activate #windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```


### 4. Configurar variáveis de ambiente
crie um arquivo .env na raiz do projeto com:

DB_NAME=nome_banco

DB_USER=postgres

DB_PASSWORD=sua_senha

DB_HOST=localhost

DB_PORT=5432

### 5. Rodar aplicação
```bash
python -m streamlit run app.py
```

### Funcionalidades

- Conexão com o banco
- Criar alunos
- Listar alunos
- Atualizar alunos
- Deletar alunos
- interface simples no streamlit 

### Autor 
Projeto desenvolvido em aula para treinar python + postgresql

Professor: Gabriel Brito de sousa