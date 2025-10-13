from entidades.pagamento import Pagamento

class Dinheiro(Pagamento):

    def __init__(self, pagante, valor, pagamento_efetuado, valor_entregue: float):
        super().__init__(pagante, valor, pagamento_efetuado)
        self.__valor_entregue = 0.0
        self.__troco = 0.0

        if isinstance(valor_entregue, (int, float)):
            self.__valor_entregue = float(valor_entregue)

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

    def conversao_dict(self):
        dinheiro_dict = super().conversao_dict()

        dinheiro_dict.update({
            'tipo': 'Dinheiro',
            'troco': f"Troco: R$ {self.__troco:.2f}"
        })
        
        return dinheiro_dict