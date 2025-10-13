from datetime import datetime
from local_viagem import LocalViagem
from grupo import Grupo

class PasseioTuristico:

    def __init__(self, localizacao: LocalViagem, atracao_turistica: str, horario_inicio: datetime, horario_fim: datetime, valor: float, grupo_passeio: Grupo):

        if not isinstance(localizacao, LocalViagem):
            raise TypeError ("Localizacão deve ser uma instância da classe LocalViagem.")

        if not isinstance(atracao_turistica, str):
            raise TypeError ("Atração turística deve ser uma instância da classe str.")
        if not atracao_turistica.strip():
            raise ValueError("Atração turística não pode ser vazia.")
        
        if horario_fim <= horario_inicio:
            raise ValueError("Horário de fim deve ser após o início.")

        if not isinstance(valor, (int, float)):
            raise TypeError ("Valor deve ser uma instância da classe float.")
        if valor < 0:
            raise ValueError("Valor deve ser um número positivo.")

        if not isinstance(grupo_passeio, Grupo):
            raise TypeError ("Grupo do passeio deve ser uma instância da classe Grupo.")

        self.__localizacao = LocalViagem
        self.__atracao_turistica = atracao_turistica
        self.__horario_inicio = datetime
        self.__horario_fim = datetime
        self.__valor = valor
        self.__grupo_passeio = Grupo

    @property
    def localizacao(self):
        return self.__localizacao
    @localizacao.setter
    def localizacao(self, localizacao):
        self.__localizacao = localizacao

    @property
    def atracao_turistica(self):
        return self.__atracao_turistica
    @atracao_turistica.setter
    def atracao_turistica(self, atracao_turistica):
        self.__atracao_turistica = atracao_turistica

    @property
    def horario_inicio(self):
        return self.__horario_inicio
    @horario_inicio.setter
    def horario_inicio(self, horario_inicio):
        self.__horario_inicio = horario_inicio

    @property
    def horario_fim(self):
        return self.__horario_fim
    @horario_fim.setter
    def horario_fim(self, horario_fim):
        self.__horario_fim = horario_fim

    @property 
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def grupo_passeio(self):
        return self.__grupo_passeio
    @grupo_passeio.setter
    def grupo_passeio(self, grupo_passeio):
        self.__grupo_passeio = grupo_passeio
