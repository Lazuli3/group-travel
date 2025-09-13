from passeioTuristico import PasseioTuristico
from passagem import Passagem

class Pacote:

    def __init__(self, passeio: PasseioTuristico, passagem: Passagem):

        self.__passeio: None
        self.__passagem: None

        if isinstance(passeio, PasseioTuristico):
            self.__passeio = passeio
        if isinstance(passagem, Passagem):
            self.__passagem = passagem
            
        