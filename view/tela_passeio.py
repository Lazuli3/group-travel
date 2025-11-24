import FreeSimpleGUI as sg
from datetime import datetime

class TelaPasseioTuristico:
    def mostra_mensagem(self, msg:str):
        sg.popup(msg)

    def mostra_opcoes(self):
        layout = [
            [sg.Text('Menu', font=("Arial", 14, "bold"))],
            [sg.Button('1 - Incluir passeio turístico')],
            [sg.Button('2 - Listar passeios turísticos')],
            [sg.Button('3 - Excluir passeio turístico')],
            [sg.Button('0 - Sair')]
        ]
        
        window = sg.Window('Menu Passeios Turísticos', layout)
        
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

    def pega_dados_passeio(self):
        horas = [f'{i:02d}' for i in range(0, 24)]
        minutos = [f'{i:02d}' for i in range(0, 60)]
        
        layout = [
            [sg.Text('Dados do Passeio', font=("Arial", 14, "bold"))],
            [sg.Text('Atração turística:'), sg.Input(key='atracao')],
            [sg.Text('Cidade:'), sg.Input(key='cidade')],
            [sg.Text('País:'), sg.Input(key='pais')],
            [sg.Text('Data:'), sg.Input(key='dia', disabled=True, size=(12,1)), 
            sg.CalendarButton('Selecionar', target='dia', format='%d/%m/%Y')],
            [sg.Text('Horário de início:'), 
            sg.Combo(horas, default_value='09', key='hora_inicio', readonly=True, size=(5,1)),
            sg.Text(':'),
            sg.Combo(minutos, default_value='00', key='minuto_inicio', readonly=True, size=(5,1))],
            [sg.Text('Horário de fim:'), 
            sg.Combo(horas, default_value='18', key='hora_fim', readonly=True, size=(5,1)),
            sg.Text(':'),
            sg.Combo(minutos, default_value='00', key='minuto_fim', readonly=True, size=(5,1))],
            [sg.Text('Valor (R$):'), sg.Input(key='valor')],
            [sg.Text('ID do grupo:'), sg.Input(key='id_grupo')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        
        window = sg.Window('Cadastro de Passeio', layout)

        while True:
            event, values = window.read()
            
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None

            if event == 'Confirmar':
                if not values['dia']:
                    sg.popup('Por favor, selecione a data!')
                    continue
                
                try:
                    data_passeio = datetime.strptime(values['dia'], '%d/%m/%Y')
                    data_hoje = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                    
                    if data_passeio < data_hoje:
                        sg.popup('Erro: A data do passeio não pode ser no passado!')
                        continue
                except ValueError:
                    sg.popup('Formato de data inválido!')
                    continue
                
                # Monta os horários no formato HH:MM
                horario_inicio = f"{values['hora_inicio']}:{values['minuto_inicio']}"
                horario_fim = f"{values['hora_fim']}:{values['minuto_fim']}"
                
                dados = {
                    'atracao_turistica': values['atracao'],
                    'cidade': values['cidade'],
                    'pais': values['pais'],
                    'dia': values['dia'],
                    'horario_inicio': horario_inicio,
                    'horario_fim': horario_fim,
                    'valor': values['valor'],
                    'id_grupo': values['id_grupo']
                }
                window.close()
                return dados

    def seleciona_passeio(self):
        layout = [
            [sg.Text("Digite o ID do passeio:")],
            [sg.Input(key='id')],
            [sg.Button("OK"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Grupo", layout)

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
                    
    def lista_passeios_turisticos(self, passeios: list):
        dados = [
            [passeio['id'], passeio['atracao'], passeio['localizacao'],
            passeio['horario_inicio'], passeio['horario_fim'],
            passeio['valor'], passeio['grupo']] for passeio in passeios
        ]
        
        headings = [
            'ID', 'Atração', 'Local', 'Início', 'Fim', 'Valor', 'Grupo'
        ]
        
        layout = [
            [sg.Text('Lista de Locais', font=("Arial", 14, "bold"), justification='center')],
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
        
        window = sg.Window('Lista de Locais', layout, size=(800, 450), element_justification='center')
        window.read()
        window.close()
        
        #texto = ''
        #for passeio in passeios:
        #    texto += f'''{passeio['id']}. Atração: {passeio['atracao']}
        #           Localização: {passeio['localizacao']}
        #           Horário de início: {passeio['horario_inicio']}
        #           Horário de fim: {passeio['horario_fim']}
        #           Valor: {passeio['valor']}
        #           Grupo do passeio: {passeio['grupo']}\n'''
            
        #layout = [
        #    [sg.Multiline(texto, size=(90,25), disabled=True)],
        #    [sg.Button('OK')]
        #]
        
        #window = sg.Window('Lista de Passeios', layout)
        #window.read()
        #window.close()

    def confirma_exclusao(self, atracao_turistica, nome_grupo):
        layout = [
            [sg.Text(f"Você confirma a exclusão do passeio turístico '{atracao_turistica}' do grupo '{nome_grupo}'?")],
            [sg.Button("Sim"), sg.Button("Não")]
        ]

        window = sg.Window("Confirmar Exclusão", layout)

        event, values = window.read()
        window.close()

        return event == "Sim"
    
    #adicionando método para vinculo com exclusão

    def confirma_exclusao_com_vinculo(self, atracao, vinculo_info):
        """Confirma exclusão quando há vínculos"""
        layout = [
            [sg.Text(f"⚠️ O passeio '{atracao}' está vinculado ao {vinculo_info}.")],
            [sg.Text("Deseja remover do pacote e excluir?")],
            [sg.Button("Sim"), sg.Button("Não")],
        ]

        window = sg.Window("Confirmar Exclusão", layout)
        event, _ = window.read()
        window.close()

        return event == "Sim"
