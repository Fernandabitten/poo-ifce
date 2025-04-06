# 1.Declare uma classe Usuario que contenha os atributos RG (int), CPF (int), nome (string) e dataNascimento (datetime). Deve ser implementado método construtor que possibilita a passagem de parâmetros ou, na sua ausência, valores padrão;

from datetime import datetime as dt

class Usuario:
  def __init__(self, rg=0, cpf=0, nome='Sem nome', data_nascimento=dt(1900, 1, 1)):
    self.rg = rg
    self.cpf = cpf
    self.nome = nome
    self.data_nascimento = data_nascimento

  def get_rg(self):
    return self.rg
  def set_rg(self, rg):
    self.rg = rg    

  def get_cpf(self):
    return self.cpf
  def set_cpf(self, cpf):
    self.cpf = cpf

  def get_nome(self):
    return self.nome
  def set_nome(self, nome):
    self.nome = nome

  def get_data_nascimento(self):
    return self.data_nascimento
  def set_data_nascimento(self, dia, mes, ano):
    self.data_nascimento = dt(ano, mes, dia)

  def __str__(self):
    return (f"RG: {self.rg}\n"
            f"CPF: {self.cpf}\n"
            f"Nome: {self.nome}\n"
            f"Data de Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}")
