from DAOs.dao import DAO
from entidades.pessoa import Pessoa

#cada entidade terá uma classe dessa, implementação bem simples.
class PessoaDAO(DAO):
    def __init__(self):
        super().__init__('pessoa.pkl')

    def add(self, pessoa: Pessoa):
        if((pessoa is not None) and isinstance(pessoa, Pessoa) and isinstance(pessoa.cpf, str)):
            super().add(pessoa.cpf, pessoa)

    def update(self, pessoa: Pessoa):
        if((pessoa is not None) and isinstance(pessoa, Pessoa) and isinstance(pessoa.cpf, str)):
            super().update(pessoa.cpf, pessoa)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key:str):
        if(isinstance(key, str)):
            return super().remove(key)