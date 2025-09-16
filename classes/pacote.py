from passeioTuristico import PasseioTuristico
from passagem import Passagem
from pagamento import Pagamento
from grupo import Grupo

class Pacote:

    def __init__(self, passeio: PasseioTuristico, passagem: Passagem, pagamento: Pagamento, grupo: Grupo):

        if not isinstance(passeio, PasseioTuristico):
            raise TypeError ("passeio deve ser uma instância da classe PasseioTuristico.")
        if not isinstance(passagem, Passagem):
            raise TypeError ("passagem deve ser uma instância da classe Passagem.")
        if not isinstance(pagamento, Pagamento):
            raise TypeError ("pagamento deve ser uma instância da classe Pagamento.")
        if not isinstance(grupo, Grupo):
            raise TypeError ("grupo deve ser uma instância da classe Grupo.")
        
        self.__passeios = []
        self.__passagens = []
        self.__pagamentos = []
        self.__grupo = Grupo

        
    @property
    def passeios(self):
        return self.__passeios

    def adicionar_passeio(self, passeio):
        if passeio not in self.__passeios:
            self.__passeios.append(passeio)

    def excluir_passeio(self, passeio):
        if passeio in self.__passeios:
            self.__passeios.remove(passeio)

    @property
    def passagens(self):
        return self.__passagens
    
    def adicionar_passagem(self, passagem):
        if passagem not in self.__passagens:
            self.__passagens.append(passagem)

    def excluir_passagem(self, passagem):
        if passagem in self.__passagens:
            self.__passagens.remove(passagem)
    
    @property
    def pagamentos(self):
        return self.__pagamentos
    
    def adicionar_pagamento(self, pagamento):
        if pagamento not in self.__pagamentos:
            self.__pagamentos.append(pagamento)

    def valor_total(self):
        valor_passagens = 0.0
        valor_passeios = 0.0
        
        for passagem in self.__passagens:
            valor_passagens += passagem.valor

        for passeio in self.__passeios:
            valor_passeios += passeio.valor
        
        return valor_passagens + valor_passeios
    
    def calcular_valor_pago(self):
        total_pago = 0.0

        for pagamento in self.__pagamentos:
            total_pago += pagamento.valor()

        return total_pago
    
    def calcular_valor_restante(self):
        return self.valor_total - self.calcular_valor_pago()
    
    @property
    def grupo(self):
        return self.__grupo
