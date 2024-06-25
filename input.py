import pandas as pd


pessoa = {}


Matricula = input('Digite sua Matrícula')
nome = input('Digite seu nome')
idade = input('Digite sua idade')
telefone = input('Digite seu telefone')
print(type(nome))
pessoa['nome'] = [nome]
pessoa['idade'] = [idade]
pessoa['Matricula'] = [Matricula]
pessoa['telefone'] = [telefone]

funcionario = pd.DataFrame(pessoa)

print(funcionario)