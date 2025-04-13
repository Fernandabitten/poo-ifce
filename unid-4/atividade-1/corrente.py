# Adiciona uma taxa de manutenção e um método para cobrá-la.

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'unid-3', 'atividade-1')))
from conta import Conta
from datetime import datetime as dt

class ContaCorrente(Conta):
  def __init__(self, agencia=0, usuario=None, data_abertura=dt(1900, 1, 1), saldo=0.0, taxa_manutencao=0.0):
        super().__init__(agencia, usuario, data_abertura, saldo)
        self.taxa_manutencao = taxa_manutencao

  def get_taxa_manutencao(self):
    return f"Taxa de manutenção: R$ {self.taxa_manutencao:.2f}"

  def set_taxa_manutencao(self, taxa):
    if taxa >= 0:
        self.taxa_manutencao = taxa
    else:
        print("Taxa de manutenção não pode ser negativa.")

  def cobrar_taxa(self):
    if self.saldo >= self.taxa_manutencao:
      self.saldo -= self.taxa_manutencao
      return f"Taxa de R$ {self.taxa_manutencao:.2f} cobrada. Saldo atual: R$ {self.saldo:.2f}"
    else:
      return "Saldo insuficiente para cobrar a taxa de manutenção."