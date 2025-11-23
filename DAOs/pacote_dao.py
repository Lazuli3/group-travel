from DAOs.dao import DAO
from entidades.pacote import Pacote

class PacoteDAO(DAO):
    def __init__(self):
        super().__init__('pacotes.pkl')

    def add (self, pacote: Pacote):
        print(f"Adicionando pacote com ID: {pacote.id}, tipo: {type(pacote.id)}")
        super().add(pacote.id, pacote)

    def update(self, pacote: Pacote):
        if ((pacote is not None) and isinstance(pacote, Pacote) and isinstance(pacote.id, int)):
            super().update(pacote.id, pacote)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if isinstance(key, int):
            return super().remove(key)
