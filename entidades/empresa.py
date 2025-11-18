
class Empresa:
    def __init__(self, nome:str, cnpj:int, telefone: int):

        self.__nome = None
        self.__cnpj = cnpj
        self.__telefone = telefone

        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(cnpj, str):
            self.__cnpj= int
        if isinstance(telefone, int):
            self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cnpj(self):
        return self.__cnpj 
    
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone:str):
        self.__telefone = telefone
        