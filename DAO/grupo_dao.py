from DAO.DAO import DAO
from entidades.grupo import Grupo

#cada entidade terá uma classe dessa, implementação bem simples.
class GrupoDAO(DAO):
    def __init__(self):
        super().__init__('grupo.pkl')

    def add(self, grupo: Grupo):
        if((grupo is not None) and isinstance(grupo, Grupo) and isinstance(grupo.id, int)):
            super().add(grupo.id, grupo)

    def update(self, grupo: Grupo):
        if((grupo is not None) and isinstance(grupo, Grupo) and isinstance(grupo.id, int)):
            super().update(grupo.id, grupo)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)