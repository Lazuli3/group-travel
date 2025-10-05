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
        dados = self.__tela_pessoa.pega_dados_pessoa()
        nova = Pessoa(**dados)
        self.__pessoas.append(nova)
        self.__tela_pessoa.mostra_mensagem("Pessoa cadastrada com sucesso.")

    def listar_pessoa(self):
        if not self.__pessoas:
            self.__tela_pessoa.mostra_mensagem('Nenhuma pessoa cadastrada')
        else:
            self.__tela_pessoa.lista_pessoas(self.__pessoas)

    def excluir_pessoa(self):
        cpf = self.__tela_pessoa.pega_cpf()
        pessoa = next((p for p in self.__pessoas if p.cpf == cpf), None)
        if pessoa:
            self.__pessoas.remove(pessoa)
            self.__tela_pessoa.mostra_mensagem(f"A pessoa {pessoa.nome} foi removida com sucesso.")
        else:
            self.__tela_pessoa.mostra_mensagem("Essa pessoa não está cadastrada no sistema.")

    def sair(self):
        self.__tela_pessoa.mostra_mensagem('Encerrando a tela pessoa.')
        return True
        