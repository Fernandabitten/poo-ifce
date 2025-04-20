from cartao_namorados import DiaDosNamorados
from cartao_natal import Natal
from cartao_aniversario import Aniversario
from cartao_web import CartaoWeb

# Variável de referência do tipo da classe base
cartao: CartaoWeb

cartao = DiaDosNamorados("Fernanda")
cartao.showMessage()

cartao = Natal("Fernanda")
cartao.showMessage()

cartao = Aniversario("Fernanda")
cartao.showMessage()
