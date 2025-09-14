from localViagem import LocalViagem
from empresa import Empresa
from transporte import Transporte


# aqui que eu acho que a gente consegue puxar a empresa diretpo de transporte, trazendo o atributo, não sei o que achas...
class Passagem:

    def __init__(self, local_viagem: LocalViagem, transporte: Transporte):

        self.__local_viagem = None
        self.__transporte = None

        if isinstance(local_viagem, LocalViagem):
            self.__local_viagem = local_viagem
        if isinstance(transporte, Transporte):
            self.__transporte = transporte
        

    @property
    def local_viagem(self):
        return self.__local_viagem
    @local_viagem.setter
    def local_viagem(self, local_viagem):
        self.__local_viagem = local_viagem

    @property
    def transporte(self):
        return self.__transporte
    @transporte.setter
    def transporte(self, transporte):
        self.__transporte = transporte
