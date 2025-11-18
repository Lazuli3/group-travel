from DAO.DAO import DAO
from entidades.local_viagem import LocalViagem

class LocalDAO(DAO):
    def __init__(self):
        super().__init__('locais_viagem.pkl')

    def add(self, localviagem: LocalViagem):
        if isinstance(local, LocalViagem):
            super().add(localviagem.cidade, localviagem)

