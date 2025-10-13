from pagamento import Pagamento

class CartaoCredito(Pagamento):

    def __init__(self, pagante, valor, num_cartao:int, bandeira:str, parcelas:int):
        super().__init__(pagante, valor)
        self.__num_cartao = 0
        self.__bandeira = None
        self.__parcelas = 0

        if isinstance(num_cartao, int):
            self.__num_cartao = num_cartao
        if isinstance(bandeira, str):
            self.__bandeira = bandeira
        if isinstance(parcelas, int):
            self.__parcelas = parcelas

    
    @property
    def num_cartao(self):
        return self.__num_cartao
    @num_cartao.setter
    def n_cartao(self, num_cartao):
        self.__num_cartao = num_cartao
    
    @property
    def bandeira(self):
        return self.__bandeira
    @bandeira.setter
    def bandeira(self, bandeira):
        self.__bandeira = bandeira
    
    @property
    def parcelas(self, parcelas):
        return self.__parcelas
    @parcelas.setter
    def parcelas(self, parcelas):
        self.__parcelas = parcelas

    def conversao_dict(self):
        return {
            'tipo': 'Cartão de Crédito',
            'pagante': self.__pagante.nome,
            'valor': f"R$ {self.__valor:.2f}",
            'parcelas': f"{self.__parcelas}x",
            'bandeira': {self.__bandeira}
        }
