from pagamento import Pagamento

class CartaoCredito(Pagamento):

    def __init__(self, pagante, valor, n_cartao:int, banco:str, n_parcelas:int):
        super().__init__(pagante, valor)
        self.__n_cartao = 0
        self.__banco = None
        self.__n_parcelas = 0

        if isinstance(n_cartao, int):
            self.__n_cartao = n_cartao
        if isinstance(banco, str):
            self.__banco = banco
        if isinstance(n_parcelas, int):
            self.__n_parcelas = n_parcelas

    
    @property
    def n_cartao(self):
        return self.__n_cartao
    @n_cartao.setter
    def n_cartao(self, n_cartao):
        self.__n_cartao = n_cartao
    
    @property
    def banco(self):
        return self.__banco
    @banco.setter
    def banco(self, banco):
        self.__banco = banco
    
    @property
    def n_parcelas(self, n_parcelas):
        return self.__n_parcelas
    @n_parcelas.setter
    def n_parcelas(self, n_parcelas):
        self.__n_parcelas = n_parcelas