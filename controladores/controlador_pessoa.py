from entidades.pessoa import Pessoa
from view.tela_pessoa import TelaPessoa

class ControladorPessoa:

    def __init__(self):
        self.__pessoas = []
        self.__tela_pessoa = TelaPessoa()

    def inicia(self):
        opcoes = {
            1: self.incluir_pessoa,
            2: self.listar_pessoa,
            3: self.excluir_pessoa,
            0: self.sair
        }

        while True:
            opcao = self.__tela_pessoa.mostra_opcoes()

            if opcao in opcoes:
                resultado = opcoes[opcao]()
                if resultado is True:
                    break
            else:
                self.__tela_pessoa.mostra_mensagem('Opção inválida.')

    def incluir_pessoa(self):
        """Cadastra uma nova pessoa"""
        try:
            dados = self.__tela_pessoa.pega_dados_pessoa()
            
            # Verifica se CPF já existe
            if self.buscar_por_cpf(dados['cpf']):
                self.__tela_pessoa.mostra_mensagem(f"Pessoa com CPF {dados['cpf']} já cadastrada!")
                return
            
            nova = Pessoa(**dados)
            self.__pessoas.append(nova)
            self.__tela_pessoa.mostra_mensagem("Pessoa cadastrada com sucesso.")
        
        except Exception as e:
            self.__tela_pessoa.mostra_mensagem(f"Erro ao cadastrar pessoa: {str(e)}")

    def listar_pessoa(self):
        """Lista todas as pessoas cadastradas"""
        if not self.__pessoas:
            self.__tela_pessoa.mostra_mensagem('Nenhuma pessoa cadastrada')
        else:
            self.__tela_pessoa.lista_pessoas(self.__pessoas)

    def excluir_pessoa(self):
        """Exclui uma pessoa do sistema"""
        try:
            cpf = self.__tela_pessoa.pega_cpf()
            pessoa = self.buscar_por_cpf(cpf)
            
            if pessoa:
                self.__pessoas.remove(pessoa)
                self.__tela_pessoa.mostra_mensagem(f"A pessoa {pessoa.nome} foi removida com sucesso.")
            else:
                self.__tela_pessoa.mostra_mensagem("Essa pessoa não está cadastrada no sistema.")
        
        except Exception as e:
            self.__tela_pessoa.mostra_mensagem(f"Erro ao excluir pessoa: {str(e)}")

    # ====== MÉTODOS PARA INTEGRAÇÃO COM CONTROLADOR DE GRUPO ======

    def buscar_por_cpf(self, cpf):
        """Busca uma pessoa pelo CPF - usado pelo ControladorGrupo"""
        for pessoa in self.__pessoas:
            if pessoa.cpf == cpf:
                return pessoa
        return None

    def validar_existencia(self, cpf):
        """Valida se uma pessoa existe no sistema"""
        return self.buscar_por_cpf(cpf) is not None

    def vincular_grupo(self, cpf, grupo_id):
        """Vincula uma pessoa a um grupo"""
        pessoa = self.buscar_por_cpf(cpf)
        if pessoa:
            pessoa.grupo_id = grupo_id
            return True
        return False

    def desvincular_grupo(self, cpf):
        """Desvincula uma pessoa de um grupo"""
        pessoa = self.buscar_por_cpf(cpf)
        if pessoa:
            pessoa.grupo_id = None
            return True
        return False

    def listar_por_grupo(self, grupo_id):
        """Lista todas as pessoas de um grupo específico"""
        return [p for p in self.__pessoas if hasattr(p, 'grupo_id') and p.grupo_id == grupo_id]

    def listar_sem_grupo(self):
        """Lista pessoas que não estão em nenhum grupo"""
        return [p for p in self.__pessoas if not hasattr(p, 'grupo_id') or p.grupo_id is None]

    def obter_todas_pessoas(self):
        """Retorna lista de todas as pessoas (para uso externo)"""
        return self.__pessoas.copy()

    def sair(self):
        """Sai do menu de pessoas"""
        self.__tela_pessoa.mostra_mensagem('Encerrando a tela pessoa.')
        return True