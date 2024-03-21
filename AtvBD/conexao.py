import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
        host = 'db-atv.cpcnfjng6gnj.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password= 'aulanoite123',
        database = 'tribos'
    )
    return mydb
    
 