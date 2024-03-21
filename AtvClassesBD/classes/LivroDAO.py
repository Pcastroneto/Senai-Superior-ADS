import mysql.connector
from classes.conexao import conectar
class LivroDAO:
    def __init__(self):
        self.conexao = conectar()

    def listar_livros(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT * FROM tbLivro")
            livros = cursor.fetchall()
            return livros
        except mysql.connector.Error as erro:
            print(f"Erro ao listar livros: {erro}")
        finally:
            cursor.close()
    
    def buscar_livro(self, codLivro):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT * FROM tbLivro WHERE codLivro = %s", (codLivro,))
            livro = cursor.fetchone()
            return livro
        except mysql.connector.Error as erro:
            print(f"Erro ao buscar livro: {erro}")
        finally:
            cursor.close()
    
    def inserir_livro(self, nomeLivro, anoLivro):
        try:
            cursor = self.conexao.cursor()
            query = "INSERT INTO tbLivro (nomeLivro, anoLivro) VALUES (%s, %s)"
            valores = (nomeLivro, anoLivro)
            cursor.execute(query, valores)
            self.conexao.commit()
            print("Livro inserido com sucesso.")
        except mysql.connector.Error as erro:
            print(f"Erro ao inserir livro: {erro}")
        finally:
            cursor.close()

    def atualizar_livro(self, codLivro, nomeLivro, anoLivro):
        try:
            cursor = self.conexao.cursor()
            query = "UPDATE tbLivro SET nomeLivro = %s, anoLivro = %s WHERE codLivro = %s"
            valores = (nomeLivro, anoLivro, codLivro)
            cursor.execute(query, valores)
            self.conexao.commit()
            print("Livro atualizado com sucesso.")
        except mysql.connector.Error as erro:
            print(f"Erro ao atualizar livro: {erro}")
        finally:
            cursor.close()
            
    def excluir_livro(self, codLivro):
        try:
            cursor = self.conexao.cursor()
            query = "DELETE FROM tbLivro WHERE codLivro = %s"
            valores = (codLivro,)
            cursor.execute(query, valores)
            self.conexao.commit()
            print("Livro excluído com sucesso.")
        except mysql.connector.Error as erro:
            print(f"Erro ao excluir livro: {erro}")
        finally:
            cursor.close()