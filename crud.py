from db import conectar 

def listar_alunos(nome, idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute( 
                "SELECT * FROM alunos ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f'erro ao listar {erro}')
            return[]
        finally:
            cursor.close()
            conexao.close()


