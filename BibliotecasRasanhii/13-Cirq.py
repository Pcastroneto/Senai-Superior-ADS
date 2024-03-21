'''
Cirq é uma biblioteca Python para escrever, manipular e otimizar circuitos quânticos e
executá-los em computadores e simuladores quânticos.
Exemplo:


import cirq

# Define o circuito quântico
circuit = cirq.Circuit()
q0 = cirq.LineQubit(0)
q1 = cirq.LineQubit(1)
circuit.append(cirq.H(q0))
circuit.append(cirq.CNOT(q0, q1))
circuit.append(cirq.measure(q0, q1))

# Executa o circuito em um simulador
simulator = cirq.Simulator()
result = simulator.run(circuit)

# Imprime o resultado
print(result)


Neste exemplo, estamos criando um circuito quântico simples com dois qubits. 
Primeiro, aplicamos um gate H (Hadamard) no qubit 0, seguido por um gate CNOT entre os qubits 0 e 1. 
Por fim, medimos os dois qubits.
'''