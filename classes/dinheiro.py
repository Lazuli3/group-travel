from pagamento import Pagamento

class Dinheiro(Pagamento):

    def __init__(self, pagante, valor, valor_entregue: float):
        super().__init__(pagante, valor)
        self.__valor_entregue = 0.0
        self.__troco = 0.0

        if isinstance(valor_entregue, float):
            self.__valor_entregue = valor_entregue

    @property
    def valor_entregue(self):
        return self.__valor_entregue
    @valor_entregue.setter
    def valor_entregue(self, valor_entregue):
        self.__valor_entregue = valor_entregue


    def calc_troco(self):
        if self.__valor_entregue > self.__valor:
            self.__troco = self.__valor_entregue - self.__valor
        return self.__troco


        