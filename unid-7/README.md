## Unidade 7 – Persistência em arquivos e Tratamento de Exceções

Este projeto é a atividade final da Unidade 7 do curso de Programação Orientada a Objetos. O objetivo é aplicar os conceitos de **persistência de dados em arquivos de texto** e **tratamento de exceções** em um sistema que simula o gerenciamento de alunos, professores e disciplinas.

---

## Conteúdos Aplicados

- Leitura e escrita de arquivos de texto (`.txt`)
- Tratamento de exceções com `try`, `except`, `FileNotFoundError`, entre outros
- Programação Orientada a Objetos com herança
- Manipulação de listas e objetos

---

## Estrutura do Projeto

O sistema é dividido em módulos:

- `pessoa.py`: Define a classe base `Pessoa`.
- `aluno.py`: Define a classe `Aluno`, filha de `Pessoa`, contendo matrícula, lista de notas e disciplinas.
- `professor.py`: Define a classe `Professor`, também filha de `Pessoa`.
- `disciplina.py`: Define a classe `Disciplina`, com nome e código.
- `persistencia.py`: Responsável por:
  - Ler os arquivos `alunos.txt`, `professores.txt` e `disciplinas.txt`.
  - Tratar erros como arquivos não encontrados.
  - Criar instâncias dos objetos com os dados lidos.
  - Vincular alunos a disciplinas.
  - Exibir os dados com métodos personalizados.
- `main.py`: Executa o programa, carregando os dados e exibindo os resultados.

## Arquivos de Entrada

O programa espera arquivos `.txt` com as informações:

- `alunos.txt`
- `professores.txt`
- `disciplinas.txt`

Cada linha desses arquivos contém os dados separados por `|`, que são lidos e convertidos em objetos.

## Funcionalidades

- Carregar dados de alunos, professores e disciplinas a partir de arquivos `.txt`.
- Tratar exceções como `FileNotFoundError` e outros problemas de leitura.
- Criar e exibir instâncias com as informações dos arquivos.
- Métodos `exibir_dados()` nas classes para mostrar informações completas dos objetos.

## Como Executar

1. Certifique-se de que os arquivos `alunos.txt`, `professores.txt` e `disciplinas.txt` estão na pasta **bd** projeto.
2. Execute o script principal:

```bash
python main.py
```
3. Os dados serão carregados, e os objetos serão exibidos com as informações completas.

##  Tratamento de Erros
- Caso algum dos arquivos não exista, o sistema exibe uma mensagem amigável e continua a execução.
- Possíveis erros de leitura ou dados mal formatados também são tratados com blocos try/except.

## Observação
Este projeto é focado em arquivos de texto. A persistência com arquivos binários e banco de dados será abordada em etapas futuras do curso.

