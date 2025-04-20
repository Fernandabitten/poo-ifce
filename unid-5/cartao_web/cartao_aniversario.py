from cartao_web import CartaoWeb
class Aniversario(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)

    def showMessage(self):
        print(f"Parabéns, {self.destinatario}! 🎉 Que seu aniversário seja incrível e cheio de felicidade!")
