import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="aulanoite123",
        database="livro"
        )
    return mydb