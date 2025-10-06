from entidades.local_viagem import LocalViagem
from view.tela_local_viagem import TelaLocalViagem

class ControladorLocalViagem:
    def __init__(self):
        self.__locais_viagem = []
        self.__tela_local_viagem = TelaLocalViagem()

    def inicia(self):
        switcher = {
            1: self.incluir_local_viagem,
            2: self.listar_locais_viagem,
            3: self.excluir_local_viagem,
            0: self.sair
        }

        while True:
            opcao = self.__tela_local_viagem.mostra_opcoes()

            funcao_escolhida = switcher.get(
                opcao,
                lambda: self.__tela_local_viagem.mostra_mensagem(
                    'Opção inválida.'
                ) #get: se switcher[opcao] for inválido -> retorna a função lambda
            )
            if funcao_escolhida() is True:
                break

    def incluir_local_viagem(self):
        dados = self.__tela_local_viagem.pega_dados_local_viagem()
        novo = LocalViagem(**dados) #Desempacota o dicionário
        self.__locais_viagem.append(novo)
        self.__tela_local_viagem.mostra_mensagem('Local de viagem cadastrado.')

    def listar_locais_viagem(self):
        if not self.__locais_viagem:
            self.__tela_local_viagem.mostra_mensagem('Nenhum local de viagem cadastrado.')
        else:
            self.__tela_local_viagem.lista_locais_viagem(self.__locais_viagem) #passar lista de dicionários ao invés da lista privada

    def excluir_local_viagem(self):
        if not self.__locais_viagem:
            return

        indice = self.__tela_local_viagem.seleciona_local(self.__locais_viagem)

        if indice is None:
            return

        if 0 <= indice < len(self.__locais_viagem):
            local_excluido = self.__locais_viagem[indice]
            del self.__locais_viagem[indice]
            self.__tela_local_viagem.mostra_mensagem(
            f"Local '{local_excluido.cidade}, {local_excluido.pais}' excluído com sucesso!"
            )
        else:
            self.__tela_local_viagem.mostra_mensagem("Número inválido.")

    def sair(self):
        self.__tela_local_viagem.mostra_mensagem('Encerrando o cadastro.')
        return True
