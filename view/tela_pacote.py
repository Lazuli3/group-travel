import FreeSimpleGUI as sg

class TelaPacote:
    """Interface gráfica de pacotes usando FreeSimpleGUI"""

    # ===================== MENU PRINCIPAL ======================
    def mostra_opcoes(self):
        layout = [
            [sg.Text("Gerenciamento de Pacotes", justification='center', font=("Arial", 14))],
            [sg.Button("1 - Incluir Pacote")],
            [sg.Button("2 - Listar Pacotes")],
            [sg.Button("3 - Alterar Pacote")],
            [sg.Button("4 - Excluir Pacote")],
            [sg.Button("0 - Voltar")],
        ]

        window = sg.Window("Menu de Pacotes", layout)
        event, values = window.read()
        window.close()

        if event is None:
            return 0
        return int(event[0])  # pega apenas o primeiro caractere da string "1 - ...."

    def mostra_menu_alteracao(self):
        """Menu de opções para alteração"""
        layout = [
            [sg.Text("Menu", justification='center', font=("Arial", 14))],
            [sg.Button("1 - Adicionar Passagem")],
            [sg.Button("2 - Remover Passagem")],
            [sg.Button("3 - Adicionar Passeio")],
            [sg.Button("4 - Remover Passeio")],
            [sg.Button("5 - Adicionar Pagamento")],
            [sg.Button("6 - Cancelar Pagamento")],
            [sg.Button("0 - Cancelar")]
        ]

        window = sg.Window("Alteração de Pacote", layout)
        event, values = window.read()
        window.close()

        if event is None or event == "0 - Cancelar":
            return 0
        
        return int(event[0])
    
    #PEDIR ID
    def pega_id_grupo(self):
        layout = [
            [sg.Text("Digite o ID do grupo:")],
            [sg.Input(key="id")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("ID do Grupo", layout)
        event, values = window.read()
        window.close()

        if event == "OK" and values["id"] != "":
            try:
                return int(values["id"])
            except:
                return None
        return None

    def pega_id_passeio(self):
        """Pede o ID do passeio"""
        layout = [
            [sg.Text("Digite o ID do passeio:")],
            [sg.Input(key="id")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("ID do Passeio", layout)
        event, values = window.read()
        window.close()

        if event == "OK" and values["id"] != "":
            try:
                return int(values["id"])
            except:
                return None
        return None

    def pega_id_passagem(self):
        """Pede o ID da passagem"""
        layout = [
            [sg.Text("Digite o ID da passagem:")],
            [sg.Input(key="id")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("ID da Passagem", layout)
        event, values = window.read()
        window.close()

        if event == "OK" and values["id"] != "":
            try:
                return int(values["id"])
            except:
                return None
        return None
    
    def pega_id_pagamento(self):
        """Pede o ID do pagamento"""
        layout = [
            [sg.Text("Digite o ID do pagamento:")],
            [sg.Input(key="id")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("ID do Pagamento", layout)
        event, values = window.read()
        window.close()

        if event == "OK" and values["id"] != "":
            try:
                return int(values["id"])
            except:
                return None
        return None

    #CONFIRMA ADIÇÃO
    def confirma_adicao(self, tipo):
        layout = [
            [sg.Text(f"Deseja adicionar {tipo}?")],
            [sg.Button("Sim"), sg.Button("Não")]
        ]

        window = sg.Window("Confirmar Adição", layout)
        event, values = window.read()
        window.close()

        return event == "Sim"

    #SELECIONA PACOTE
    def seleciona_pacote(self):
        layout = [
            [sg.Text("Digite o ID do pacote:")],
            [sg.Input(key="numero")],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Pacote", layout)
        event, values = window.read()
        window.close()

        if event == "OK" and values["numero"] != "":
            try:
                return int(values["numero"])
            except:
                return None
        return None

    def seleciona_membro(self, membros):
        """Mostra lista de membros e retorna o CPF escolhido"""
        dados = [
            [i, membro.nome, membro.cpf] for i, membro in enumerate(membros, 1)
        ]
        
        headings = ['Nº', 'Nome', 'CPF']
        
        layout = [
            [sg.Text('Selecionar Membro', font=("Arial", 14, "bold"), justification='center')],
            [sg.Table(
                values=dados,
                headings=headings,
                auto_size_columns=True,
                justification='left',
                num_rows=min(15, len(dados)),
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

        window = sg.Window("Seleção de Membros", layout, size=(400, 450), element_justification='center')
        window.read()
        window.close()
        
        layout_cpf = [
            [sg.Text("Digite o CPF do membro:")],
            [sg.Input(key='cpf')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        window_cpf = sg.Window("CPF", layout_cpf)
        event, values = window_cpf.read()
        window_cpf.close()
        
        if event == "OK":
            return values['cpf']
        return None

    #LISTAR PACOTES
    def lista_pacotes(self, pacotes):
        dados = [
            [p['id'], p['grupo'], p['total_passagens'], p['total_passeios'], f'R$ {p['valor_total']:.2f}',
            f'R$ {p['valor_pago']:.2f}', f'R$ {p['valor_restante']:.2f}'] for p in pacotes
        ]
        
        headings = ['ID', 'Grupo', 'Passagens', 'Passeios', 'Total', 'Pago', 'Restante']
        
        layout = [
            [sg.Text('Lista de Pacotes', font=("Arial", 14, "bold"), justification='center')],
            [sg.Table(
                values=dados,
                headings=headings,
                auto_size_columns=True,
                justification='left',
                num_rows=min(15, len(dados)),
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

        window = sg.Window("Lista de Pacotes", layout, size=(800, 450), element_justification='center')
        window.read()
        window.close()

    #CONFIRMA EXCLUSÃO
    def confirma_exclusao(self, nome_grupo):
        layout = [
            [sg.Text(f"Deseja excluir o pacote do grupo '{nome_grupo}'?")],
            [sg.Button("Sim"), sg.Button("Não")],
        ]

        window = sg.Window("Excluir Pacote", layout)
        event, _ = window.read()
        window.close()

        return event == "Sim"

    def mostra_mensagem(self, mensagem):
        sg.Popup(mensagem)
        
    #MOSTRAR ELEMENTOS DO PACOTE
    def mostra_pagamentos_pacote(self, pagamentos):
        """Mostra os pagamentos de um pacote específico"""
        if not pagamentos:
            self.mostra_mensagem("Não há pagamentos no pacote.")
            return

        dados = [
            [pagamento.id, pagamento.pagante.nome, pagamento.valor,
            "Efetuado" if pagamento.pagamento_efetuado else "Pendente"]
            for pagamento in pagamentos
        ]
        
        headings = ['ID', 'Pagante', 'Valor', 'Status']
        
        layout = [
            [sg.Text('Pagamentos do Pacote', font=("Arial", 14, "bold"), justification='center')],
            [sg.Table(
                values=dados,
                headings=headings,
                auto_size_columns=True,
                justification='left',
                num_rows=min(15, len(dados)),
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
        
        window = sg.Window('Pagamentos do Pacote', layout, size=(400, 450), element_justification='center')
        window.read()
        window.close()
    
    def mostra_passagens_pacote(self, passagens):
        """Mostra as passagens de um pacote específico"""
        dados = [
            [passagem.id, passagem.local_origem.cidade, passagem.local_destino.cidade] for passagem in passagens
        ]
        
        headings = ['ID', 'Local de Origem', 'Local de Destino']
        
        layout = [
            [sg.Text('Passagens do Pacote', font=("Arial", 14, "bold"), justification='center')],
            [sg.Table(
                values=dados,
                headings=headings,
                auto_size_columns=True,
                justification='left',
                num_rows=min(15, len(dados)),
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
        
        window = sg.Window('Passagens do Pacote', layout, size=(350, 450), element_justification='center')
        window.read()
        window.close()
    
    def mostra_passeios_pacote(self, passeios):
        """Mostra os passeios de um pacote específico"""
        dados = [
            [passeios.id, passeios.atracao_turistica] for passeio in passeios
        ]
        
        headings = ['ID', 'Atração']
        
        layout = [
            [sg.Text('Passeios do Pacote', font=("Arial", 14, "bold"), justification='center')],
            [sg.Table(
                values=dados,
                headings=headings,
                auto_size_columns=True,
                justification='left',
                num_rows=min(15, len(dados)),
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
        
        window = sg.Window('Passeios do Pacote', layout, size=(300, 450), element_justification='center')
        window.read()
        window.close()
    
    def mostra_info_pagamento(self, valor_total, valor_pago, valor_restante):
        dados = [[valor_total, valor_pago, valor_restante]]
        
        headings = [
            'Total', 'Valor pago', 'Valor restante'
        ]
        
        layout = [
            [sg.Text('Informações do Pagamento', font=("Arial", 14, "bold"), justification='center')],
            [sg.Table(
                values=dados,
                headings=headings,
                auto_size_columns=True,
                justification='left',
                num_rows=min(15, len(dados)),
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
        
        window = sg.Window('Informações do Pagamento', layout, size=(400, 450), element_justification='center')
        window.read()
        window.close()
