from metodo_pagamento import MetodoPagamento

class CartaoCredito(MetodoPagamento):
    def pagar(self):
        taxa = self.valor * 0.05
        total = self.valor + taxa
        print(f"Pagamento com Cartão de Crédito")
        print(f"Valor original: R${self.valor:.2f}")
        print(f"Valor com taxa de 5%: R${total:.2f}")
