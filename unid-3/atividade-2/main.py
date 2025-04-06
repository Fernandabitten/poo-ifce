from restaurante import Restaurante

restaurante1 = Restaurante("Pizzaria do João", "Italiana")
restaurante2 = Restaurante("Sushi do Carlos", "Japonesa")
restaurante3 = Restaurante("Churrascaria do Pedro", "Brasileira")

# Chamando descrever_restaurante para cada objeto
print("\n--- Informações dos Restaurantes com descrever_restaurante ---")
print("Restaurante 1:")
restaurante1.descrever_restaurante()

print("Restaurante 2:")
restaurante2.descrever_restaurante()

print("Restaurante 3:")
restaurante3.descrever_restaurante()


# Exibindo informações usando __str__
print("\n--- Informações dos Restaurantes com __str__---")
print("Restaurante 1:")
print(restaurante1) 

print("Restaurante 2:")
print(restaurante2)

print("Restaurante 3:")
print(restaurante3)

