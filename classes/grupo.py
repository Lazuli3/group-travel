
from pessoa import Pessoa

class Grupo:

    def __init__(self, pessoas:Pessoa):
        self.__pessoas: []

        if isinstance(pessoas, Pessoa):
            self.__pessoas = pessoas

    @property
    def pessoas(self):
        return self.__pessoas

    @pessoas.setter
    def pessoas(self, pessoas):
        self.__pessoas = pessoas
                


        