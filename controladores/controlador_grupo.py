
from entidades.grupo import Grupo
from view.tela_grupo import TelaGrupo
from DAOs.grupo_dao import GrupoDAO

class ControladorGrupo:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__grupo_dao = GrupoDAO() 
        self.__tela_grupo = TelaGrupo()
        self.__proximo_id = self.__gerar_proximo_id()

    def __gerar_proximo_id(self):
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
            5: self.remover_pessoa_de_grupo,
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

    def criar_grupo(self):
        try:
            dados_grupo = self.__tela_grupo.pega_dados_grupo()
            nome_grupo = dados_grupo['nome']
            descricao = dados_grupo.get('descricao', '')

            if self.buscar_por_nome(nome_grupo):
                self.__tela_grupo.mostra_mensagem(f"Já existe um grupo com o nome '{nome_grupo}'!")
                return

            #criando um id dentro do controlador
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

            # CORRETO: Usa método público do controlador de pacotes
            if self.__controlador_sistema:
                if self.__controlador_sistema.controlador_pacote.grupo_tem_pacotes(id_grupo):
                    qtd = self.__controlador_sistema.controlador_pacote.contar_pacotes_do_grupo(id_grupo)
                    self.__tela_grupo.mostra_mensagem(
                        f"❌ Não é possível excluir!\n"
                        f"O grupo possui {qtd} pacote(s) vinculado(s).\n"
                        "Exclua os pacotes primeiro."
                    )
                    return

            confirmacao = self.__tela_grupo.confirma_exclusao(grupo.nome)
            if not confirmacao:
                self.__tela_grupo.mostra_mensagem("Exclusão cancelada.")
                return

            # Desvincula todos os membros do grupo
            for cpf in grupo.obter_lista_membros():
                self.__controlador_sistema.controlador_pessoa.desvincular_grupo(cpf)

            self.__grupo_dao.remove(id_grupo)
            
            self.__tela_grupo.mostra_mensagem(f"Grupo '{grupo.nome}' excluído com sucesso!")

        except Exception as e:
            self.__tela_grupo.mostra_mensagem(f"Erro ao excluir grupo: {str(e)}")

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

            self.__controlador_sistema.controlador_pessoa.listar_pessoa()

            cpf = self.__tela_grupo.pega_cpf_pessoa()

            pessoa = self.__controlador_sistema.controlador_pessoa.buscar_por_cpf(cpf)
            if not pessoa:
                self.__tela_grupo.mostra_mensagem(f"Pessoa com CPF {cpf} não encontrada!")
                return

            if not grupo.adicionar_membro(cpf):
                self.__tela_grupo.mostra_mensagem(f"{pessoa.nome} já é membro do grupo '{grupo.nome}'!")
                return
            
            self.__controlador_sistema.controlador_pessoa.vincular_grupo(cpf, grupo.id)

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
                pessoa = self.__controlador_sistema.controlador_pessoa.buscar_por_cpf(cpf)
                if pessoa:
                    membros.append({
                        'nome': pessoa.nome,
                        'cpf': pessoa.cpf,
                        'telefone': pessoa.telefone,
                    })

            self.__tela_grupo.lista_membros(grupo.nome, membros)

        except Exception as e:
            self.__tela_grupo.mostra_mensagem(f"Erro ao listar membros: {str(e)}")


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

            # VERIFICA INTEGRIDADE: Usa método público do controlador de pacotes
            if self.__controlador_sistema:
                if self.__controlador_sistema.controlador_pacote.grupo_tem_pacotes(id_grupo):
                    qtd = self.__controlador_sistema.controlador_pacote.contar_pacotes_do_grupo(id_grupo)
                    
                    # Pergunta se quer excluir em cascata
                    confirmacao_cascata = self.__tela_grupo.confirma_exclusao_cascata(
                        grupo.nome, 
                        qtd
                    )
                    
                    if not confirmacao_cascata:
                        self.__tela_grupo.mostra_mensagem("Exclusão cancelada.")
                        return
                    
                    # Exclui os pacotes do grupo
                    pacotes_excluidos = self.__controlador_sistema.controlador_pacote.excluir_pacotes_do_grupo(id_grupo)
                    self.__tela_grupo.mostra_mensagem(
                        f"{len(pacotes_excluidos)} pacote(s) excluído(s)."
                    )

            confirmacao = self.__tela_grupo.confirma_exclusao(grupo.nome)
            if not confirmacao:
                self.__tela_grupo.mostra_mensagem("Exclusão cancelada.")
                return

            # Desvincula todos os membros do grupo
            for cpf in grupo.obter_lista_membros():
                self.__controlador_sistema.controlador_pessoa.desvincular_grupo(cpf)

            self.__grupo_dao.remove(id_grupo)
            
            self.__tela_grupo.mostra_mensagem(f"✅ Grupo '{grupo.nome}' excluído com sucesso!")

        except Exception as e:
            self.__tela_grupo.mostra_mensagem(f"Erro ao excluir grupo: {str(e)}")

    #metodos para integração com outras classes

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
            pessoa = self.__controlador_sistema.controlador_pessoa.buscar_por_cpf(cpf)
            if pessoa:
                membros.append(pessoa)
        return membros
    
    def obter_todos_grupos(self):
        return list(self.__grupo_dao.get_all())

    def sair(self):
        self.__tela_grupo.mostra_mensagem('Encerrando o gerenciamento de grupos.')
        return True

    def pessoa_esta_em_grupo(self, cpf):
            """Verifica se uma pessoa está em algum grupo e retorna o grupo"""
            grupos = list(self.__grupo_dao.get_all())
            for grupo in grupos:
                if grupo.tem_membro(cpf):
                    return grupo
            return None
    
    def remover_pessoa_de_grupo(self, cpf):
        """Remove uma pessoa de seu grupo (se estiver em algum)"""
        grupo = self.pessoa_esta_em_grupo(cpf)
        if grupo:
            grupo.remover_membro(cpf)
            self.__grupo_dao.update(grupo)
            return True
        return False

