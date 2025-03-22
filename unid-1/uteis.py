def adicionar(dicionario, chave, valor):
  if chave in dicionario:
    print (f'\n{chave} já existe no cadastro. Use editar para modificar a quantidade.')
  else:
    dicionario[chave] = valor
    print('-'*30)
    print(f'{chave} adicionado(a) com sucesso.')
    print('-'*30)

def listar(dicionario, exibir_media=False):
  if not dicionario:
    print("Nenhum cadastro encontrado.")
    return
  for chave, valor in dicionario.items():
    # se for um dicionario
    if isinstance(valor, dict):  # Caso seja um dicionário (como as tarefas)
        descricao = valor.get("descricao", "N/A")
        status = valor.get("status", "N/A")
        print(f"{chave:<20} {descricao:<30} {status:<10}")
    # se for uma lista
    elif isinstance(valor, list):
      valor_formatado = "     ".join(map(str, valor))
      if exibir_media:
          media = sum(valor) / len(valor)
          print(f"{chave:<20} {valor_formatado:<30} {media:.2f}")
      else:
          print(f"{chave:<20} {valor_formatado:<30}")
    else:
        # se for valores simples 
        print(f"{chave:<20} {valor:<6}")

def remover(dicionario, nome):
  if nome in dicionario:
    del dicionario[nome]
    print(f"'{nome}' removido com sucesso.")
  else:
    print(f"'{nome}' não foi encontrado.")

def editar(dicionario, chave, valor):
  if not chave in dicionario:
    print(f'{chave} não existe no cadastro')
  else:
    dicionario[chave] = valor
    print('-'*30)
    print(f'{chave} editado(a) com sucesso.')
    print('-'*30)
  

def menu(titulo, texto): 
  print(f"\n{titulo}")
  print(f"1: Adicionar um {texto}")
  print(f"2: Exibir {texto}s")
  print(f"3: Editar {texto}")
  print(f"4: Remover {texto}")
  print("5: Voltar para o menu principal")

      