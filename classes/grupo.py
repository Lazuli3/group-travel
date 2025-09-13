
from pessoa import Pessoa

class Grupo:

    def __init__(self, pessoas:Pessoa):
        self.__pessoas: []

        if isinstance(pessoas, []):
            self.__pessoas = pessoas
        


        