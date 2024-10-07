#coding: utf-8

def ComissaoSalario():
    Nome = input("Entre com o nome do Vendedor:")
    SalarioFixo = float(input("Informe o Salário:"))
    Vendas = float(input("Informe o Total de Vendas:"))
    Comissao = 0.15*Vendas
    PagamentoEsperado = SalarioFixo+Comissao
    return Nome, SalarioFixo, Vendas, PagamentoEsperado

if __name__ == "__main__":
   Nome, SalarioFixo, Comissao, PagamentoEsperado =ComissaoSalario()
   strg = "{0} Obteve R$ {1: 2f} de Comissão e vai Receber {2: 2f}".format(Nome, Comissao,PagamentoEsperado)
   print(strg)
