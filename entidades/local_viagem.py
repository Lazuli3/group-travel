
class LocalViagem:

    def __init__(self, cidade: str, pais: str):
        if not isinstance(cidade, str):
            raise TypeError ("Cidade deve ser uma instância da classe str.")
        if not isinstance(pais, str):
            raise TypeError ("País deve ser uma instância da classe str.")

        if not cidade.strip():
            raise ValueError("Cidade não pode ser vazia.")
        if any(c.isdigit() for c in cidade):
            raise ValueError("Cidade não pode conter números.")

        if not pais.strip():
            raise ValueError("País não pode ser vazio.")
        if any(c.isdigit() for c in pais):
            raise ValueError("País não pode conter números.")

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
