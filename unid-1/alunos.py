import uteis

def cadastro_de_alunos():
  alunos={}
  
  while True:
    uteis.menu('Controle de Alunos', 'aluno')
    opcao = None 

    try:
      opcao = int(input("\nEscolha uma opção: ")) 
    except ValueError:
      print("\nOpção inválida. Por favor, insira um número.\n")
      continue

    if opcao == 1:
      print('Adicionar aluno')
      nome = input('Nome do aluno: ').title()
      nota_1 = round(float(input('Nota 1: ')), 3)
      nota_2 = round(float(input('Nota 2: ')), 3)
      nota_3 = round(float(input('Nota 3: ')), 2)
      nota_4 = round(float(input('Nota 4: ')), 2)
      notas = [nota_1, nota_2, nota_3, nota_4]
      uteis.adicionar(alunos, nome, notas)

    elif opcao == 2:
      print('\nLista de alunos\n'.center(25))
      print(f"{'Nome':<20} {'Nota1':<6} {'Nota2':<6} {'Nota3':<6} {'Nota4':<6} {'Media':<12}")
      print('-'*55)
      uteis.listar(alunos, exibir_media=True)
      print('-'*55)
    
    elif opcao == 3:
      print('Editar aluno')
      if not alunos:
        print('Não existe aluno cadastrado')
      else:
        nome = input('Nome do aluno: ').title()
        nota_1 = float(input('Nota 1: '))
        nota_2 = float(input('Nota 2: '))
        nota_3 = float(input('Nota 3: '))
        nota_4 = float(input('Nota 4: '))
        notas = [nota_1, nota_2, nota_3, nota_4]
        uteis.editar(alunos, nome, notas)

    elif opcao == 4:
      print('Remover aluno')
      if not alunos:
        print('Não existe alunos cadastrados')
      else:
        nome = input('Digite o nome do aluno que você quer excluir: ').title()
        uteis.remover(alunos, nome)  

    elif opcao == 5:
      print("\nSaindo do programa. Até logo! 👋🏻\n")
      break

    else:
      print("\nOpção inválida. Por favor, tente novamente.\n")

 