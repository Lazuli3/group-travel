
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

    def status_pagamento(self) -> bool:
        """Pergunta ao usuário se o pagamento foi realizado"""
        print('\n===== Status do Pagamento =====')
        print('1 - Pagamento EFETUADO (Concluído)')
        print('2 - Pagamento PENDENTE (Agendado ou a Confirmar)')
        
        while True:
            try:
                opcao = int(input('Selecione o status (1 ou 2): '))
                if opcao == 1:
                    return True  # Pagamento Efetuado
                elif opcao == 2:
                    return False # Pagamento Pendente
                else:
                    self.mostra_mensagem("Opção inválida. Digite 1 ou 2.")
            except ValueError:
                self.mostra_mensagem("Entrada inválida. Digite apenas o número 1 ou 2.")

    def lista_pagamentos(self, pagamentos_dict: list):
        if not pagamentos_dict:
            self.mostra_mensagem("Nenhum pagamento registrado.")
            return

        print('\n============ Histórico de Pagamentos ============')
        for i, pag in enumerate(pagamentos_dict, 1):
            tipo = pag['tipo'] 
            valor = pag['valor']
            pagante = pag['pagante']
            data = pag['data']
            status = pag['status']

            print(f"{i}. Pagante: {pagante} | Tipo: {tipo}")
            print(f"   Valor: R$ {valor:.2f}")
            print(f"   Data: {data}")
            print(f"   Status: {status}\n")
