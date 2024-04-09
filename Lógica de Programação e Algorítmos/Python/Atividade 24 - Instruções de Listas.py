tarefas = [ ]
tarefas.append("Acordar")
tarefas.append("Escovar os dentes")
tarefas.append("Café da Manhã")
tarefas.append("Ir a Escola")
tarefas.append("Fazer as atividades escolares")
tarefas.append("Pegar o ônibus")
tarefas.append("Voltar para a casa")
tarefas.append("Tomar banho")
tarefas.append("Jantar")
tarefas.append("Dormir")

tarefas = [ ]

for i in range(0,10):
    tarefa = input(f"Digite a tarefa número {i+1}:")
    tarefas.append(tarefa)
    print(tarefas)


tarefas = [ ]
contador = 0
while contador < 10:
    tarefa = input(f"Digite a tarefa número {contador + 1}:")
    tarefas.append(tarefa)
    contador += 1
    print(tarefas)

    frutas = []
    frutas.append("maçã")
    frutas.append("bergamota")
    frutas.append("banana")
    frutas.append("melão")
    frutas.append("laranja")
    print(frutas)
    frutas.pop(0)
    print(frutas)
    frutas.pop(-1)
    print(frutas)
    print(len(frutas[0]))
    frutas.clear()
    print(frutas)

    print(f"frutas selecionadas: {frutas[0]} e {frutas[2]}")
