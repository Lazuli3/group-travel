from entidades.empresa import Empresa

class Transporte:
    def __init__(self, tipo:str, empresa:Empresa):

        self.__tipo = None
        self.__empresa = None

        if isinstance(tipo, str):
            self.__tipo = tipo
        if isinstance(empresa, Empresa):
            self.__empresa = empresa
        
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def empresa(self):
        return self.__empresa
    @empresa.setter
    def empresa(self, empresa):
        self.__empresa = empresa
        