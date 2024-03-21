print("Cadastro de clientes: \n0 - Fim \n1 - Inclui \n2 - Altera \n3 - Exclui \n4 - Consulta")
menu = int(input())

if menu == 0:
    print("Fim")

if menu == 1:
    print("Inclui")

if menu == 2:
    print("Altera")

if menu == 3:
    print("Exclui")

if menu == 4:
    print("Consulta")

if menu < 0 or menu > 4:
    print("item não encontrado.")