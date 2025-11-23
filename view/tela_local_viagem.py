import FreeSimpleGUI as sg

class TelaLocalViagem:

    def mostra_mensagem(self, msg: str):
        sg.popup(msg)

    def mostra_opcoes(self):
        layout = [
            [sg.Text('============ Menu ============')],
            [sg.Button('1 - Incluir local de viagem')],
            [sg.Button('2 - Listar locais de viagem')],
            [sg.Button('3 - Excluir local de viagem')],
            [sg.Button('0 - Sair')]
        ]
        
        window = sg.Window('Menu Locais de viagem', layout)
        
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

    def pega_dados_local_viagem(self):
        layout = [
            [sg.Text('Cidade:'), sg.Input(key='cidade')],
            [sg.Text('País:'), sg.Input(key='pais')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        
        window = sg.Window('Cadastro de Local', layout)
        
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None

            if event == 'Confirmar':
                cidade = values['cidade'].strip()
                pais = values['pais'].strip()

                if not cidade or not pais:
                    self.mostra_mensagem('Cidade e país não podem estar vazios.')
                    continue

                if pais.isdigit() or cidade.isdigit():
                    self.mostra_mensagem('Cidade/país não devem conter apenas números.')
                    continue

                dados = {
                    'cidade': cidade,
                    'pais': pais
                }
                window.close()
                return dados

    def lista_locais_viagem(self, locais: list):
        texto = ''
        for local in locais:
            texto += f"{local['id']}. Cidade: {local['cidade']} | País: {local['pais']}\n"
            
        layout = [
            [sg.Multiline(texto, size=(90,25), disabled=True)],
            [sg.Button('OK')]
        ]
        
        window = sg.Window('Lista de Locais', layout)
        window.read()
        window.close()

    def seleciona_local(self):
        layout = [
            [sg.Text("Digite o ID do local:")],
            [sg.Input(key='id')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]
        
        window = sg.Window("Selecionar Local", layout)
        
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

    def confirma_exclusao(self, cidade_local, pais_local):
        layout = [
            [sg.Text(f"Confirma a exclusão do local de viagem: '{cidade_local}, {pais_local}'?")],
            [sg.Button("Sim"), sg.Button("Não")]
        ]

        window = sg.Window("Confirmar Exclusão", layout)

        event, values = window.read()
        window.close()

        return event == "Sim"