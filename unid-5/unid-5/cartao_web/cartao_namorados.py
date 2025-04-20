from cartao_web import CartaoWeb 


class DiaDosNamorados(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)

    def showMessage(self):
        print(f"Querido(a) {self.destinatario}, feliz Dia dos Namorados! 💖 Você é muito especial pra mim!")
