'''
from controlador_pacote import ControladorPacote
from controlador_pagamento import ControladorPagamento
from controlador_passeio_turistico import ControladorPasseioTuristico
'''
from controladores.controlador_pessoa import ControladorPessoa
from controladores.controlador_grupo import ControladorGrupo
from controladores.controlador_passagem import ControladorPassagem
from controladores.controlador_local_viagem import ControladorLocalViagem

from view.tela_sistema import TelaSistema

class ControladorSistema():
    
    def __init__(self):
        self.__controlador_pessoa = ControladorPessoa()
        self.__controlador_grupo = ControladorGrupo(self.controlador_pessoa)
        self.__controlador_local_viagem = ControladorLocalViagem()
        self.__controlador_passagem = ControladorPassagem(self.controlador_local_viagem)
        self.__tela_sistema = TelaSistema()
    
    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa

    @property
    def controlador_grupo(self):
        return self.__controlador_grupo
    
    @property
    def controlador_local_viagem(self):
        return self.__controlador_local_viagem
    
    @property
    def controlador_passagem(self):
        return self.__controlador_passagem

    def inicializa_sistema(self):
        self.abre_tela()

    def pessoa(self):
        # Chama o controlador de Livros
        self.__controlador_pessoa.inicia()

    def grupo(self):
        self.__controlador_grupo.inicia()

    def local_viagem(self):
        self.__controlador_local_viagem.inicia()

    def passagem(self):
        self.__controlador_passagem.inicia()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.pessoa, 2: self.grupo, 3:self.local_viagem, 4:self.passagem,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()