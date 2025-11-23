# ====== entidades/pacote.py ======

class Pacote:
    """Classe que representa um pacote de viagem"""
    
    def __init__(self, id_pacote, passeio, passagem, grupo):
        """
        Construtor do Pacote
        
        Args:
            passeio: Lista de objetos PasseioTuristico
            passagem: Lista de objetos Passagem
            grupo: Objeto Grupo
        """
        self.__passeios = passeio if isinstance(passeio, list) else []
        self.__passagens = passagem if isinstance(passagem, list) else []
        self.__grupo = grupo
        self.__pagamentos = []
        self.__id = id_pacote
    
    # ====== GETTERS (conforme UML) ======

    @property
    def id(self):
        return self.__id

    @property
    def passeios(self):
        """Retorna a lista de passeios turísticos"""
        return self.__passeios

    @property
    def passagens(self):
        """Retorna a lista de passagens"""
        return self.__passagens

    @property
    def pagamentos(self):
        """Retorna a lista de pagamentos"""
        return self.__pagamentos
    
    @property
    def grupo(self):
        """Retorna o grupo associado ao pacote"""
        return self.__grupo
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id (self, id):
        self.__id = id
    
    # ====== MÉTODOS DE GERENCIAMENTO (conforme UML) ======
    
    def adicionar_passeio(self, passeio_turistico):
        """Adiciona um passeio turístico ao pacote"""
        self.__passeios.append(passeio_turistico)
    
    def excluir_passeio(self, passeio_turistico):
        """Remove um passeio turístico do pacote"""
        if passeio_turistico in self.__passeios:
            self.__passeios.remove(passeio_turistico)
    
    def adicionar_passagem(self, passagem):
        """Adiciona uma passagem ao pacote"""
        self.__passagens.append(passagem)
    
    def excluir_passagem(self, passagem):
        """Remove uma passagem do pacote"""
        if passagem in self.__passagens:
            self.__passagens.remove(passagem)
    
    def adicionar_pagamento(self, pagamento):
        """Adiciona um pagamento ao pacote"""
        self.__pagamentos.append(pagamento)
    
    # ====== MÉTODOS DE CÁLCULO (conforme UML) ======
    
    def valor_total(self):
        """
        Calcula o valor total do pacote
        Soma: passagens + passeios
        """
        total = 0.0
        
        # Soma valor das passagens
        for passagem in self.__passagens:
            total += passagem.valor
        
        # Soma valor dos passeios
        for passeio in self.__passeios:
            if hasattr(passeio, 'valor'):
                total += passeio.valor
        
        return total
    
    def calcular_valor_pago(self):
        """Calcula o total já pago (soma dos pagamentos)"""
        total_pago = 0.0
        
        for pagamento in self.__pagamentos:
            if hasattr(pagamento, 'valor'):
                total_pago += pagamento.valor
        
        return total_pago
    
    def calcular_valor_restante(self):
        """Calcula o valor restante a pagar"""
        return self.valor_total() - self.calcular_valor_pago()