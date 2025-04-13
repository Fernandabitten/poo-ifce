# Unidade 4 – Herança e Polimorfismo

Esta unidade aborda os pilares fundamentais da Programação Orientada a Objetos: **herança** e **polimorfismo**. Através de atividades práticas com contas bancárias e restaurantes, foi possível explorar o reuso de código e a adaptação de comportamentos em subclasses.

---

## Objetivos

- Compreender o conceito de **herança** para reuso de código.
- Criar estruturas **flexíveis** com o uso do **polimorfismo**.
- Implementar métodos específicos e sobrescritos para diferentes perfis de objetos.
- Aplicar boas práticas de modelagem com foco na reutilização e extensão de funcionalidades.

---

## Atividades

### Atividade 1 – Sistema Bancário Orientado a Objetos

1. Adição de métodos `consultar_saldo`, `depositar`, `sacar` e `transferir` à classe base `Conta`.
2. Criação das subclasses:
   - `ContaPoupanca`
   - `ContaCorrente`
   - `ContaEspecial` (com limite de saque)
3. **Polimorfismo** aplicado:
   - Sobrescrita de métodos `consultar_saldo`, `sacar` e `transferir` em `ContaEspecial`.
4. Instanciação de objetos de diferentes tipos e execução de métodos específicos.

Arquivos envolvidos:

- `conta.py`
- `poupanca.py`
- `corrente.py`
- `especial.py`
- `main.py`

---

### Atividade 2 – Restaurante com Contador de Clientes

1. Adição do atributo `numeroServidos` com valor padrão igual a `0`.
2. Métodos:
   - `get_numero_servidos()`
   - `set_numero_servidos(valor)`
   - `incremente_numero_servidos(valor)`
3. Criação de uma instância chamada `restaurante` e execução dos métodos para alterar e apresentar o número de clientes servidos.

---

Arquivos envolvidos:

- `restaurante.py`
- `main.py`

---

#### Conceitos Aplicados

- **Herança**: Classes filhas `ContaPoupanca`, `ContaCorrente` e `ContaEspecial` herdam de `Conta` ou de outras subclasses, aproveitando métodos e atributos existentes.
- **Polimorfismo**: Os métodos `sacar`, `consultar_saldo` e `transferir` são sobrescritos na subclasse, alterando o comportamento conforme o tipo de conta.

---

#### Execução

Para executar os testes, navegue até o diretório da atividade e execute o arquivo `main.py` correspondente:

```bash
python main.py
```

---

#### Resultado Esperado

- Impressão dos saldos após depósitos, saques e transferências.
- Uso correto do limite em contas especiais.
- Exibição dos clientes servidos no restaurante.
