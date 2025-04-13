# ATIVIDADE 2:
# 1.	A partir da atividade 2 da unidade 3, acrescente o atributo numeroServidos, cujo valor padrão é 0 (zero). Crie uma instância chamada restaurante, apresente o número de clientes atendidos e, em seguida, mude o valor e exiba-o novamente;
# 2.	Adicione os métodos getNumeroServidos e setNumeroServidos, para alterar o valor de clientes atendidos. Execute-o com um novo valor de clientes atendidos e, em seguida, apresente o valor novamente;
# 3.	Acrescente o método incrementeNumeroServidos que permita incrementar o número de clientes servidos, através de um parâmetro passado. Em sua implementação, invoque os métodos getNumeroServidos e setNumeroServidos para incrementar o número de clientes atendidos.

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'unid-3', 'atividade-2')))
from restaurante import Restaurante

restaurante = Restaurante("Pizzaria do João", "Italiana")
print("Número de clientes atendidos:", restaurante.get_numero_servidos())
restaurante.set_numero_servidos(50)
print("Número de clientes atendidos:", restaurante.get_numero_servidos())
restaurante.incremente_numero_servidos(10)
print("Número de clientes atendidos:", restaurante.get_numero_servidos())