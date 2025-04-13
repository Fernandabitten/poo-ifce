# Permite um limite adicional (cheque especial) e sobrescreve os métodos de consulta de saldo, saque e transferência.
from corrente import ContaCorrente
from datetime import datetime as dt

class ContaEspecial(ContaCorrente):
    def __init__(self, agencia=0, usuario=None, data_abertura=dt(1900, 1, 1), saldo=0.0, taxa_manutencao=0.0, limite=0.0):
        super().__init__(agencia, usuario, data_abertura, saldo, taxa_manutencao)
        self.limite = limite
    
    def get_limite(self):
      return f"Limite de R$ {self.limite:.2f}"

    def set_limite(self, novo_limite):
      if novo_limite >= 0:
          self.limite = novo_limite
      else:
          print("Limite não pode ser negativo.")

    def consultar_saldo(self):
        return f"Saldo atual: R$ {self.saldo:.2f}, Limite: R$ {self.limite:.2f}"

    def sacar(self, valor):
        if 0 < valor <= self.saldo + self.limite:
            self.saldo -= valor
            return f"Saque de R$ {valor:.2f} realizado com sucesso."
        return "Saldo insuficiente ou valor inválido."

    def transferir(self, valor, conta_destino):
        if 0 < valor <= self.saldo + self.limite:
            self.saldo -= valor
            conta_destino.depositar(valor)
            return f"Transferência de R$ {valor:.2f} realizada com sucesso para a conta de {conta_destino.usuario.nome}."
        return "Saldo insuficiente ou valor inválido."
