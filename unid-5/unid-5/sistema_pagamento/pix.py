from metodo_pagamento import MetodoPagamento

class Pix(MetodoPagamento):
    def pagar(self):
        print(f"Pagamento com Pix")
        print(f"Valor original: R${self.valor:.2f}")
        print(f"Valor final: R${self.valor:.2f}")
