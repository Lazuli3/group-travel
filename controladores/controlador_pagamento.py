from datetime import datetime
from entidades.pagamento import Pagamento
from entidades.cartao_credito import CartaoCredito
from entidades.pix import Pix
from entidades.dinheiro import Dinheiro
from view.tela_pagamento import TelaPagamento

class ControladorPagamento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__pagamentos = []
        self.__tela_pagamento = TelaPagamento()

    def criar_pagamento(self, valor: float, pessoa):
        switcher = {
            1: lambda: self.cria_pagamento_cartao(valor, pessoa),
            2: lambda: self.cria_pagamento_pix(valor, pessoa),
            3: lambda: self.cria_pagamento_dinheiro(valor, pessoa),
            0: lambda: self.sair()
        }
        
        while True:
            opcao = self.__tela_pagamento.mostra_opcoes()

            funcao_escolhida = switcher.get(
                opcao,
                lambda: self.__tela_pagamento.mostra_mensagem(
                    'Opção inválida.'
                )
            )
            
            if funcao_escolhida() is True:
                break

    def cria_pagamento_cartao(self, valor: float, pessoa):
        while True:
            dados = self.__tela_pagamento.pega_dados_cartao(valor)
            
            if dados is None:
                return

            # Validação do número de cartão
            num_cartao = dados['num_cartao']
            if not num_cartao.isdigit() or not (13 <= len(num_cartao) <= 19):
                self.__tela_pagamento.mostra_mensagem(
                    "Erro: O número do cartão deve conter apenas dígitos (0-9) e ter entre 13 e 19 caracteres."
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

            try:
                pagamento = CartaoCredito(
                    pagante = pessoa,
                    valor = valor,
                    num_cartao = num_cartao,
                    parcelas = parcelas
                )
                self.__pagamentos.append(pagamento)
                
                valor_parcela = valor / parcelas

                self.__tela_pagamento.mostra_mensagem(
                    f"Pagamento de R$ {valor:.2f} em {parcelas}x de R$ {valor_parcela:.2f} realizado!"
                )
                return pagamento
            
            except (ValueError, TypeError) as e:
                self.__tela_pagamento.mostra_mensagem(f"Erro: {e}")
                return None
            
    def cria_pagamento_pix(self, valor: float, pessoa):
        while True:
            dados = self.__tela_pagamento.pega_dados_pix(valor)

            if dados is None:
                return
            
            try:
                pagamento = Pix(
                    pagante = pessoa,
                    valor = valor,
                    chave = dados['chave'],
                    banco = dados['banco']
                )
                self.__pagamentos.append(pagamento)

                self.__tela_pagamento.mostra_mensagem(
                    f"Pagamento de R$ {valor:.2f} via PIX realizado!"
                )
                return pagamento

            except (TypeError, ValueError) as e:
                self.__tela_pagamento.mostra_mensagem(f"Erro: {e}")
                return None

    def cria_pagamento_dinheiro(self, valor: float, pessoa):
        dados = self.__tela_pagamento.pega_dados_dinheiro(valor)
        
        try:
            valor_entregue = float(dados['valor_entregue'].replace(',', '.'))
            
            if valor_entregue < valor:
                self.__tela_pagamento.mostra_mensagem(
                    f"Erro: Valor insuficiente! Faltam R$ {valor - valor_entregue:.2f}"
                )
                return None
            
            pagamento = Dinheiro(
                pagante = pessoa,
                valor = valor,
                valor_entregue = valor_entregue
            )
            
            troco = pagamento.calc_troco()
            self.__pagamentos.append(pagamento)
            
            self.__tela_pagamento.mostra_mensagem(
                f"Pagamento de R$ {valor:.2f} realizado!"
            )
            if troco > 0:
                self.__tela_pagamento.mostra_mensagem(f"Troco: R$ {troco:.2f}")
            
            return pagamento

        except (ValueError, TypeError) as e:
            self.__tela_pagamento.mostra_mensagem(f"Erro: {e}")
            return None

    def pagamentos_para_dict(self):
        pagamentos_dict = []
        for pag in self.__pagamentos:
            pagamentos_dict.append(pag.conversao_dict())
        return pagamentos_dict
    
    def listar_pagamentos(self):
        if not self.__pagamentos:
            self.__tela_pagamento.mostra_mensagem('Nenhum pagamento foi realizado.')
        else:
            self.__tela_pagamento.lista_pagamentos(self.pagamentos_para_dict())
            
    def obter_pagamentos(self):
        return self.__pagamentos
        
    def marcar_pagamento_efetuado(self, pagamento):
        """Marca um pagamento como efetuado"""
        if pagamento in self.__pagamentos:
            pagamento.marcar_como_efetuado()
            self.__tela_pagamento.mostra_mensagem("Pagamento marcado como efetuado!")
            return True
        return False
        
    def sair(self):
        self.__tela_pagamento.mostra_mensagem('Encerrando.')
        return True