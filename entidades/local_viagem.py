from datetime import datetime

class LocalViagem:
    
    def __init__(self, cidade: str, pais: str):
        if not isinstance(cidade, str):
            raise TypeError ("cidade deve ser uma instância da classe str.")
        if not isinstance(pais, str):
            raise TypeError ("pais deve ser uma instância da classe str.")

        self.__cidade = cidade
        self.__pais = pais

    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade
    
    @property
    def pais(self):
        return self.__pais
    
    @pais.setter
    def pais(self, pais):
        self.__pais = pais
        

        