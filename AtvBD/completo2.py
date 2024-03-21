from conexao2 import conectar

def listar(conn, cursor):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    
    cursor = conn.cursor()

    # Executar a consulta SQL para listar os registros
    cursor.execute("SELECT * FROM animais_nat")

    # Obter os resultados
    resultados = cursor.fetchall()

    # Imprimir os resultados
    for resultado in resultados:
        print(resultado)

    # Fechar a conexão e o cursor
    cursor.close()
    conn.close()


def inserir(raca,quant,risco,area):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para inserir um novo registro
    sql = "INSERT INTO animais_nat (raça,quant,risco,area) VALUES (%s, %s,%s,%s)"
    val = (raca,quant,risco,area)
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
    sql = "DELETE FROM animais_nat WHERE id = %s"
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

def atu_raca(codigo,nova_raca):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE animais_nat SET raça = %s WHERE id = %s"
    val = (nova_raca, codigo)
    cursor.execute(sql, val)
    conn.commit()
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")
        
    cursor.close()
    conn.close()
    
def atu_quant(codigo,nova_quant):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE animais_nat SET quant = %s WHERE id = %s"
    val = (nova_quant, codigo)
    cursor.execute(sql, val)
    conn.commit()
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")
        
    cursor.close()
    conn.close()

def atu_risco(codigo,novo_risco):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE animais_nat SET risco = %s WHERE id = %s"
    val = (novo_risco, codigo)
    cursor.execute(sql, val)
    conn.commit()
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")
        
    cursor.close()
    conn.close()
        
def atu_area(codigo,nova_area):
    conn = conectar()
    cursor = conn.cursor()
    sql = "UPDATE animais_nat SET area = %s WHERE id = %s"
    val = (nova_area, codigo)
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
  print("1 - Listar animais")
  print("2 - Inserir um novo animal")
  print("3 - Deletar um animal")
  print("4- Atualizar informação")
  print("0 - Sair")
  
  opcao = int(input("Digite o número da opção desejada: "))

  if opcao == 1:
    print("Esses são os animais que foram inseridas: \n")
    listar(conn, cursor)
  
  elif opcao == 2:
    
    raca = input("Digite a raça do animal: ")
    quant = int(input("Digite a quantidade de animais: "))
    risco = input("Possuem risco de extinção? (sim ou não)? ")
    area =input("Qual área eles são encontrados (norte, sul, leste ou oeste)?")
    
    
    inserir(raca,quant,risco,area)

  elif opcao == 3:
    
    codigo = int(input("Digite o id do animal que deseja deletar: "))
    deletar(codigo)
  
  elif opcao ==4:
    codigo = int(input("Digite o código do animal que deseja atualizar: "))
    
    print("Qual informação deseja alterar?")
    print("1 - Raça")
    print("2 - Quantidade")
    print("3 - Risco de extinção")
    print("4 - Área encontrada")
    
    escolha = int(input("Digite o número da opção desejada: "))
    
    if escolha ==1:
      nova_raca = input("Digite a raça do animal: ")
      atu_raca(codigo,nova_raca)
      
    elif escolha ==2:
      nova_quant = int(input("Digite a quantidade de animais: "))
      atu_quant(codigo,nova_quant)
      
    elif escolha ==3:
      novo_risco = input("Possuem risco de extinção? (sim ou não)? ")
      atu_risco(codigo, novo_risco)
    elif escolha ==4:
      nova_area =input("Qual área eles são encontrados (norte, sul, leste ou oeste)?")
      atu_area(codigo,nova_area)
      
    else:
      break 
    

  elif opcao == 0:
    
    break

  else:
    print("Opção inválida. Digite novamente.")
    
# Fechar a conexão e o cursor
cursor.close()
conn.close()