# Unidade 6 – Encapsulamento

Este projeto faz parte da Unidade 6 do curso, na qual são discutidos os conceitos de encapsulamento, atributos de classe, métodos de classe e métodos estáticos em Python. Como exercício prático, foi implementada a classe Veiculo, que representa veículos em um sistema de locadora.

---

## Conteúdo Abordado

- **Encapsulamento:**.
  Utilização de atributos privados e propriedades para proteger e controlar o acesso aos dados dos objetos.
- **Atributos de Classe:**
  Uso de um atributo compartilhado entre todas as instâncias para contar o total de veículos cadastrados.
- **Métodos de Classe e Estáticos:**
  - Método de classe para exibir o total de veículos.
  - Método estático para calcular o valor do aluguel.

---

## Funcionalidades

- Cadastro de veículos com placa, modelo e valor da diária.
- Controle de status do veículo (alugado/disponível).
- Encapsulamento da placa, permitindo apenas leitura.
- Contador automático do total de veículos cadastrados.
- Cálculo do valor do aluguel para um número de dias.

### Estrutura da Classe

- **Atributos:**

  - \_\_placa (privado): Placa do veículo (acesso somente leitura).
  - modelo: Modelo do veículo.
  - diaria: Valor da diária de aluguel.
  - \_\_alugado (privado): Status de aluguel do veículo.
  - total_veiculos (classe): Total de veículos cadastrados.

- **Métodos:**
  - alugar(): Aluga o veículo, se disponível.
  - devolver(): Devolve o veículo, se alugado.
  - status(): Exibe o status atual do veículo.
  - placa (propriedade): Permite leitura da placa, mas não alteração.
  - mostrar_total_veiculos() (classe): Exibe o total de veículos cadastrados.
  - calcular_preco_aluguel(dias, diaria) (estático): Calcula o valor do aluguel.

### Como Executar

1. Clone o repositório:

```
  git clone https://github.com/Fernandabitten/poo-ifce/tree/main/unid-6
```

2.Execute o arquivo `main.py`

```
  python main.py
```

### Exemplo de saída esperada:

```
  O veículo Toyota Corolla foi alugado com sucesso!
  O veículo Toyota Corolla está alugado.
  O veículo Toyota Corolla foi devolvido com sucesso!
  O veículo Toyota Corolla está disponível para aluguel.
  Placa do veículo: ABC-1234
  A placa não pode ser modificada.
  Total de veículos cadastrados: 2
  Valor total do aluguel por 5 dias do Toyota Corolla: R$ 750.00
```
