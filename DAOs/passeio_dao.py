from DAOs.dao import DAO
from entidades.passeio_turistico import PasseioTuristico

class PasseioTuristicoDAO(DAO):
    def __init__(self):
        super().__init__('passeios.pkl')

    def add (self, passeio: PasseioTuristico):
        if ((passeio is not None) and isinstance(passeio, PasseioTuristico) and isinstance(passeio.id, int)):
            super().add(passeio.id, passeio)

    def update(self, passeio: PasseioTuristico):
        if ((passeio is not None) and isinstance(passeio, PasseioTuristico) and isinstance(passeio.id, int)):
            super().update(passeio.id, passeio)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if isinstance(key, int):
            return super().remove(key)
