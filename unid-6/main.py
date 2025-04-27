from veiculo import Veiculo 

# 1. Criar dois veículos
veiculo1 = Veiculo("ABC-1234", "Toyota Corolla", 150.0)
veiculo2 = Veiculo("XYZ-5678", "Honda Civic", 180.0)

# 2. Alugar um veículo e exibir seu status.
veiculo1.alugar()
veiculo1.status()

# 3. Devolver o veículo e exibir novamente o status.
veiculo1.devolver()
veiculo1.status()

# 4. Exibir a placa do veículo e tentar modificá-la para verificar o encapsulamento.
print(f"Placa do veículo: {veiculo1.placa}")
veiculo1.placa = "DEF-5678"  # Tentativa de modificar a placa (não deve funcionar)

# 5. Exibir o total de veículos cadastrados.
Veiculo.mostrar_total_veiculos()

# 6. Calcular e exibir o valor do aluguel de um dos veículos para um número de dias usando o método estático.
valor_total = Veiculo.calcular_preco_aluguel(5, veiculo1.diaria)
print(f"Valor total do aluguel por 5 dias do {veiculo1.modelo}: R$ {valor_total:.2f}")


