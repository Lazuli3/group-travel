from entidades.pagamento import Pagamento

class Pix(Pagamento):

    def __init__(self, pagante, valor, pagamento_efetuado, banco:str, chave:str):
        super().__init__(pagante, valor, pagamento_efetuado)
        self.__banco = None
        self.__chave = None

        if isinstance(banco, str):
            self.__banco = banco
        if isinstance(chave, str):
            self.__chave = chave

    @property 
    def banco(self):
        return self.__banco
    @banco.setter
    def banco(self, banco):
        self.__banco = banco
    
    @property
    def chave(self):
        return self.__chave
    @chave.setter
    def chave(self, chave):
        self.__chave = chave
        
    def conversao_dict(self):
        pix_dict = super().conversao_dict() 
        
        pix_dict.update({
            'tipo': 'Pix',
            'banco': self.__banco
        })
        
        return pix_dict
