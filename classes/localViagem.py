
class LocalViagem():
    
    def __init__(self,cidade:str, pais:str):
        self.__cidade = None
        self.__pais = None

        if isinstance(cidade, str):
            self.__cidade = None
        if isinstance(pais, str):
            self.__pais = None

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
        

        