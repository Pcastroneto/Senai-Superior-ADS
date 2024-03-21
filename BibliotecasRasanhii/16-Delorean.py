'''
Delorean é uma biblioteca Python para manipulação de datas e tempos. 
Ele permite que os usuários manipulem datas e horários com facilidade, incluindo a conversão entre fusos horários e o cálculo de diferenças de tempo.
'''

import delorean
import datetime

dt = delorean.Delorean(datetime=datetime.datetime(2023, 5, 8, 20, 30, 0), timezone="America/Sao_Paulo")

print(dt)

