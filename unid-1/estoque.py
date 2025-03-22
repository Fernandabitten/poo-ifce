import uteis

def estoque_de_produtos():
  produtos={}
  while True:
    uteis.menu('Controle de Produtos', 'produto')
    opcao = None 

    try:
      opcao = int(input("\nEscolha uma opção: ")) 
    except ValueError:
      print("\nOpção inválida. Por favor, insira um número.\n")
      continue     

    if opcao == 1:
      print('Adicionar produto')
      nome = input('Nome do produto: ').title()
      quantidade = int(input('Quantidade do produto: '))
      uteis.adicionar(produtos, nome, quantidade)

    elif opcao == 2:
      print('Lista de produtos')
      print('\nLista de produtos\n'.center(25))
      print(f"{'Nome':<20}{'Quantidade':<6}")
      print('-'*25)
      uteis.listar(produtos)
      print('-'*25)

    elif opcao == 3:
      print('Editar produto')
      if not produtos:
        print('Não existe produto cadastrado')
      else:
        nome = input('Nome do produto: ').title()
        quantidade = int(input('Quantidade do produto: '))
        uteis.editar(produtos, nome, quantidade)

    elif opcao == 4:
      print('Remover produto')
      if not produtos:
        print('Não existe produtos cadastrados')
      else:
        nome = input('Digite o nome do produto que você quer excluir: ').title()
        uteis.remover(produtos, nome)  

    elif opcao == 5:
      print("\nSaindo do programa. Até logo! 👋🏻\n")
      break

    else:
      print("\nOpção inválida. Por favor, insira um número válido5.\n")


