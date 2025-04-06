# 3.	Implemente um programa que deve:
# a.	Instanciar um objeto do tipo Usuario apenas com os valores padrão)
# b.	Solicitar a digitação dos dados do usuário (rg, cpf, nome e data de nascimento),
# c.	Atribuir os valores dos atributos através dos métodos modificadores.
# d.	Em seguida, o programa deve instanciar um objeto do tipo Conta. Porém, para isso, deve passar valores para todos os atributos (leitura prévia) no momento da instanciação.
#   i.	Observação: o código da agência deve ser um valor gerado aleatoriamente entre 0 e 999.
# e. Exibir dados da conta e do usuário

from usuario import Usuario
from conta import Conta
from datetime import datetime as dt
import random

usuario1 = Usuario()
print("Usuário criado com valores padrão:")
print(usuario1)

rg = int(input("Digite o RG do usuário: "))
cpf = int(input("Informe o CPF do usuário: "))
nome = input("Informe o Nome do usuário: ").title()
dia = int(input("Informe o dia de nascimento do usuário: "))
mes = int(input("Informe o mês de nascimento do usuário: "))
ano = int(input("Informe o ano de nascimento do usuário: "))    

usuario1.set_rg(rg)
usuario1.set_cpf(cpf) 
usuario1.set_nome(nome)
usuario1.set_data_nascimento(dia,mes,ano)

saldo = float(input("Digite o saldo inicial da conta: "))
data_abertura = dt.today()
agencia = random.randint(0, 999)

conta1 = Conta(agencia, usuario1, data_abertura, saldo)
print("Conta criada com valores padrão:")
print(conta1)

print("\n--- Dados da Conta ---")
print(f"Agência: {conta1.get_agencia()}")
print(f"Saldo: R${conta1.get_saldo():.2f}")
print(f"Data de Abertura: {conta1.get_data_abertura().strftime('%d/%m/%Y')}")

print("\n--- Dados do Usuário ---")
print(f"Nome: {conta1.get_usuario().get_nome()}")
print(f"RG: {conta1.get_usuario().get_rg()}")
print(f"CPF: {conta1.get_usuario().get_cpf()}")
print(f"Data de Nascimento: {conta1.get_usuario().get_data_nascimento().strftime('%d/%m/%Y')}")



