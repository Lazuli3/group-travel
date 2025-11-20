from entidades.local_viagem import LocalViagem
from view.tela_local_viagem import TelaLocalViagem
from DAOs.local_dao import LocalViagemDAO

class ControladorLocalViagem:
    def __init__(self):
        self.__locais_DAO = LocalViagemDAO()
        self.__tela_local_viagem = TelaLocalViagem()
        self.__proximo_id = self.__gerar_proximo_id()

    def __gerar_proximo_id(self):
        """Gera o próximo ID disponível baseado nos locais existentes"""
        locais = list(self.__locais_DAO.get_all())
        if not locais:
            return 1
        
        max_id = max(local.id for local in locais)
        return max_id + 1

    def buscar_por_id(self, local_id):
        return self.__locais_DAO.get(local_id)

    def __local_ja_existe(self, cidade, pais):
        """Verifica se já existe um local com a mesma cidade e país"""
        for local in self.__locais_DAO.get_all():
            if (local.cidade.lower().strip() == cidade.lower().strip() and 
                local.pais.lower().strip() == pais.lower().strip()):
                return True
        return False

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

        if self.__local_ja_existe(dados['cidade'], dados['pais']):
            self.__tela_local_viagem.mostra_mensagem(
                f"O local '{dados['cidade']}, {dados['pais']}' já está cadastrado!"
            )
            return

        novo = LocalViagem(self.__proximo_id, dados['cidade'], dados['pais']) #Desempacota o dicionário

        self.__locais_DAO.add(novo)
        
        self.__proximo_id += 1

        self.__tela_local_viagem.mostra_mensagem('Local de viagem cadastrado.')

    def obter_locais(self):
        '''Retorna a lista de locais, mas sem exibir'''
        return list(self.__locais_DAO.get_all())

    def listar_locais_viagem(self):
        locais = list(self.__locais_DAO.get_all())
        
        if not locais:
            self.__tela_local_viagem.mostra_mensagem('Nenhum local de viagem cadastrado.')
            return

        dados_locais = []
        for local in locais:
            dados_locais.append({
                'id': local.id,
                'cidade': local.cidade,
                'pais': local.pais
            })

        self.__tela_local_viagem.lista_locais_viagem(dados_locais)

    def excluir_local_viagem(self):
        locais = list(self.__locais_DAO.get_all())
        
        if not self.__locais_DAO:
            self.__tela_local_viagem.mostra_mensagem("Nenhum local de viagem cadastrado.")
            return
        
        try:
            self.listar_locais_viagem()
            
            id_local = self.__tela_local_viagem.seleciona_local()
            local = self.buscar_por_id(id_local)

            if not local:
                self.__tela_local_viagem.mostra_mensagem(f"Local com ID {id_local} não encontrado!")
                return

            confirmacao = self.__tela_local_viagem.confirma_exclusao(local.cidade, local.pais)
            if not confirmacao:
                self.__tela_local_viagem.mostra_mensagem("Exclusão cancelada.")
                return

            self.__locais_DAO.remove(id_local)

            self.__tela_local_viagem.mostra_mensagem(
            f"Local '{local.cidade}, {local.pais}' excluído com sucesso!"
            )
        
        except Exception as e:
            self.__tela_local_viagem.mostra_mensagem(f"Erro ao excluir grupo: {str(e)}")

    def sair(self):
        self.__tela_local_viagem.mostra_mensagem('Encerrando o cadastro.')
        return True
