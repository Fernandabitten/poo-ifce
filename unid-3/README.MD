# POO unidade 3

Este repositório contém a implementação de duas atividades práticas referentes à Unidade 3 – Atributos e Métodos do curso de Programação Orientada a Objetos. Os objetivos desta unidade incluem o aprofundamento dos conceitos de atributos, métodos, autorreferência, construtores, métodos de acesso e modificadores, além da introdução à proteção de dados (encapsulamento).

### Objetivos da Unidade 3

Nesta unidade, os seguintes conceitos foram abordados e aplicados:

- Autorreferência: Uso do self para atribuição e manipulação dos atributos da classe.
- Assinatura de métodos: Definição clara dos parâmetros e retorno dos métodos.
- Construtores: Implementação de métodos especiais (**init**) para inicialização de objetos.
- Métodos de acesso e modificadores: Criação de getters e setters para controle dos atributos.
- Proteção de dados (encapsulamento): Introdução à necessidade de proteger os dados internos da classe.

### Atividade 1: Sistema de Usuário e Conta Bancária

#### Descrição

Nesta atividade, foi desenvolvido um sistema que simula a criação de usuários e contas bancárias. O programa utiliza conceitos como construtores, autorreferência e encapsulamento para gerenciar os dados.

#### Funcionalidades

1. Classe Usuario:

- Atributos: RG, CPF, nome, dataNascimento.
- Métodos:
  - Construtor com valores padrão ou personalizados.
  - Modificadores (setters) para atribuir valores aos atributos.
  - Acessores (getters) para acessar os valores dos atributos.

2. Classe Conta:

- Atributos: agencia, usuario (objeto do tipo Usuario), dataAbertura, saldo.
- Métodos:
  - Construtor para inicialização com valores fornecidos.
  - Modificadores (setters) e acessores (getters).

3. Programa principal:

- Instancia um objeto Usuario com valores padrão.
- Solicita os dados do usuário via entrada do teclado.
- Cria uma conta bancária associada ao usuário, gerando automaticamente o código da agência (valor aleatório entre 0 e 999).
- Exibe as informações completas da conta e do usuário.

### Atividade 2: Classe Restaurante

#### Descrição

Nesta atividade, foi desenvolvida uma classe que representa um restaurante, utilizando construtores, autorreferência e métodos personalizados para exibição das informações.

#### Funcionalidades

1. Classe Restaurante:

- Atributos: nomeRestaurante, tipoCozinha.
- Métodos:
  - Construtor para inicialização com valores fornecidos.
  - Método descreverRestaurante: Exibe as informações do restaurante.
  - Método abrirRestaurante: Exibe uma mensagem indicando que o restaurante está aberto.
  - Método especial **str**: Substitui o método anterior para exibir as informações do restaurante diretamente.

Programa principal:

Cria três objetos da classe Restaurante.

Exibe as informações dos restaurantes utilizando o método especial **str**.

1. Classe Restaurante:

- Atributos: nomeRestaurante, tipoCozinha.

- Métodos:
  - Construtor para inicialização com valores fornecidos.
  - Método descreverRestaurante: Exibe as informações do restaurante.
  - Método abrirRestaurante: Exibe uma mensagem indicando que o restaurante está aberto.
  - Método especial **str**: Substitui o método anterior para exibir as informações do restaurante diretamente.

Programa principal:

- Cria três objetos da classe Restaurante.
- Exibe as informações dos restaurantes utilizando o método especial **str**.

### Estrutura do Repositório

```
├── atividade1.py  # Código referente à Atividade 1
├── atividade2.py  # Código referente à Atividade 2
└── README.md      # Documentação do projeto
```

### Tecnologias Utilizadas

- Python 3.x
