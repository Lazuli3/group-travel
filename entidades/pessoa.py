
class Pessoa:
    def __init__(self, nome:str, idade: int, telefone: str, cpf: str):
        self.__nome = nome
        self.__idade = idade
        self.__telefone = telefone
        self.__cpf = cpf

        if not isinstance(nome, str):
            raise TypeError("A variavel nome tem que ser do tipo string.") 
        if not isinstance(idade, int):
            raise TypeError("A variável idade tem que ser do tipo inteiro.")
        if not isinstance(telefone, str):
            raise TypeError("A variável telefone tem que ser do tipo string")
        if not isinstance(cpf, str):
            raise TypeError('A variável cpf tem que ser do tipo string.')
    
    
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

    def maior_idade(self):
        return self.__idade >= 18
            
    
        
