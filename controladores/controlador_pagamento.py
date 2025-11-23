from datetime import datetime
from entidades.pagamento import Pagamento
from entidades.cartao_credito import CartaoCredito
from entidades.pix import Pix
from entidades.dinheiro import Dinheiro
from view.tela_pagamento import TelaPagamento
from DAOs.pagamento_dao import PagamentoDAO

class ControladorPagamento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__pagamentos_DAO = PagamentoDAO()
        self.__tela_pagamento = TelaPagamento()
        self.__proximo_id = self.__gerar_proximo_id()
        
    def __gerar_proximo_id(self):
        """Gera o próximo ID disponível baseado nos locais existentes"""
        pagamentos = list(self.__pagamentos_DAO.get_all())
        if not pagamentos:
            return 1
        
        max_id = max(pagamento.id for pagamento in pagamentos)
        return max_id + 1
    
    def buscar_por_id(self, pagamento_id):
        return self.__pagamentos_DAO.get(pagamento_id)

    def inicia(self, valor: float, pessoa):
        """
        Inicia o processo de pagamento e RETORNA o pagamento criado
        """
        switcher = {
            1: lambda: self.cria_pagamento_cartao(valor, pessoa),
            2: lambda: self.cria_pagamento_pix(valor, pessoa),
            3: lambda: self.cria_pagamento_dinheiro(valor, pessoa),
            0: lambda: None  # Retorna None se cancelar
        }
        
        while True:
            opcao = self.__tela_pagamento.mostra_opcoes()

            funcao_escolhida = switcher.get(
                opcao,
                lambda: self.__tela_pagamento.mostra_mensagem('Opção inválida.')
            )
            
            resultado = funcao_escolhida()
            
            # Se retornou um pagamento ou None (cancelamento), sai do loop
            if resultado is not None or opcao == 0:
                return resultado

    def cria_pagamento_cartao(self, valor: float, pessoa):
        while True:
            dados = self.__tela_pagamento.pega_dados_cartao(valor)
            
            if dados is None:
                return None

            # Validação do número de cartão
            num_cartao = dados['num_cartao']
            if not num_cartao.isdigit():
                self.__tela_pagamento.mostra_mensagem(
                    "Erro: O número do cartão deve conter apenas dígitos (0-9)."
                )
                continue
            
            try:
                parcelas = int(dados['parcelas'])
                if parcelas < 1:
                    raise ValueError("O número de parcelas deve ser no mínimo 1.")

            except ValueError:
                self.__tela_pagamento.mostra_mensagem(
                    "O número de parcelas deve ser um número inteiro positivo."
                )
                continue
            
            status_efetuado = self.__tela_pagamento.status_pagamento()

            try:
                pagamento = CartaoCredito(
                    id = self.__proximo_id,
                    pagante = pessoa,
                    valor = valor,
                    pagamento_efetuado = status_efetuado,
                    num_cartao = num_cartao,
                    bandeira = dados['bandeira'],
                    parcelas = parcelas
                )
                self.__pagamentos_DAO.add(pagamento)
                self.__proximo_id += 1
                
                valor_parcela = valor / parcelas

                self.__tela_pagamento.mostra_mensagem(
                    f"Pagamento de R$ {valor:.2f} em {parcelas}x de R$ {valor_parcela:.2f} realizado!"
                )
                return pagamento  # RETORNA O PAGAMENTO
            
            except (ValueError, TypeError) as e:
                self.__tela_pagamento.mostra_mensagem(f"Erro: {e}")
                return None
            
    def cria_pagamento_pix(self, valor: float, pessoa):
        while True:
            dados = self.__tela_pagamento.pega_dados_pix(valor)

            if dados is None:
                return None
            
            status_efetuado = self.__tela_pagamento.status_pagamento()
            
            try:
                pagamento = Pix(
                    id = self.__proximo_id,
                    pagante = pessoa,
                    valor = valor,
                    pagamento_efetuado = status_efetuado,
                    chave = dados['chave'],
                    banco = dados['banco']
                )
                self.__pagamentos_DAO.add(pagamento)
                self.__proximo_id += 1

                self.__tela_pagamento.mostra_mensagem(
                    f"Pagamento de R$ {valor:.2f} via PIX realizado!"
                )
                return pagamento  # RETORNA O PAGAMENTO

            except (TypeError, ValueError) as e:
                self.__tela_pagamento.mostra_mensagem(f"Erro: {e}")
                return None

    def cria_pagamento_dinheiro(self, valor: float, pessoa):
        while True:
            dados = self.__tela_pagamento.pega_dados_dinheiro(valor)
            
            if dados is None:
                return None
            
            try:
                valor_entregue = float(dados['valor_entregue'].replace(',', '.'))
                if valor_entregue < valor:
                    self.__tela_pagamento.mostra_mensagem(
                        f"Erro: Valor insuficiente! Faltam R$ {valor - valor_entregue:.2f}"
                    )
                    return None
            except ValueError:
                self.__tela_pagamento.mostra_mensagem(
                    "O valor entregue deve ser maior que o valor total."
                )
                continue
            
            status_efetuado = self.__tela_pagamento.status_pagamento()
                
            try:
                pagamento = Dinheiro(
                    id = self.__proximo_id,
                    pagante = pessoa,
                    valor = valor,
                    pagamento_efetuado = status_efetuado,
                    valor_entregue = valor_entregue
                )
                
                troco = pagamento.calc_troco()
                self.__pagamentos_DAO.add(pagamento)
                self.__proximo_id += 1
                
                self.__tela_pagamento.mostra_mensagem(
                    f"Pagamento de R$ {valor:.2f} realizado!"
                )
                if troco > 0:
                    self.__tela_pagamento.mostra_mensagem(f"Troco: R$ {troco:.2f}")
                
                return pagamento  # RETORNA O PAGAMENTO

            except (ValueError, TypeError) as e:
                self.__tela_pagamento.mostra_mensagem(f"Erro: {e}")
                return None

    def pagamentos_para_dict(self):
        pagamentos = list(self.__pagamentos_DAO.get_all())
        pagamentos_dict = []

        for pagamento in pagamentos:
            pagamentos_dict.append(pagamento.conversao_dict())
        return pagamentos_dict
    
    def listar_pagamentos(self):
        pagamentos = list(self.__pagamentos_DAO.get_all())

        if not pagamentos:
            self.__tela_pagamento.mostra_mensagem('Nenhum pagamento foi realizado.')
        else:
            self.__tela_pagamento.lista_pagamentos(self.pagamentos_para_dict())
            
    def obter_pagamentos(self):
        return list(self.__pagamentos_DAO.get_all())

    def confirmar_cancelamento_pagamento(self, pagamento):
        """Confirma o cancelamento através da tela"""
        return self.__tela_pagamento.confirma_cancelamento(
            pagamento.valor,
            pagamento.pagante.nome
    )

    def remover_pagamento_dao(self, id_pagamento):
        """Remove um pagamento do DAO"""
        try:
            self.__pagamentos_DAO.remove(id_pagamento)
            return True
        except:
            return False
    
    def sair(self):
        self.__tela_pagamento.mostra_mensagem('Encerrando.')
        return None  # Retorna None ao invés de True