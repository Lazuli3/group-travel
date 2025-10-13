
class TelaPagamento:
    def mostra_mensagem(self, msg: str):
        print(msg)

    def mostra_opcoes(self):
        while True:
            print('''============ Forma de Pagamento ============
                1 - Cartão de Crédito
                2 - Pix
                3 - Dinheiro
                0 - Sair
            ''')

            try:
                return int(input('Escolha uma das opções do menu: '))

            except ValueError:
                self.mostra_mensagem('Escolha uma opção válida do menu..')

    def pega_dados_cartao(self, valor: float):
        print('\n============ Dados do Cartão ============')
        num_cartao = input('Número do cartão: ')
        bandeira = input('Bandeira do cartão: ')
        parcelas = input('Número de parcelas: ')

        numero_limpo = num_cartao.replace(" ", "").replace("-", "")

        return {
            'num_cartao': numero_limpo,
            'bandeira': bandeira,
            'parcelas': parcelas,
            'valor': valor
        }

    def pega_dados_pix(self, valor: float):
        print('\n============ Dados do Pix ============')
        chave = input('Chave PIX: ')
        banco = input('Banco: ')

        return {
            'chave': chave,
            'banco': banco,
            'valor': valor
        }

    def pega_dados_dinheiro(self, valor: float):
        print('\n============ Pagamento em Dinheiro ============')
        self.mostra_mensagem(f'Valor a pagar: R$ {valor:.2f}')
        valor_entregue = input('Valor entregue: R$ ')

        return {
            'valor_entregue': valor_entregue,
            'valor': valor
        }

    def lista_pagamentos(self, pagamentos_dict: list):
        if not pagamentos_dict:
            self.mostra_mensagem("Nenhum pagamento registrado.")
            return

        print('\n============ Histórico de Pagamentos ============')
        for i, pag in enumerate(pagamentos_dict, 1):
            status = "[✓] Efetuado" if pag.pagamento_efetuado else "[X] Pendente"
            print(f"{i}. Pagante: {pag.pagante.nome}")
            print(f"   Valor: R$ {pag.valor:.2f}")
            print(f"   Data: {pag.data.strftime('%d/%m/%Y %H:%M')}")
            print(f"   Status: {status}\n")
