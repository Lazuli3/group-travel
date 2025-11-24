import FreeSimpleGUI as sg

class TelaPessoa:

    def mostra_opcoes(self):
        layout = [
            [sg.Text('Menu', font=("Arial", 14, "bold"))],
            [sg.Button('1 - Incluir pessoa')],
            [sg.Button('2 - Listar pessoas')],
            [sg.Button('3 - Excluir pessoa')],
            [sg.Button('0 - Sair')]
        ]

        window = sg.Window('Menu Pessoas', layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                window.close()
                return 0
            
            if event.startswith('1'):
                window.close()
                return 1
            elif event.startswith('2'):
                window.close()
                return 2
            elif event.startswith('3'):
                window.close()
                return 3
            elif event.startswith('0'):
                window.close()
                return 0


    def pega_dados_pessoa(self):
        layout = [
            [sg.Text('Dados da Pessoa', font=("Arial", 14, "bold"), justification='center')],
            [sg.Text('Nome:'), sg.Input(key='nome')],
            [sg.Text('Idade:'), sg.Input(key='idade')],
            [sg.Text('Telefone:'), sg.Input(key='telefone')],
            [sg.Text('CPF:'), sg.Input(key='cpf')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Cadastro de Pessoa', layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None

            if event == 'Confirmar':
                try:
                    idade = int(values['idade'])
                except ValueError:
                    self.mostra_mensagem('Idade deve ser um número inteiro')
                    continue

                dados = {
                    'nome': values['nome'],
                    'idade': idade,
                    'telefone': values['telefone'],
                    'cpf': values['cpf']
                }
                window.close()
                return dados

    def lista_pessoas(self, pessoas: list):
        dados = [[pessoa.nome, pessoa.idade, pessoa.telefone, pessoa.cpf] for pessoa in pessoas]
        
        headings = ['Nome', 'Idade', 'Telefone', 'CPF']
        
        layout = [
            [sg.Text('Lista de Pessoas', font=("Arial", 14, "bold"), justification='center')],
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
        
        window = sg.Window('Lista de Locais', layout, size=(500, 450), element_justification='center')
        window.read()
        window.close()
        
        #texto = '============ Lista de Pessoas ============\n\n'
        #for p in pessoas:
        #    texto += f"Nome: {p.nome} | Idade: {p.idade} | Telefone: {p.telefone} | CPF: {p.cpf}\n"

        #layout = [
        #    [sg.Multiline(texto, size=(60, 15), disabled=True)],
        #    [sg.Button('OK')]
        #]

        #window = sg.Window('Lista de Pessoas', layout)
        #window.read()
        #window.close()


    def pega_cpf(self):
        layout = [
            [sg.Text('Digite o CPF da pessoa:')],
            [sg.Input(key='cpf')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Excluir Pessoa', layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None

            if event == 'Confirmar':
                cpf = values['cpf']
                window.close()
                return cpf


    def mostra_mensagem(self, msg: str):
        sg.popup(msg)
