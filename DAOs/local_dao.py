from DAOs.dao import DAO
from entidades.local_viagem import LocalViagem

class LocalViagemDAO(DAO):
    def __init__(self):
        super().__init__('locais.pkl')

    def add (self, local: LocalViagem):
        if ((local is not None) and isinstance(local, LocalViagem) and isinstance(local.id, int)):
            super().add(local.id, local)

    def update(self, local: LocalViagem):
        if((local is not None) and isinstance(local, LocalViagem) and isinstance(local.id, int)):
            super().update(local.id, local)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if isinstance(key, int):
            return super().remove(key)
