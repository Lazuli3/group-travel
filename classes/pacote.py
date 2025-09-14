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
        
    @property
    def passeio(self):
        return self.__passeio
    @passeio.setter
    def passeio(self, passeio):
        self.__passeio = passeio
    
    @property
    def passagem(self):
        return self.__passagem
    @passagem.setter
    def passagem(self, passagem):
        self.__passagem = passagem
        