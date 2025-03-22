import uteis

def menu():
  print("\nControle de Tarefas")
  print("1: Adicionar uma tarefa")
  print("2: Exibir todas as tarefas")
  print("3: Marcar tarefa como concluida")
  print("4: Voltar para menu principal")

def listar_tarefas_por_status(dicionario):
  # Cria listas para armazenar tarefas concluídas e pendentes
  pendentes = []
  concluídas = []

  for chave, tarefa in dicionario.items():
    if tarefa['status'] == 'Pendente':
       pendentes.append((chave, tarefa))
    elif tarefa['status'] == 'Concluído':
      concluídas.append((chave, tarefa))

  # Exibe as tarefas pendentes
  print('\nTarefas Pendentes:\n'.center(25))
  print(f"{'Nome':<20} {'Descrição':<30} {'Status':<10}")
  print('-' * 60)
  for chave, tarefa in pendentes:
    print(f"{chave:<20} {tarefa['descricao']:<30} {tarefa['status']:<10}")
  print('-' * 60)

  # Exibe as tarefas concluídas
  print('\nTarefas Concluídas:\n'.center(25))
  print(f"{'Nome':<20} {'Descrição':<30} {'Status':<10}")
  print('-' * 60)
  for chave, tarefa in concluídas:
    print(f"{chave:<20} {tarefa['descricao']:<30} {tarefa['status']:<10}")
  print('-' * 60)

def concluir_tarefa(dicionario, chave):
  tarefa = dicionario.get(chave) 

  if tarefa: 
    tarefa["status"] = "Concluído"
    print(f"Tarefa '{chave}' marcada como concluída.")
  else:
    print(f"Tarefa '{chave}' não encontrada.")

def cadastro_de_tarefas():
  tarefas={}
  
  while True:
    menu()
    opcao = None 

    try:
      opcao = int(input("\nEscolha uma opção: ")) 
    except ValueError:
      print("\nOpção inválida. Por favor, insira um número.\n")
      continue

    if opcao == 1:
      print('Adicionar tarefa')
      titulo = input('Nome da tarefa: ').title()
      descricao = input('Descrição da tarefa: ').title()
      dados = {'descricao': descricao, 'status': 'Pendente'}
      uteis.adicionar(tarefas, titulo, dados)

    elif opcao == 2:
      print('\nLista de Tarefas\n'.center(25))
      if not tarefas:
        print('Não existe tarefa cadastrada')
      else:
        listar_tarefas_por_status(tarefas)
    
    elif opcao == 3:
      print('Marcar tarefa como concluída')
      if not tarefas:
        print('Não existe tarefas cadastrados')
      else:
        titulo = input('Nome da tarefa: ').title()
        concluir_tarefa(tarefas, titulo)

    elif opcao == 4:
      print("\nSaindo do programa. Até logo! 👋🏻\n")
      break

    else:
      print("\nOpção inválida. Por favor, tente novamente.\n")
 