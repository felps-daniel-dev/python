class Caixa: 

    def __init__(self, operador):
        self.__operador = operador

    def processar_pagamento(valor_compra, valor_pago):
        if valor_compra <= valor_pago:
            troco = self.caucula_troco
            print("Pagamento realizado.")
            print("Toco no valor de: ", troco)
        else:
            print("Pagamento invalido")

    def caucula_troco(valor_compra, valor_pago):
        return valor_pago - valor_compra

#▪ Na rotina de troco privada, utiliza divisão inteira (//) e módulo
#(%) para calcular a quantidade exata de cada cédula.

 
