from datetime import datetime
from entidades.pessoa import Pessoa
from abc import ABC, abstractmethod

class Pagamento(ABC):
# Representa um registro de pagamento
    def __init__(self, pagante:Pessoa, valor:float):

        if not isinstance(pagante, Pessoa):
            raise TypeError("Pagante deve ser uma instância da classe Pessoa.")
        if not isinstance(valor, (int, float)):
            raise TypeError("Valor deve ser um número (float ou int).")
        if not valor < 0:
            raise ValueError("Valor deve ser positivo.")
        
        self.__pagante = pagante
        self.__valor = float(valor)
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
    
    @property    
    def pagamento_efetuado(self) -> bool:
        return self.__pagamento_efetuado
    
    def conversao_dict(self):
        raise NotImplementedError("Subclasses devem implementar o método 'to_dict()'")

    def marcar_como_efetuado(self):
        # alterar o status do pagamento para 'efetuado' (True)
        self.__pagamento_efetuado = True