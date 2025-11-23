import FreeSimpleGUI as sg

class TelaSistema:

    def tela_opcoes(self):
        layout = [
            [sg.Text('"-------- Viagem em Grupo ---------"')],
            [sg.Button('1 - Pessoas')],
            [sg.Button('2 - Grupos')],
            [sg.Button('3 - Locais de Viagem')],
            [sg.Button('4 - Passeio')],
            [sg.Button('5 - Passagem')],
            [sg.Button('6 - Pacote')],
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
            elif event.startswith('4'):
                window.close()
                return 4
            elif event.startswith('5'):
                window.close()
                return 5
            elif event.startswith('6'):
                window.close()
                return 6
            elif event.startswith('0'):
                window.close()
                return 0
    