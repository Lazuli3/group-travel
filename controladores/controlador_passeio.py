from entidades.passeio_turistico import *
from view.tela_passeio import TelaPasseioTuristico

class ControladorPasseioTuristico:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__locais_viagem = locais_viagem
        self.__grupos = grupos
        self.__passeios = []
        self._tela_passeio = TelaPasseioTuristico()

    def inicia(self):
        switcher = {
            1: self.incluir_passeio,
            2: self.listar_passeios,
            3: self.excluir_passeio,
            0: self.sair
        }

        while True:
            opcao = self.__tela_passeio.mostra_opcoes()

            funcao_escolhida = switcher.get(
                opcao,
                lambda: self.__tela_passeio.mostra_mensagem(
                    'Opção inválida.'
                )
            )
            if funcao_escolhida() is True:
                break

    def busca_local(self, cidade: str, pais: str):
        locais = self.__controlador_sistema.controlador_local_viagem.
    
    def incluir_passeio(self):
        dados = self.__tela_passeio.pega_dados_passeio()

        novo = PasseioTuristico(**dados)
        self.__locais_passeio.append(novo)