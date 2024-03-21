ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento

if idade >= 16:
    print("Você pode votar este ano.")
else:
    print("Você não pode votar este ano.")