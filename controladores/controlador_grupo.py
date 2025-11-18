
from entidades.grupo import Grupo
from view.tela_grupo import TelaGrupo
from DAO.grupo_dao import GrupoDAO

class ControladorGrupo:
    def __init__(self, controlador_pessoa):
        self.__grupo_dao = GrupoDAO() 
        self.__tela_grupo = TelaGrupo()
        self.controlador_pessoa = controlador_pessoa
        self.__proximo_id = self.__gerar_proximo_id()

    def __gerar_proximo_id(self):
        """Gera o próximo ID disponível baseado nos grupos existentes"""
        grupos = list(self.__grupo_dao.get_all())
        if not grupos:
            return 1
        
        max_id = max(grupo.id for grupo in grupos)
        return max_id + 1

    def inicia(self):
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
        """Cria um novo grupo e persiste no arquivo"""
        try:
            dados_grupo = self.__tela_grupo.pega_dados_grupo()
            nome_grupo = dados_grupo['nome']
            descricao = dados_grupo.get('descricao', '')

            if self.buscar_por_nome(nome_grupo):
                self.__tela_grupo.mostra_mensagem(f"Já existe um grupo com o nome '{nome_grupo}'!")
                return

            # Cria o grupo com ID único
            grupo = Grupo(self.__proximo_id, nome_grupo, descricao)
            
            self.__grupo_dao.add(grupo)

            self.__proximo_id += 1

            self.__tela_grupo.mostra_mensagem(f"Grupo '{nome_grupo}' criado com sucesso!")
        
        except Exception as e:
            self.__tela_grupo.mostra_mensagem(f"Erro ao criar grupo: {str(e)}")

    def listar_grupos(self):
        grupos = list(self.__grupo_dao.get_all())
        
        if not grupos:
            self.__tela_grupo.mostra_mensagem("Nenhum grupo cadastrado no sistema.")
            return

        dados_grupos = []
        for grupo in grupos:
            dados_grupos.append({
                'id': grupo.id,
                'nome': grupo.nome,
                'descricao': grupo.descricao,
                'total_membros': grupo.total_membros()
            })

        self.__tela_grupo.lista_grupos(dados_grupos)

    def excluir_grupo(self):
        grupos = list(self.__grupo_dao.get_all())
        
        if not grupos:
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

            # Desvincula todos os membros
            for cpf in grupo.obter_lista_membros():
                self.controlador_pessoa.desvincular_grupo(cpf)

            self.__grupo_dao.remove(id_grupo)
            
            self.__tela_grupo.mostra_mensagem(f"Grupo '{grupo.nome}' excluído com sucesso!")

        except Exception as e:
            self.__tela_grupo.mostra_mensagem(f"Erro ao excluir grupo: {str(e)}")

    # ====== OPERAÇÕES COM MEMBROS ======

    def incluir_pessoa_grupo(self):
        grupos = list(self.__grupo_dao.get_all())
        
        if not grupos:
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

            self.__grupo_dao.update(grupo)

            self.__tela_grupo.mostra_mensagem(f"{pessoa.nome} adicionado(a) ao grupo '{grupo.nome}' com sucesso!")

        except Exception as e:
            self.__tela_grupo.mostra_mensagem(f"Erro ao incluir pessoa no grupo: {str(e)}")

    def listar_pessoas_grupo(self):
        grupos = list(self.__grupo_dao.get_all())
        
        if not grupos:
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
        """Remove uma pessoa de um grupo"""
        grupos = list(self.__grupo_dao.get_all())
        
        if not grupos:
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

            # Remove do grupo
            grupo.remover_membro(cpf)

            self.controlador_pessoa.desvincular_grupo(cpf)

            self.__grupo_dao.update(grupo)

            nome_pessoa = pessoa.nome if pessoa else "Pessoa"
            self.__tela_grupo.mostra_mensagem(f"{nome_pessoa} removido(a) do grupo '{grupo.nome}' com sucesso!")

        except Exception as e:
            self.__tela_grupo.mostra_mensagem(f"Erro ao remover pessoa do grupo: {str(e)}")

    # ====== MÉTODOS AUXILIARES ======

    def buscar_por_id(self, grupo_id):
        return self.__grupo_dao.get(grupo_id)

    def buscar_por_nome(self, nome_grupo):
        grupos = list(self.__grupo_dao.get_all())
        for grupo in grupos:
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
    
    def obter_todos_grupos(self):
        return list(self.__grupo_dao.get_all())

    def sair(self):
        self.__tela_grupo.mostra_mensagem('Encerrando o gerenciamento de grupos.')
        return True


