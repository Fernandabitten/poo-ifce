# 1.	Crie uma classe chamada Restaurante. O construtor deve prever a passagem de valores para os atributos: nomeRestaurante e tipoCozinha. Crie um método chamado descreverRestaurante, que mostra ambas as informações, e um método abrirRestaurante, que exibe mensagem de restaurante aberto;
# 2.	Crie 3 (três) objetos Restaurante e execute o método descreverRestaurante para cada uma delas;
# 3.	Adicione o método __str__ à classe Restaurante, utilize-o ao invés de descreverRestaurante para exibir as informações da classe.

class Restaurante:
    def __init__(self, nome_restaurante, tipo_cozinha):
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha

    def descrever_restaurante(self):
        print(f"Nome do Restaurante: {self.nome_restaurante}")
        print(f"Tipo de Cozinha: {self.tipo_cozinha}")

    def abrir_restaurante(self):
        print(f"O restaurante {self.nome_restaurante} está aberto!")

    def __str__(self):
        return (f"Nome do Restaurante: {self.nome_restaurante}\n"
                f"Tipo de Cozinha: {self.tipo_cozinha}")