from cartao_credito import CartaoCredito
from boleto_bancario import BoletoBancario
from pix import Pix
from metodo_pagamento import MetodoPagamento

def main():
    try:
        valor = float(input("Digite o valor da compra: R$"))
        print("\nEscolha o método de pagamento:")
        print("1 - Cartão de Crédito")
        print("2 - Boleto Bancário")
        print("3 - Pix")
        escolha = input("Opção: ")

        pagamento: MetodoPagamento

        if escolha == "1":
            pagamento = CartaoCredito(valor)
        elif escolha == "2":
            pagamento = BoletoBancario(valor)
        elif escolha == "3":
            pagamento = Pix(valor)
        else:
            print("Opção inválida!")
            return

        print("\n--- Comprovante de pagamento ---")
        pagamento.pagar()

    except ValueError:
        print("Valor inválido.")

main()

# Questão:
# O uso de polimorfismo facilitou a implementação porque permitiu usar uma única referência
# (do tipo MetodoPagamento) para lidar com diferentes formas de pagamento (CartaoCredito, BoletoBancario, Pix),
# cada uma com seu próprio comportamento no método pagar(). Isso deixou o código mais simples e flexível,
# sem a necessidade de escrever várias estruturas condicionais para tratar cada tipo de pagamento.

# A vantagem de usar uma interface abstrata (classe abstrata MetodoPagamento) é garantir que todas as formas
# de pagamento implementem o método pagar(), ou seja, seguimos um padrão comum entre classes diferentes.
# Isso melhora a organização do código, facilita a manutenção e permite que novas formas de pagamento sejam
# adicionadas facilmente no futuro, sem precisar mudar o funcionamento do restante do sistema.
