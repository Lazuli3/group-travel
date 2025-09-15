from pessoa import Pessoa

class Grupo:

    def __init__(self, pessoa: Pessoa):

        if not isinstance(pessoa, Pessoa):
            raise TypeError ("pessoa deve ser uma instância da classe Pessoa.")

        self.__pessoas = [] 

    @property
    def pessoas(self):
        return self.__pessoas

    def incluir_pessoa(self, pessoa: Pessoa):
        if pessoa not in self.__pessoas:
            self.__pessoas.append(pessoa)

    def excluir_pessoa(self, pessoa: Pessoa):
        if pessoa in self.__pessoas:
            self.__pessoas.remove(pessoa)
                


        