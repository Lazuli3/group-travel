from entidades.grupo import Grupo
from view.tela_grupo import TelaGrupo

class ControladorGrupo:
    def __init__(self, controlador_pessoa):
        self.__grupos = []
        self.__tela_grupo = TelaGrupo()
        self.controlador_pessoa = controlador_pessoa
        self.__proximo_id = 1

    def inicia(self):
        """Menu principal do controlador de grupos"""
        opcoes = {
            1: self.criar_grupo,
            2: self.listar_grupos,
            3: self.incluir_pessoa_grupo,
            4: self.listar_pessoas_grupo,
            5: self.excluir_pessoa_grupo,
            6: self.excluir_grupo,
            0: self.sair
        }

        while True:
            opcao = self.__tela_grupo.mostra_opcoes()

            if opcao in opcoes:
                resultado = opcoes[opcao]()
                if resultado is True:
                    break
            else:
                self.__tela_grupo.mostra_mensagem('Opção inválida.')

    # ====== OPERAÇÕES COM GRUPOS ======

    def criar_grupo(self):
        try:
            dados_grupo = self.__tela_grupo.pega_dados_grupo()
            nome_grupo = dados_grupo['nome']
            descricao = dados_grupo.get('descricao', '')

            if self.buscar_por_nome(nome_grupo):
                self.__tela_grupo.mostra_mensagem(f"Já existe um grupo com o nome '{nome_grupo}'!")
                return

            grupo = Grupo(self.__proximo_id, nome_grupo, descricao)
            self.__grupos.append(grupo)
            self.__proximo_id += 1

            self.__tela_grupo.mostra_mensagem(f"Grupo '{nome_grupo}' criado com sucesso!")
        
        except Exception as e:
            self.__tela_grupo.mostra_mensagem(f"Erro ao criar grupo: {str(e)}")

    def listar_grupos(self):
        if not self.__grupos:
            self.__tela_grupo.mostra_mensagem("Nenhum grupo cadastrado no sistema.")
            return

        dados_grupos = []
        for grupo in self.__grupos:
            dados_grupos.append({
                'id': grupo.id,
                'nome': grupo.nome,
                'descricao': grupo.descricao,
                'total_membros': grupo.total_membros()
            })

        self.__tela_grupo.lista_grupos(dados_grupos)

    def excluir_grupo(self):
        if not self.__grupos:
            self.__tela_grupo.mostra_mensagem("Nenhum grupo cadastrado no sistema.")
            return

        try:
            self.listar_grupos()
            
            id_grupo = self.__tela_grupo.seleciona_grupo()
            grupo = self.buscar_por_id(id_grupo)

            if not grupo:
                self.__tela_grupo.mostra_mensagem(f"Grupo com ID {id_grupo} não encontrado!")
                return

            confirmacao = self.__tela_grupo.confirma_exclusao(grupo.nome)
            if not confirmacao:
                self.__tela_grupo.mostra_mensagem("Exclusão cancelada.")
                return

            for cpf in grupo.obter_lista_membros():
                self.controlador_pessoa.desvincular_grupo(cpf)

            self.__grupos.remove(grupo)
            self.__tela_grupo.mostra_mensagem(f"Grupo '{grupo.nome}' excluído com sucesso!")

        except Exception as e:
            self.__tela_grupo.mostra_mensagem(f"Erro ao excluir grupo: {str(e)}")

    # ====== OPERAÇÕES COM MEMBROS ======

    def incluir_pessoa_grupo(self):
        if not self.__grupos:
            self.__tela_grupo.mostra_mensagem("Nenhum grupo cadastrado. Crie um grupo primeiro!")
            return

        try:
            self.listar_grupos()
            
            id_grupo = self.__tela_grupo.seleciona_grupo()
            grupo = self.buscar_por_id(id_grupo)

            if not grupo:
                self.__tela_grupo.mostra_mensagem(f"Grupo com ID {id_grupo} não encontrado!")
                return

            self.controlador_pessoa.listar_pessoa()

            cpf = self.__tela_grupo.pega_cpf_pessoa()

            pessoa = self.controlador_pessoa.buscar_por_cpf(cpf)
            if not pessoa:
                self.__tela_grupo.mostra_mensagem(f"Pessoa com CPF {cpf} não encontrada!")
                return

            if not grupo.adicionar_membro(cpf):
                self.__tela_grupo.mostra_mensagem(f"{pessoa.nome} já é membro do grupo '{grupo.nome}'!")
                return

            self.controlador_pessoa.vincular_grupo(cpf, grupo.id)

            self.__tela_grupo.mostra_mensagem(f"{pessoa.nome} adicionado(a) ao grupo '{grupo.nome}' com sucesso!")

        except Exception as e:
            self.__tela_grupo.mostra_mensagem(f"Erro ao incluir pessoa no grupo: {str(e)}")

    def listar_pessoas_grupo(self):
        if not self.__grupos:
            self.__tela_grupo.mostra_mensagem("Nenhum grupo cadastrado no sistema.")
            return

        try:
            self.listar_grupos()
            
            id_grupo = self.__tela_grupo.seleciona_grupo()
            grupo = self.buscar_por_id(id_grupo)

            if not grupo:
                self.__tela_grupo.mostra_mensagem(f"Grupo com ID {id_grupo} não encontrado!")
                return

            if grupo.total_membros() == 0:
                self.__tela_grupo.mostra_mensagem(f"O grupo '{grupo.nome}' não possui membros.")
                return

            membros = []
            for cpf in grupo.obter_lista_membros():
                pessoa = self.controlador_pessoa.buscar_por_cpf(cpf)
                if pessoa:
                    membros.append({
                        'nome': pessoa.nome,
                        'cpf': pessoa.cpf,
                        'telefone': pessoa.telefone,
                    })

            self.__tela_grupo.lista_membros(grupo.nome, membros)

        except Exception as e:
            self.__tela_grupo.mostra_mensagem(f"Erro ao listar membros: {str(e)}")

    def excluir_pessoa_grupo(self):
        if not self.__grupos:
            self.__tela_grupo.mostra_mensagem("Nenhum grupo cadastrado no sistema.")
            return

        try:
            self.listar_grupos()
            
            id_grupo = self.__tela_grupo.seleciona_grupo()
            grupo = self.buscar_por_id(id_grupo)

            if not grupo:
                self.__tela_grupo.mostra_mensagem(f"Grupo com ID {id_grupo} não encontrado!")
                return

            if grupo.total_membros() == 0:
                self.__tela_grupo.mostra_mensagem(f"O grupo '{grupo.nome}' não possui membros.")
                return

            self.listar_pessoas_grupo()

            cpf = self.__tela_grupo.pega_cpf_pessoa()

            if not grupo.tem_membro(cpf):
                self.__tela_grupo.mostra_mensagem(f"Pessoa com CPF {cpf} não é membro do grupo!")
                return

            pessoa = self.controlador_pessoa.buscar_por_cpf(cpf)

            grupo.remover_membro(cpf)

            self.controlador_pessoa.desvincular_grupo(cpf)

            nome_pessoa = pessoa.nome if pessoa else "Pessoa"
            self.__tela_grupo.mostra_mensagem(f"{nome_pessoa} removido(a) do grupo '{grupo.nome}' com sucesso!")

        except Exception as e:
            self.__tela_grupo.mostra_mensagem(f"Erro ao remover pessoa do grupo: {str(e)}")

    # métodos criados pra eu conseguir fazer as buscas e etc

    def buscar_por_id(self, grupo_id):
        for grupo in self.__grupos:
            if grupo.id == grupo_id:
                return grupo
        return None

    def buscar_por_nome(self, nome_grupo):
        for grupo in self.__grupos:
            if grupo.nome.lower() == nome_grupo.lower():
                return grupo
        return None

    def obter_membros(self, grupo_id):
        grupo = self.buscar_por_id(grupo_id)
        if not grupo:
            return []

        membros = []
        for cpf in grupo.obter_lista_membros():
            pessoa = self.controlador_pessoa.buscar_por_cpf(cpf)
            if pessoa:
                membros.append(pessoa)
        return membros

    def sair(self):
        self.__tela_grupo.mostra_mensagem('Encerrando o gerenciamento de grupos.')
        return True