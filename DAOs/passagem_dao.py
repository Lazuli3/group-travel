from DAOs.dao import DAO
from entidades.passagem import Passagem

#cada entidade terá uma classe dessa, implementação bem simples.
class PassagemDAO(DAO):
    def __init__(self):
        super().__init__('passagem.pkl')

    def add(self, passagem: Passagem):
        if((passagem is not None) and isinstance(passagem, Passagem) and isinstance(passagem.id, int)):
            super().add(passagem.id, passagem)

    def update(self, passagem: Passagem):
        if((passagem is not None) and isinstance(passagem, Passagem) and isinstance(passagem.id, int)):
            super().update(passagem.id, passagem)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)