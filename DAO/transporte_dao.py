from DAO.DAO import DAO
from entidades.transporte import Transporte

#cada entidade terá uma classe dessa, implementação bem simples.
class TransporteDAO(DAO):
    def __init__(self):
        super().__init__('grupo.pkl')

    def add(self, transporte: Transporte):
        if((transporte is not None) and isinstance(transporte, Transporte) and isinstance(transporte.id, int)):
            super().add(transporte.id, transporte)

    def update(self, transporte: Transporte):
        if((transporte is not None) and isinstance(transporte, Transporte) and isinstance(transporte.id, int)):
            super().update(transporte.id, transporte)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)