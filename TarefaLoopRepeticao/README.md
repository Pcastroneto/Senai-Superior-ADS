# Tarefa-Loop
Tarefa Laços de Repetição

Os programas abaixo devem estar no github. Você pode usar While ou For.

0 - Peça para  o usuário entrar com dois valores (primeiro e último).
Faça a contagem entre esses números.
Caso o último for menor que  o primeiro faça a contagem decrescente.
Caso o último número for maior que o primeiro faça a contagem crescente.

1 - Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.

2 - Faça um programa que peça ao usuário para adivinhar um número entre 1 e 100.
Enquanto o número digitado não for igual a um número secreto definido pelo programa,
o programa deve pedir ao usuário que tente novamente. Quando o usuário acertar o número,
o programa deve imprimir "Parabéns, você acertou!".
Use a biblioteca abaixo para números aleatórios:
import random
numero_secreto = random.randint(1, 100)

3 - Faça um programa que peça ao usuário para digitar uma sequência de números inteiros.
O programa deve imprimir a soma dos números digitados, mas parar a soma se o usuário digitar um número negativo.

4 - Faça um programa que peça ao usuário para digitar o número de vezes que ele quer jogar uma moeda.
O programa deve simular o lançamento de uma moeda e imprimir o resultado de cada lançamento (cara ou coroa).
No final, o programa deve imprimir o número total de caras e o número total de coroas.
Use a biblioteca abaixo para números aleatórios:
import random
resultado = random.randint(0, 1)

5 - Faça um programa que simule a urna eletrônica.
A tela a ser apresentada deverá ser da seguinte forma:
As opcoes sao:
1. Candidato Jair Rodrigues
2. Candidato Carlos Luz
3. Candidato Neves Rocha
4. Nulo
5. Branco
Entre com o seu voto:
O programa deverá ler os votos dos eleitores e, quando for entrado o número 6, apresentar as seguintes
informações:
a) O número de votos de cada candidato;
b) A porcentagem de votos nulos;
c) A porcentagem de votos brancos;
d) O candidato vencedor.

6 - Faça um algoritmo em python capaz de realizar o cálculo de rentabilidade de uma poupança,
esse algoritmo deve receber como entrada o valor inicial que o usuário está disposto a guardar.
Como saída, o programa deve imprimir na tela mês a mês o montante por 12 meses
aplicado a uma taxa de 0,5 % ao mês de rentabilidade.

A fórmula do montante (M) de uma aplicação financeira é dada por:

M = P * (1 + i)^n

onde:

P é o capital inicial (ou principal)
i é a taxa de juros aplicada (em forma decimal) - divida o valor dado por 100
n é o número de períodos de tempo em que o dinheiro ficará investido.

7 - Faça um programa que mostre o fatorial de um número fornecido pelo usuário.