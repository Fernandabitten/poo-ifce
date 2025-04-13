# Inclui um atributo adicional chamado rendimento e um método para calcular o rendimento.

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'unid-3', 'atividade-1')))
from conta import Conta
from datetime import datetime as dt


class ContaPoupanca(Conta):
    def __init__(self, agencia=0, usuario=None, data_abertura=dt(1900, 1, 1), saldo=0.0, rendimento=0.0):
        super().__init__(agencia, usuario, data_abertura, saldo)
        self.rendimento = rendimento
    
    def get_rendimento(self):
        return f"Rendimento: R$ {self.rendimento:.2f}"

    def set_rendimento(self, rendimento):
        if rendimento >= 0:
            self.rendimento = rendimento
        else:
            print("Rendimento não pode ser negativo.")

    def aplicar_rendimento(self):
        rendimento_valor = self.saldo * self.rendimento
        self.saldo += rendimento_valor
        return f"Rendimento de R$ {rendimento_valor:.2f} aplicado. Novo saldo: R$ {self.saldo:.2f}"

    