import mysql.connector
# Definir as informações de conexão
config = {
  'user': 'usuarioremoto',
  'password': 'aulanoite123',
  'host': '34.224.51.159', #IP do banco
  'database': 'africa'
}
# Estabelecer a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")
# Fechar a conexão
conn.close()


def conectar():
    mydb = mysql.connector.connect(
        host = '34.224.51.159',
        user = 'usuarioremoto',
        password= 'aulanoite123',
        database = 'africa'
    )
    return mydb