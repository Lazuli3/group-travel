import FreeSimpleGUI as sg
sg.set_options(font=("Arial", 11))

class TelaSistema:

    def tela_opcoes(self):
        layout = [
            [sg.Text('Viagem em Grupo', font=("Arial", 14, "bold"), justification='center')],
            [sg.Button('1 - Pessoas')],
            [sg.Button('2 - Grupos')],
            [sg.Button('3 - Locais de Viagem')],
            [sg.Button('4 - Passeio Turístico')],
            [sg.Button('5 - Passagem')],
            [sg.Button('6 - Pacote')],
            [sg.Button('7 - Relatório')],
            [sg.Button('0 - Sair')]
        ]

        window = sg.Window('Menu Viagem', layout)

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
            elif event.startswith('7'):
                window.close()
                return 7
            elif event.startswith('0'):
                window.close()
                return 0
    
    def mostrar_relatorio(self, dados):
        destino_popular, destino_caro, destino_barato, passeio_popular, passeio_caro, passeio_barato = dados
        
        layout = [
            [sg.Text('RELATÓRIO DO SISTEMA', font=("Arial", 14, "bold"), justification='center')],
            [sg.HorizontalSeparator()],
            
            [sg.Text('DESTINOS', font=("Arial", 12, "bold"))],
            [sg.Text(f"Mais Popular: {destino_popular['nome']} ({destino_popular['visitas']} visitas)")],
            [sg.Text(f"Mais Caro: {destino_caro['nome']} (R$ {destino_caro['valor']:.2f})")],
            [sg.Text(f"Mais Barato: {destino_barato['nome']} (R$ {destino_barato['valor']:.2f})")],
            
            [sg.HorizontalSeparator()],
            
            [sg.Text('PASSEIOS', font=("Arial", 12, "bold"))],
            [sg.Text(f"Mais Popular: {passeio_popular['nome']} ({passeio_popular['quantidade']} pacotes)")],
            [sg.Text(f"Mais Caro: {passeio_caro['nome']} (R$ {passeio_caro['valor']:.2f})")],
            [sg.Text(f"Mais Barato: {passeio_barato['nome']} (R$ {passeio_barato['valor']:.2f})")],
            
            [sg.HorizontalSeparator()],
            [sg.Button('Fechar')]
        ]
        
        window = sg.Window('Relatório', layout, modal=True)
        
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Fechar'):
                window.close()
                break