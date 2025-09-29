
class Pessoa:
    def __init__(self, nome:str, idade: int, telefone: int, cpf: int):
        self.__nome = None
        self.__idade = 0
        self.__telefone = 0
        self.__cpf = 0

        if isinstance(nome, str):
            self.__nome = nome 
        if isinstance(idade, int):
            self.__idade = idade
        if isinstance(telefone, int):
            self.__telefone = telefone
        if isinstance(cpf, int):
            self.__cpf = cpf
    
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    
    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
        
