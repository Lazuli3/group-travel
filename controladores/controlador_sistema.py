from controladores.controlador_pacote import ControladorPacote
from controladores.controlador_pagamento import ControladorPagamento
from controladores.controlador_passeio import ControladorPasseioTuristico
from controladores.controlador_pessoa import ControladorPessoa
from controladores.controlador_grupo import ControladorGrupo
from controladores.controlador_passagem import ControladorPassagem
from controladores.controlador_local_viagem import ControladorLocalViagem
from controladores.controlador_relatorio import ControladorRelatorio

from view.tela_sistema import TelaSistema

class ControladorSistema():
    
    def __init__(self):
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_grupo = ControladorGrupo(self)
        self.__controlador_local_viagem = ControladorLocalViagem()
        self.__controlador_passagem = ControladorPassagem(self)
        self.__controlador_pagamento = ControladorPagamento(self)
        self.__controlador_passeio = ControladorPasseioTuristico(self)
        self.__controlador_pacote = ControladorPacote(self)
        self.__tela_sistema = TelaSistema()
        self.__controlador_relatorio = ControladorRelatorio(self)
    
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
    
    @property 
    def controlador_pacote(self):
        return self.__controlador_pacote
    
    @property
    def controlador_pagamento(self):
        return self.__controlador_pagamento
    
    @property
    def controlador_passeio(self):
        return self.__controlador_passeio
    
    @property
    def controlador_relatorio(self):
        return self.__controlador_relatorio

    def inicializa_sistema(self):
        self.abre_tela()

    def pessoa(self):
        self.__controlador_pessoa.inicia()

    def grupo(self):
        self.__controlador_grupo.inicia()

    def local_viagem(self):
        self.__controlador_local_viagem.inicia()

    def passagem(self):
        self.__controlador_passagem.inicia()

    def pacote(self):
        self.__controlador_pacote.inicia()

    def passeio(self):
        self.__controlador_passeio.inicia()

    def relatorio(self):
        self.__controlador_relatorio.inicia()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.pessoa, 2: self.grupo, 3:self.local_viagem,
            4:self.passeio, 5:self.passagem, 6:self.pacote,
            7: self.relatorio, 0: self.encerra_sistema
        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
