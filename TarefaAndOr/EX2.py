#2 - Escreva um programa que peça ao usuário inserir duas notas (entre 0 e 100) e determine se o aluno passou ou não. Um aluno passa se a soma das notas for maior ou igual a 60 e nenhuma nota é menor que 40.

nota1 = float(input("Digite a primeira nota sendo entre 0 e 100: "))
nota2 = float(input("Digite a segunda nota sendo entre 0 e 100: "))
sum_notas = nota1 + nota2


if sum_notas >= 60 and nota1 >= 40 and nota2 >= 40:
    print("O aluno passou!")
else:
    print("O aluno não passou.")