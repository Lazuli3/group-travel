from pagamento import Pagamento

class Pix(Pagamento):

    def __init__(self, pagante, valor, banco:str, chave:int):
        super().__init__(pagante, valor)
        self.__banco = None
        self.__chave = 0

        if isinstance(banco, str):
            self.__banco = banco
        if isinstance(chave, int):
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