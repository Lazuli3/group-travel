from empresa import Empresa

class Transporte:
    def __init__(self, tipo:str, empresa:Empresa):

        self.__tipo = None
        self.__empresa = None

        if isinstance(tipo, str):
            self.__tipo = tipo
        if isinstance(empresa, Empresa):
            self.__empresa = empresa
        