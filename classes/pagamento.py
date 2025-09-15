from pessoa import Pessoa

class Pagamento:

    def __init__(self, pagante:Pessoa, valor:float, data:str):

        self.__pagante = None
        self.__valor = 0

        if isinstance(pagante, Pessoa):
            self.__pagante = pagante
        if isinstance(valor, float):
            self.__valor = valor

    @property
    def pagante(self):
        return self.__pagante
    @pagante.setter
    def pagante(self, pagante):
        self.__pagante = pagante

    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
        

