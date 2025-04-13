
# ATIVIDADE 1:
# 1.	Com base na atividade 1 da unidade 3, adicione os métodos consultarSaldo, depositar, sacar e transferir na classe Conta;
# 2.	Adicione as classes ContaPoupanca (filha de Conta), ContaCorrente (filha de Conta) e ContaEspecial (filha de ContaCorrente). Você deve identificar e adicionar demais atributos e métodos relevantes ao problema. Exemplo: saldo;
# 3.	Sobrescreva os métodos consultarSaldo, sacar e transferir na classe ContaEspecial, para refletir a condição de que este tipo de classe possui um limite (cheque especial);
# 4.	Identifique outros métodos necessários (específicos) ao perfil de cada classe. Instancie objetos e execute os novos métodos adicionados às novas classes. Exiba suas informações atualizadas.


import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'unid-3', 'atividade-1')))
from usuario import Usuario
from corrente import ContaCorrente
from poupanca import ContaPoupanca
from especial import ContaEspecial
from datetime import datetime as dt

usuario1 = Usuario()
data_abertura = dt.today()

cc = ContaCorrente(1234, usuario1, data_abertura, 1000.0, 10.0)
cp = ContaPoupanca(5678, usuario1, data_abertura, 2000.0, 0.05)
ces = ContaEspecial(9101, usuario1, data_abertura, 1500.0, 15.0, 500.0)





print("\n--- Dados da Conta Corrente---")
print(cc)
print(cc.depositar(500))
print(f"Saldo após deposito: {cc.consultar_saldo()}")
print(cc.sacar(200))
print(f"Saldo após sacar: {cc.consultar_saldo()}")
print(cc.transferir(100, cp))
print(f"Saldo após transferir: {cc.consultar_saldo()}")
print(cc.get_taxa_manutencao())
cc.set_taxa_manutencao(20)
print(cc.get_taxa_manutencao())
print(cc.cobrar_taxa())


print("\n--- Dados da Conta Poupança---")
print(cp)
print(cp.depositar(650))
print(f"Saldo após deposito: {cp.consultar_saldo()}")
print(cp.sacar(150))
print(f"Saldo após sacar: {cp.consultar_saldo()}")
print(cp.transferir(100, cc))
print(f"Saldo após transferir: {cp.consultar_saldo()}")
print(cp.get_rendimento())
cp.set_rendimento(0.08)
print(cp.get_rendimento())
print(f"Rendimento: {cp.aplicar_rendimento()}")
print(f"Saldo após aplicar rendimento: {cp.consultar_saldo()}")

print("\n--- Dados da Conta Especial---")
print(ces)
print(ces.depositar(450))
print(f"Saldo após deposito: {ces.consultar_saldo()}")
print(ces.sacar(50))
print(f"Saldo após sacar: {ces.consultar_saldo()}")
print(ces.transferir(50, cp))
print(f"Saldo após transferir: {ces.consultar_saldo()}")
print(ces.get_taxa_manutencao())
ces.set_taxa_manutencao(50)
print(ces.get_taxa_manutencao())
print(ces.cobrar_taxa())
print(ces.get_limite())

