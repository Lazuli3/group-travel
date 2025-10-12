from datetime import datetime

class Passagem:
    """Classe que representa uma passagem de viagem"""
    
    def __init__(self, data, valor, local_origem, local_destino, transporte):
        self.__data = data  # datetime
        self.__valor = valor  # float
        self.__local_origem = local_origem  # LocalViagem
        self.__local_destino = local_destino  # LocalViagem
        self.__transporte = transporte  # Transporte
    
    @property
    def data(self):
        return self.__data
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def local_origem(self):
        return self.__local_origem
    
    @property
    def local_destino(self):
        return self.__local_destino
    
    @property
    def transporte(self):
        return self.__transporte
    
    @data.setter
    def data(self, data):
        self.__data = data
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
    @local_origem.setter
    def local_origem(self, local_origem):
        self.__local_origem = local_origem
    
    @local_destino.setter
    def local_destino(self, local_destino):
        self.__local_destino = local_destino
    
    @transporte.setter
    def transporte(self, transporte):
        self.__transporte = transporte
    
    def __str__(self):
        data_formatada = self.__data.strftime("%d/%m/%Y")
        return f"Passagem: {self.__local_origem.cidade} → {self.__local_destino.cidade} | {data_formatada} | R$ {self.__valor:.2f}"
    
    def __repr__(self):
        return f"Passagem(origem='{self.__local_origem.cidade}', destino='{self.__local_destino.cidade}', valor={self.__valor})"