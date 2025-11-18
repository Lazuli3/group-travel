from entidades.pessoa import Pessoa
from view.tela_pessoa import TelaPessoa

from DAOs.pessoa_dao import PessoaDAO

class ControladorPessoa:

    def __init__(self):
        self.__pessoa_dao = PessoaDAO()
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
            
            if self.buscar_por_cpf(dados['cpf']):
                self.__tela_pessoa.mostra_mensagem(f"Pessoa com CPF {dados['cpf']} já cadastrada!")
                return
            
            nova = Pessoa(**dados)
            self.__pessoa_dao.add(nova)
            
            self.__tela_pessoa.mostra_mensagem("Pessoa cadastrada com sucesso.")
        
        except Exception as e:
            self.__tela_pessoa.mostra_mensagem(f"Erro ao cadastrar pessoa: {str(e)}")

    def listar_pessoa(self):
        """Lista todas as pessoas cadastradas"""
        pessoas = list(self.__pessoa_dao.get_all())
        
        if not pessoas:
            self.__tela_pessoa.mostra_mensagem('Nenhuma pessoa cadastrada')
        else:
            self.__tela_pessoa.lista_pessoas(pessoas)

    def excluir_pessoa(self):
        """Exclui uma pessoa do sistema"""
        try:
            cpf = self.__tela_pessoa.pega_cpf()
            pessoa = self.buscar_por_cpf(cpf)
            
            if pessoa:
                self.__pessoa_dao.remove(cpf)
                self.__tela_pessoa.mostra_mensagem(f"A pessoa {pessoa.nome} foi removida com sucesso.")
            else:
                self.__tela_pessoa.mostra_mensagem("Essa pessoa não está cadastrada no sistema.")
        
        except Exception as e:
            self.__tela_pessoa.mostra_mensagem(f"Erro ao excluir pessoa: {str(e)}")

    # ====== MÉTODOS AUXILIARES ======

    def buscar_por_cpf(self, cpf):
        """Busca uma pessoa pelo CPF"""
        return self.__pessoa_dao.get(cpf)

    def validar_existencia(self, cpf):
        """Valida se uma pessoa existe no sistema"""
        return self.buscar_por_cpf(cpf) is not None

    def vincular_grupo(self, cpf, grupo_id):
        """Vincula uma pessoa a um grupo"""
        pessoa = self.buscar_por_cpf(cpf)
        if pessoa:
            pessoa.grupo_id = grupo_id
            self.__pessoa_dao.update(pessoa)
            return True
        return False

    def desvincular_grupo(self, cpf):
        """Desvincula uma pessoa de um grupo"""
        pessoa = self.buscar_por_cpf(cpf)
        if pessoa:
            pessoa.grupo_id = None
            self.__pessoa_dao.update(pessoa)
            return True
        return False

    def listar_por_grupo(self, grupo_id):
        """Lista todas as pessoas de um grupo específico"""
        pessoas = list(self.__pessoa_dao.get_all())
        return [p for p in pessoas if hasattr(p, 'grupo_id') and p.grupo_id == grupo_id]

    def listar_sem_grupo(self):
        """Lista pessoas que não estão em nenhum grupo"""
        pessoas = list(self.__pessoa_dao.get_all())
        return [p for p in pessoas if not hasattr(p, 'grupo_id') or p.grupo_id is None]

    def obter_todas_pessoas(self):
        """Retorna lista de todas as pessoas"""
        return list(self.__pessoa_dao.get_all())

    def sair(self):
        """Sai do menu de pessoas"""
        self.__tela_pessoa.mostra_mensagem('Encerrando a tela pessoa.')
        return True