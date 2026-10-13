tarefas = []

def cadastrar_tarefa():
    print("\n--- Cadastrar Nova Tarefa ---")
    
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo == "":
            print("Erro: o título não pode ser vazio. Tente novamente.")
        else:
            break
    
    descricao = input("Descrição (opcional): ").strip()
    
    while True:
        prioridade = input("Prioridade (Alta / Média / Baixa): ").strip()
        if prioridade not in ["Alta", "Média", "Media", "Baixa"]:
            print("Erro: prioridade inválida. Digite Alta, Média ou Baixa.")
        else:
            break
    
    data_limite = input("Data limite (DD/MM/AAAA ou deixe em branco): ").strip()
    
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }
    
    tarefas.append(tarefa)
    print("\nTarefa cadastrada com sucesso!")

def visualizar_tarefas():
    print("\n--- Lista de Tarefas ---")
    
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada ainda.")
        return
    
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {i}:")
        print(f"  Título:      {tarefa['titulo']}")
        print(f"  Descrição:   {tarefa['descricao']}")
        print(f"  Prioridade:  {tarefa['prioridade']}")
        print(f"  Data Limite: {tarefa['data_limite']}")
        print(f"  Status:      {tarefa['status']}")

def menu():
    while True:
        print("\n=== TaskTracker ===")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Digite 1, 2 ou 3.")

menu()