from metodo_pagamento import MetodoPagamento

class BoletoBancario(MetodoPagamento):
    def pagar(self):
        desconto = self.valor * 0.02
        total = self.valor - desconto
        print(f"Pagamento com Boleto Bancário")
        print(f"Valor original: R${self.valor:.2f}")
        print(f"Valor com desconto de 2%: R${total:.2f}")

