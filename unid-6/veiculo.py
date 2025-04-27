class Veiculo:
    total_veiculos = 0  # atributo de classe
    def __init__(self,placa, modelo, diaria):
        self.__placa = placa  # atributo privado
        self.modelo = modelo
        self.diaria = diaria
        self.__alugado = False  # atributo privado
        Veiculo.total_veiculos += 1  # incrementa o total de veículo

    def alugar(self):
      if not self.__alugado:
          self.__alugado = True
          print(f"O veículo {self.modelo} foi alugado com sucesso!")
      else:
          print(f"O veículo {self.modelo} já está alugado.")
    
    def devolver(self):
      if self.__alugado:
          self.__alugado = False
          print(f"O veículo {self.modelo} foi devolvido com sucesso!")
      else:
          print(f"O veículo {self.modelo} não está alugado.")
    
    def status(self):
      if self.__alugado:
          print(f"O veículo {self.modelo} está alugado.")
      else:
          print(f"O veículo {self.modelo} está disponível para aluguel.")

    @property
    def placa(self):
        return self.__placa
    
    @placa.setter
    def placa(self, placa):
      print("A placa não pode ser modificada.")
    
    @classmethod
    def mostrar_total_veiculos(cls):
       print(f"Total de veículos cadastrados: {cls.total_veiculos}")

    @staticmethod
    def calcular_preco_aluguel(dias, diaria):
        return dias * diaria
    

    def __str__(self):
        return f"{self.marca} {self.modelo}"