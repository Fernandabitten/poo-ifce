import estoque
import alunos
import tarefas


def menu():
  print("\nMenu principal")
  print("1: Controle de Alunos")
  print("2: Controle de Produtos")
  print("3: Controle de tarefas")
  print("4: Sair")

def menu_principal():
  while True:
    menu()
    opcao = None 

    try:
      opcao = int(input("\nEscolha uma opção: ")) 
    except ValueError:
      print("\nOpção inválida. Por favor, insira um número.\n")
      continue

    if opcao == 1:
      alunos.cadastro_de_alunos()
    elif opcao == 2:
     estoque.estoque_de_produtos()
    elif opcao == 3:
     tarefas.cadastro_de_tarefas()
    elif opcao == 4:
      break
    else:
      print("Opção inválida!")

menu_principal()