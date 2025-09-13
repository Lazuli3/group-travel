
class Pessoa:
    def __init__(self, nome:str, idade: int, celular: int, cpf: int):
        self.__nome = None
        self.__idade = 0
        self.__celular = 0
        self.__cpf = 0

        if isinstance(nome, str):
            self.__nome = nome 
        if isinstance(idade, int):
            self.__idade = idade
        if isinstance(celular, int):
            self.__celular = int
        if isinstance(cpf, int):
            self.__cpf = cpf
    
    