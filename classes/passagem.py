from localViagem import LocalViagem
from empresa import Empresa
from transporte import Transporte

class Passagem:

    def __init__(self, local_viagem: LocalViagem, transporte: Transporte):

        self.__local_viagem = None
        self.__transporte = None

        if isinstance(local_viagem, LocalViagem):
            self.__local_viagem = local_viagem
        if isinstance(transporte, Transporte):
            self.__transporte = transporte
        

        