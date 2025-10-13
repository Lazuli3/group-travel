from entidades.pagamento import Pagamento

class CartaoCredito(Pagamento):

    def __init__(self, pagante, valor, pagamento_efetuado, num_cartao:str, bandeira:str, parcelas:int):
        super().__init__(pagante, valor, pagamento_efetuado)
        self.__num_cartao = None
        self.__bandeira = None
        self.__parcelas = 0

        if isinstance(num_cartao, str):
            self.__num_cartao = num_cartao
        if isinstance(bandeira, str):
            self.__bandeira = bandeira
        if isinstance(parcelas, int):
            self.__parcelas = parcelas

    
    @property
    def num_cartao(self):
        return self.__num_cartao
    @num_cartao.setter
    def num_cartao(self, num_cartao):
        self.__num_cartao = num_cartao
    
    @property
    def bandeira(self):
        return self.__bandeira
    @bandeira.setter
    def bandeira(self, bandeira):
        self.__bandeira = bandeira
    
    @property
    def parcelas(self):
        return self.__parcelas
    @parcelas.setter
    def parcelas(self, parcelas):
        self.__parcelas = parcelas

    def conversao_dict(self):
        cartao_dict = super().conversao_dict()
        
        cartao_dict.update({
            'tipo': 'Cartão de Crédito',
            'parcelas': f"{self.__parcelas}x",
            'bandeira': self.__bandeira
        })
        
        return cartao_dict
