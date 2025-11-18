from DAOs.dao import DAO
from entidades.local_viagem import LocalViagem

class LocalViagemDAO(DAO):
    def __init__(self):
        super().__init__('locais.pkl')

    def add (self, local: LocalViagem):
        if ((local is not None) and isinstance(local, LocalViagem)):
            novo_id = super().gerar_id()
            local.id = novo_id
            super().add(novo_id, local)