
from localViagem import LocalViagem
from grupo import Grupo

class PasseioTuristico:

    def __init__(self, localizacao: LocalViagem, atracao_turistica: str, horario_inicio:int, horario_fim:int, valor:float, grupo_passeio: Grupo):

        self.__localizacao = None
        self.__atracao_turistica = None
        self.__horario_inicio = 0
        self.__horario_fim = 0
        self.__valor = 0
        self.__grupo_passeio: []

        if isinstance(localizacao, LocalViagem):
            self.__localizacao = localizacao
        if isinstance(atracao_turistica, str):
            self.__atracao_turistica = atracao_turistica
        if isinstance(horario_inicio, int):
            self.__horario_inicio = horario_inicio
        if isinstance(horario_fim, int):
            self.__horario_fim = horario_fim
        if isinstance(valor, float):
            self.__valor = valor
        if isinstance(grupo_passeio, []):
            self.__grupo_passeio = grupo_passeio
        