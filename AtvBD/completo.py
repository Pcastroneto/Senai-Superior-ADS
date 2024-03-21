from conexao import conectar

def listar(conn, cursor):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para listar os registros
    cursor.execute("SELECT * FROM tribo")

    # Obter os resultados
    resultados = cursor.fetchall()

    # Imprimir os resultados
    for resultado in resultados:
        print(resultado)

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()


def inserir(nome_tribo,num_hab,renda,escolaridade, trab_salar):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para inserir um novo registro
    sql = "INSERT INTO tribo (nome_tribo,num_hab,renda_mensal,escolaridade,trab_salar) VALUES (%s, %s,%s,%s,%s)"
    val = (nome_tribo,num_hab,renda,escolaridade,trab_salar)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Imprimir mensagem de sucesso
    print("Registro inserido com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()



def deletar(codigo):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para deletar o registro
    sql = "DELETE FROM tribo WHERE id = %s"
    val = (codigo,)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Verificar se algum registro foi deletado
    if cursor.rowcount == 0:
        print("Nenhum registro deletado.")
    else:
        print("Registro deletado com sucesso.")

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()
    
    
def atu_nome(codigo,novo_nome):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE tribo SET nome_tribo = %s WHERE id = %s"
    val = (novo_nome, codigo)
    cursor.execute(sql, val)
    conn.commit()
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")
        
    cursor.close()
    conn.close()
    
def atu_num(codigo,novo_num):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE tribo SET num_hab = %s WHERE id = %s"
    val = (novo_num, codigo)
    cursor.execute(sql, val)
    conn.commit()
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")
        
    cursor.close()
    conn.close()

def atu_renda(codigo,nova_renda):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE tribo SET renda_mensal = %s WHERE id = %s"
    val = (nova_renda, codigo)
    cursor.execute(sql, val)
    conn.commit()
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")
        
    cursor.close()
    conn.close()
def atu_esco(codigo,nova_esco):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE tribo SET escolaridade = %s WHERE id = %s"
    val = (nova_esco, codigo)
    cursor.execute(sql, val)
    conn.commit()
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")
        
    cursor.close()
    conn.close()
def atu_trab(codigo,novo_trab):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE tribo SET trab_salar = %s WHERE id = %s"
    val = (novo_trab, codigo)
    cursor.execute(sql, val)
    conn.commit()
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")
        
    cursor.close()
    conn.close()






# chama a função conectar
conn = conectar()
# Criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()
while True:
  # Mostra as opções de operação
  print("O que você deseja fazer?")
  print("1 - Listar tribos")
  print("2 - Inserir nova tribo")
  print("3 - Deletar uma tribo")
  print("4 - Atualizar informação")
  print("0 - Sair")
  
  opcao = int(input("Digite o número da opção desejada: "))

  if opcao == 1:
    print("Essas são as tribos que foram inseridas: ")
    listar(conn, cursor)
    print('')
  
  elif opcao == 2:
    
    nome_tribo = input("Digite o nome da tribo: ")
    num_hab = int(input("Digite o número de habitantes: "))
    renda = float(input("Digite a renda média mensal da tribo: "))
    escolaridade =input("Digite o nivel de escolaridade(Fundamental, médio ou superior): ")
    trab_salar = input("Possuem trabalho assalariado?(sim ou não): ")
    
    inserir(nome_tribo,num_hab,renda,escolaridade, trab_salar)

  elif opcao == 3:
    
    codigo = int(input("Digite o id da tribo que deseja deletar: "))
    deletar(codigo)
  
  elif opcao ==4:
    codigo = int(input("Digite o código da tribo que deseja atualizar: "))
    
    print("Qual informação deseja alterar?")
    print("1 - Nome da tribo")
    print("2 - Numero de habitantes")
    print("3 - Renda mensal")
    print("4 - Nivel de escolaridade")
    print("5 - Trabalho ou não assalariado")
    
    escolha = int(input("Digite o número da opção desejada: "))
    
    if escolha ==1:
      novo_nome = input("Digite o novo nome da tribo: ")
      atu_nome(codigo,novo_nome)
      
    elif escolha ==2:
      novo_num = int(input("Digite o novo número de habitantes: "))
      atu_num(codigo,novo_num)
      
    elif escolha ==3:
      nova_renda = float(input("Digite a nova renda média mensal da tribo: "))
      atu_renda(codigo,nova_renda)
      
    elif escolha ==4:
      nova_esco =input("Digite o novo nivel de escolaridade(Fundamental, médio ou superior): ")
      atu_esco(codigo,nova_esco)
      
    elif escolha ==5:
      novo_trab = input("Possuem trabalho assalariado?(sim ou não): ")
      atu_trab(codigo,novo_trab)

  elif opcao == 0:
    
    break

  else:
    print("Opção inválida. Digite novamente.")
    
# Fechar a conexão e o cursor
cursor.close()
conn.close()