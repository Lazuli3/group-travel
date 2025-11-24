import FreeSimpleGUI as sg

class TelaPagamento:
    def mostra_mensagem(self, msg: str):
        sg.popup(msg)

    def mostra_opcoes(self):
        layout = [
            [sg.Text('Menu', font=("Arial", 14, "bold"))],
            [sg.Button('1 - Cartão de Crédito')],
            [sg.Button('2 - Pix')],
            [sg.Button('3 - Dinheiro')],
            [sg.Button('0 - Sair')]
        ]
        
        window = sg.Window('Menu Pagamento', layout)
        event, values = window.read()
        window.close()

        if event is None or event == "0 - Cancelar":
            return 0
        
        return int(event[0])  # pega apenas o primeiro caractere da string "1 - ...."

    def pega_dados_cartao(self, valor: float):
        layout = [
            [sg.Text('Pagamento (Cartão de Crédito)', font=("Arial", 14, "bold"))],
            [sg.Text('Número do Cartão:'), sg.Input(key='numero')],
            [sg.Text('Bandeira do Cartão:'), sg.Input(key='bandeira')],
            [sg.Text('Número de Parcelas:'), sg.Input(key='parcelas')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        
        window = sg.Window('Dados do Cartão', layout)
        
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None

            if event == 'Confirmar':
                numero_limpo = values['numero'].replace(" ", "").replace("-", "")
                bandeira = values['bandeira'].strip()

                if not values['numero'] or not ['bandeira']:
                    self.mostra_mensagem('Número e bandeira do cartão não podem estar vazios.')
                    continue

                dados = {
                    'num_cartao': numero_limpo,
                    'bandeira': bandeira,
                    'parcelas': values['parcelas'],
                    'valor': valor
                }
                window.close()
                return dados

    def pega_dados_pix(self, valor: float):
        layout = [
            [sg.Text('Pagamento (Pix)', font=("Arial", 14, "bold"))],
            [sg.Text('Chave Pix:'), sg.Input(key='chave')],
            [sg.Text('Banco:'), sg.Input(key='banco')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        
        window = sg.Window('Dados do Pix', layout)
        
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None

            if event == 'Confirmar':

                if not values['chave'] or not ['banco']:
                    self.mostra_mensagem('Chave e banco não podem estar vazios.')
                    continue

                dados = {
                    'chave': values['chave'],
                    'banco': values['banco'],
                    'valor': valor
                }
                window.close()
                return dados

    def pega_dados_dinheiro(self, valor: float):
        layout = [
            [sg.Text('Pagamento (Dinheiro)', font=("Arial", 14, "bold"))],
            [sg.Text(f'Valor a pagar: R$ {valor:.2f}')],
            [sg.Text('Valor entregue: R$'), sg.Input(key='valor_entregue')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        
        window = sg.Window('Dados do Dinheiro', layout)
        
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None

            if event == 'Confirmar':

                if not values['valor_entregue']:
                    self.mostra_mensagem('Valor entregue não pode estar vazio.')
                    continue

                dados = {
                    'valor_entregue': values['valor_entregue'],
                    'valor': valor
                }
                window.close()
                return dados

    def status_pagamento(self) -> bool:
        """Pergunta ao usuário se o pagamento foi realizado"""
        layout = [
            [sg.Button("Pagamento EFETUADO (Concluído)")],
            [sg.Button("Pagamento PENDENTE (Agendado ou a Confirmar)")],
            [sg.Button("Cancelar")]
        ]
        
        window = sg.Window("Status do Pagamento", layout)
        event, values = window.read()
        window.close()
        
        if event == "Pagamento EFETUADO (Concluído)":
            return True
        elif event == "Pagamento PENDENTE (Agendado ou a Confirmar)":
            return False
        else:
            return None

    def lista_pagamentos(self, pagamentos: list):
        dados = [
            [pag['id'], pag['pagante'], pag['tipo'], pag['valor'], pag['data'],
            pag['status']] for pag in pagamentos
        ]
        
        headings = [
            'ID', 'Pagante', 'Tipo', 'Valor', 'Data', 'Status'
        ]
        
        layout = [
            [sg.Text('Lista de Pagamentos', font=("Arial", 14, "bold"), justification='center')],
            [sg.Table(
                values=dados,
                headings=headings,
                auto_size_columns=True,
                justification='left',
                num_rows=min(15, len(dados)),  # Menos linhas visíveis
                key='-TABLE-',
                enable_events=False,
                display_row_numbers=False,
                alternating_row_color='#E8E8E8',
                header_background_color='#425261',
                header_text_color='white',
                background_color='white',
                text_color='black'
            )],
            [sg.Button('OK', size=(10, 1))]
        ]
        
        window = sg.Window('Lista de Pagamentos', layout, size=(500, 450), element_justification='center')
        window.read()
        window.close()
        
        #texto = ''
        #for pag in pagamentos:
        #    texto += f'''{pag['id']}. Pagante: {pag['pagante']} | Tipo: {pag['tipo']}")
        #            Valor: {pag['valor']} | Data: {pag['data']} | Status: {pag['status']}\n'''
            
        #layout = [
        #    [sg.Multiline(texto, size=(90,25), disabled=True)],
        #    [sg.Button('OK')]
        #]
        
        #window = sg.Window('Lista de Pagamentos', layout)
        #window.read()
        #window.close()


    def seleciona_pagamento(self):
        layout = [
            [sg.Text("Digite o ID do pagamento:")],
            [sg.Input(key='id')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Pagamento", layout)

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None

            if event == "OK":
                try:
                    valor = int(values['id'])
                    window.close()
                    return valor
                except ValueError:
                    sg.popup("ID inválido! Digite um número inteiro.")

    def confirma_cancelamento(self, valor: float, pagante: str):
        layout = [
            [sg.Text(f"Deseja cancelar o pagamento de R$ {valor:.2f} do pagante '{pagante}'?")],
            [sg.Button("Sim"), sg.Button("Não")]
        ]

        window = sg.Window("Confirmar Cancelamento", layout)

        event, values = window.read()
        window.close()

        return event == "Sim"
