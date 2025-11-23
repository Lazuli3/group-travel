from DAOs.dao import DAO
from entidades.pagamento import Pagamento

class PagamentoDAO(DAO):
    def __init__(self):
        super().__init__('pagamentos.pkl')

    def add (self, pagamento: Pagamento):
        if ((pagamento is not None) and isinstance(pagamento, Pagamento) and isinstance(pagamento.id, int)):
            super().add(pagamento.id, pagamento)

    def update(self, pagamento: Pagamento):
        if ((pagamento is not None) and isinstance(pagamento, Pagamento) and isinstance(pagamento.id, int)):
            super().update(pagamento.id, pagamento)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if isinstance(key, int):
            return super().remove(key)
