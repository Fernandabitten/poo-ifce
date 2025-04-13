# 1.	Crie uma classe chamada Restaurante. O construtor deve prever a passagem de valores para os atributos: nomeRestaurante e tipoCozinha. Crie um método chamado descreverRestaurante, que mostra ambas as informações, e um método abrirRestaurante, que exibe mensagem de restaurante aberto;
# 2.	Crie 3 (três) objetos Restaurante e execute o método descreverRestaurante para cada uma delas;
# 3.	Adicione o método __str__ à classe Restaurante, utilize-o ao invés de descreverRestaurante para exibir as informações da classe.

class Restaurante:
    def __init__(self, nome_restaurante, tipo_cozinha):
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha
        self.numero_servidos = 0 # Atributo adicional para contar o número de pratos servidos

    def descrever_restaurante(self):
        print(f"Nome do Restaurante: {self.nome_restaurante}")
        print(f"Tipo de Cozinha: {self.tipo_cozinha}")

    def abrir_restaurante(self):
        print(f"O restaurante {self.nome_restaurante} está aberto!")
    
    def get_numero_servidos(self):
        return self.numero_servidos

    def set_numero_servidos(self, numero):
        if numero >= 0:
            self.numero_servidos = numero
        else:
            print("O número de clientes servidos não pode ser negativo.")

    def incremente_numero_servidos(self, adicional):
        if adicional > 0:
            novo_total = self.get_numero_servidos() + adicional
            self.set_numero_servidos(novo_total)
        else:
            print("O incremento precisa ser maior que zero.")

    def __str__(self):
        return (f"Nome do Restaurante: {self.nome_restaurante}\n"
                f"Tipo de Cozinha: {self.tipo_cozinha}")