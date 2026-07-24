print("===Lista de tarefas===")
tarefas = []

while True:
    escolha = int(input("1- Adicionar tarefa\n2- Ver tarefas\n3- Remover tarefa\n4- Sair\n"))
    
    if escolha == 1:
        nome_tarefa = input("Nome da tarefa: ")
        tarefas.append(nome_tarefa)
        print(f"Certo, {nome_tarefa} foi adicionado à lista de tarefas!")
    elif escolha == 2:
        for tarefa in tarefas:
            print(tarefa)
    elif escolha == 3:
        for tarefa in tarefas:
            print(tarefa)
        nome_tarefa = input("Nome da tarefa que você deseja remover: ")
        tarefas.remove(nome_tarefa)
    elif escolha == 4:
        print("Encerrando a lista")
        break
    else:
        print("Opção inválida!")