from DAO.DAO import DAO
from entidades.empresa import Empresa

#cada entidade terá uma classe dessa, implementação bem simples.
class EmpresaDAO(DAO):
    def __init__(self):
        super().__init__('grupo.pkl')

    def add(self, empresa: Empresa):
        if((empresa is not None) and isinstance(empresa, Empresa) and isinstance(empresa.cnpj, int)):
            super().add(empresa.cnpj, empresa)

    def update(self, empresa: Empresa):
        if((empresa is not None) and isinstance(empresa, Empresa) and isinstance(empresa.cnpj, int)):
            super().update(empresa.cnpj, empresa)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)