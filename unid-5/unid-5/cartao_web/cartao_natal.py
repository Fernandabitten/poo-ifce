from cartao_web import CartaoWeb 
class Natal(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)

    def showMessage(self):
        print(f"Feliz Natal, {self.destinatario}! 🎄 Que seu dia seja cheio de alegria e paz!")
