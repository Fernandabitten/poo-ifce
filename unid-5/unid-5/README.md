# Unidade 5 – Classes Abstratas e Interfaces

Esta unidade explora conceitos fundamentais para o design orientado a objetos: classes abstratas, métodos abstratos e o uso de interfaces em Python. Por meio de atividades práticas com cartões personalizados e sistemas de pagamento, foi possível entender como estruturar e padronizar comportamentos em diferentes classes por meio do polimorfismo.

---

## Objetivos

- Entender o que são **classes e métodos abstratos**.
- Aprender a criar **interfaces** para padronizar comportamentos.
- Usar **polimorfismo** para tratar objetos diferentes de forma igual.

---

## Conceitos-Chave

### 1. **Classe Abstrata**

- É um "molde" que **não pode ser instanciado diretamente**.
- Define **métodos abstratos** (sem implementação) que as classes filhas **devem** implementar.
- Exemplo: `CartaoWeb` e `MetodoPagamento` das atividades.

### 2. **Método Abstrato**

- Um método que só tem a **assinatura** (nome e parâmetros), mas **não tem código**.
- Usamos `@abstractmethod` em Python para marcar esses métodos.
- Exemplo: `showMessage()` e `pagar()`.

### 3. **Interface**

- Um conjunto de regras que diz **"o que"** uma classe deve fazer, mas não **"como"**.
- Em Python, usamos classes abstratas para simular interfaces.
- Exemplo: Todos os cartões (`DiaDosNamorados`, `Natal`, etc.) seguem a interface `CartaoWeb`.

### 4. **Polimorfismo**

- Capacidade de **tratar objetos diferentes como se fossem do mesmo tipo**.
- Exemplo: Chamar `pagar()` em `CartaoCredito`, `BoletoBancario` ou `Pix` sem se preocupar com o tipo real.

---

## Atividades

### 1. **Sistema de Cartões Web**

- **Classe Abstrata**: `CartaoWeb`.
- **Classes Filhas**: `DiaDosNamorados`, `Natal`, `Aniversario`.
- **Funcionalidade**: Cada cartão exibe uma mensagem personalizada usando `showMessage()`.

Arquivos envolvidos:

- cartao_web.py
- dia_dos_namorados.py
- natal.py
- aniversario.py
- main.py

### 2. **Sistema de Pagamento**

- **Classe Abstrata**: `MetodoPagamento`.
- **Classes Filhas**: `CartaoCredito`, `BoletoBancario`, `Pix`.
- **Funcionalidade**: Cada método calcula o valor final (com taxa ou desconto) no `pagar()`.

Arquivos envolvidos:

- metodo_pagamento.py
- cartao_credito.py
- boleto_bancario.py
- pix.py
- main.py

---

#### Conceitos Aplicados

- **Classe Abstrata:** Define um contrato de métodos e atributos obrigatórios.
- **Interface:** Padroniza comportamentos entre múltiplas classes.
- **Polimorfismo:** A chamada do método pagar() ou showMessage() se adapta ao comportamento da subclasse utilizada.

---

#### Execução

Para executar os testes, navegue até o diretório da atividade e execute o arquivo `main.py` correspondente:

```bash
python main.py
```

---

#### Resultado Esperado

- Exibição personalizada de mensagens de cartões conforme a data comemorativa.
- Cálculo e exibição de valores finais com base no método de pagamento escolhido.
