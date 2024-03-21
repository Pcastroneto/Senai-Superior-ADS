from classes.LivroDAO import LivroDAO
class MenuLivros:
    def __init__(self):
        self.dao = LivroDAO() 
    
    def exibir_menu(self):
        print("--- MENU ---")
        print("1. Listar Livros")
        print("2. Buscar Livro")
        print("3. Inserir Livro")
        print("4. Atualizar Livro")
        print("5. Excluir Livro")
        print("0. Sair")
	
    def listar_livros(self):
        livros = self.dao.listar_livros()
        if livros:
    	    print("Livros:")
    	    for livro in livros:
    	        print(f"Código: {livro[0]}, Nome: {livro[1]}, Ano: {livro[2]}, Data/Hora do Cadastro: {livro[3]}")
        else:
    	    print("Nenhum livro encontrado.")
    
    def buscar_livro(self):
	    codLivro = input("Digite o código do livro que deseja buscar: ")
	    livro = self.dao.buscar_livro(codLivro)
	    if livro:
		    print(f"Código: {livro[0]}, Nome: {livro[1]}, Ano: {livro[2]}, Data/Hora do Cadastro: {livro[3]}")
	    else:
	        print("Livro não encontrado.") 
	 
    def inserir_livro(self):
        nomeLivro = input("Digite o nome do livro: ")
        anoLivro = input("Digite o ano do livro: ")
        self.dao.inserir_livro(nomeLivro, anoLivro)
        print("Livro inserido com sucesso.")
        
    def atualizar_livro(self):
        codLivro = input("Digite o código do livro que deseja atualizar: ")
        nomeLivro = input("Digite o novo nome do livro: ")
        anoLivro = input("Digite o novo ano do livro: ")
        self.dao.atualizar_livro(codLivro, nomeLivro, anoLivro)
        print("Livro atualizado com sucesso.")
    
    def excluir_livro(self):
	    codLivro = input("Digite o código do livro que deseja excluir: ")
	    self.dao.excluir_livro(codLivro)
	    print("Livro excluído com sucesso.") 

    def executar(self):
	    while True:
	        self.exibir_menu()
	        opcao = input("Digite a opção desejada: ")
	        if opcao == "1":
	            self.listar_livros()
	        elif opcao == "2":
	            self.buscar_livro()
	        elif opcao == "3":
	            self.inserir_livro()
	        elif opcao == "4":
	            self.atualizar_livro()
	        elif opcao == "5":
	            self.excluir_livro()
	        elif opcao == "0":
	            print("Encerrando o programa.")
	            break
	        else:
	            print("Opção inválida. Digite novamente.")