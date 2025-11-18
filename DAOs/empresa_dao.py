from DAOs.dao import DAO
from entidades.empresa import Empresa

#cada entidade terá uma classe dessa, implementação bem simples.
class EmpresaDAO(DAO):
    def __init__(self):
        super().__init__('grupo.pkl')

    def add(self, empresa: Empresa):
        if((empresa is not None) and isinstance(empresa, Empresa) and isinstance(empresa.cnpj, int)):
            super().add(empresa.cnpj, empresa)

    def update(self, empresa: Empresa):
        if((empresa is not None) and isinstance(empresa, Empresa) and isinstance(empresa.cnpj, str)):
            super().update(empresa.cnpj, empresa)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key:str):
        if(isinstance(key, str)):
            return super().remove(key)