from pagamento import Pagamento

class CartaoCredito(Pagamento):

    def __init__(self, pagante, valor, n_cartao:int, bandeira:str, n_parcelas:int):
        super().__init__(pagante, valor)
        self.__n_cartao = 0
        self.__bandeira = None
        self.__n_parcelas = 0

        if isinstance(n_cartao, int):
            self.__n_cartao = n_cartao
        if isinstance(bandeira, str):
            self.__bandeira = bandeira
        if isinstance(n_parcelas, int):
            self.__n_parcelas = n_parcelas

    
    @property
    def n_cartao(self):
        return self.__n_cartao
    @n_cartao.setter
    def n_cartao(self, n_cartao):
        self.__n_cartao = n_cartao
    
    @property
    def bandeira(self):
        return self.__bandeira
    @bandeira.setter
    def bandeira(self, bandeira):
        self.__bandeira = bandeira
    
    @property
    def n_parcelas(self, n_parcelas):
        return self.__n_parcelas
    @n_parcelas.setter
    def n_parcelas(self, n_parcelas):
        self.__n_parcelas = n_parcelas
