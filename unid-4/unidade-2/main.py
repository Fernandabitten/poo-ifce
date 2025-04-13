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