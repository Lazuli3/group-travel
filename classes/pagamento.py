from datetime import datetime
from pessoa import Pessoa
from abc import ABC, abstractmethod

class Pagamento(ABC):
# Representa um registro de pagamento
    def __init__(self, pagante:Pessoa, valor:float):

        if not isinstance(pagante, Pessoa):
            raise TypeError("pagante deve ser uma instância da classe Pessoa.")
        if not isinstance(valor, float):
            raise TypeError("valor deve ser um número (float ou int).")
        
        self.__pagante = pagante
        self.__valor = valor
        self.__data = datetime.now()
        self.__pagamento_efetuado = False

    @property
    def pagante(self):
        return self.__pagante
    @pagante.setter
    def pagante(self, pagante):
        self.__pagante = pagante

    @property
    def valor(self):
        return self.__valor

    @property
    def data(self):
        return self.__data

    def marcar_como_efetuado(self):
        # alterar o status do pagamento para 'efetuado' (True)
        self.__pagamento_efetuado = True
        

