'''
Fire é uma biblioteca feita para gerar automaticamente interfaces de linha de comando (CLIs) com uma única linha de código. 
Ele transformará qualquer módulo Python, classe, objeto, função, etc. em uma CLI. 
Exemplo:
'''

import fire

class Calculator:
    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

if __name__ == '__main__':
    fire.Fire(Calculator)

'''
Neste exemplo, estamos criando uma classe chamada Calculator que possui dois métodos: add e multiply. 
Em seguida, estamos usando a função fire.Fire() para tornar os métodos da classe disponíveis na linha de comando. 
Quando executamos o script, podemos chamar os métodos da classe diretamente a partir do terminal.
'''